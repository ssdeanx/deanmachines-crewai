from typing import Dict, List, Optional
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from ..utils.webdriver_utils import WebDriverManager
import requests
import json
import os
import logging
import mlflow
import time
from datetime import datetime

logger = logging.getLogger(__name__)

class BaseSearchTool:
    """Base class for search implementations"""
    def search(self, query: str, **kwargs) -> List[Dict]:
        raise NotImplementedError

class SeleniumSearchTool(BaseSearchTool):
    """Search tool using Selenium with automated WebDriver management"""
    def __init__(self, headless: bool = True):
        self.headless = headless

    def search(self, query: str, max_results: int = 5, timeout: int = 10) -> List[Dict]:
        start_time = time.time()
        driver = None
        results = []

        try:
            driver = WebDriverManager.get_chrome_driver(headless=self.headless)
            search_url = f"https://www.google.com/search?q={query}"
            driver.get(search_url)

            WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.g"))
            )

            search_results = driver.find_elements(By.CSS_SELECTOR, "div.g")
            for result in search_results[:max_results]:
                try:
                    title = result.find_element(By.CSS_SELECTOR, "h3").text
                    link = result.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
                    snippet = result.find_element(By.CSS_SELECTOR, "div.VwiC3b").text

                    results.append({
                        "title": title,
                        "link": link,
                        "snippet": snippet
                    })
                except Exception as e:
                    logger.warning(f"Error extracting result: {str(e)}")
                    continue

            return results

        except TimeoutException:
            logger.error("Search timeout")
            return []
        except Exception as e:
            logger.error(f"Search error: {str(e)}")
            return []
        finally:
            execution_time = time.time() - start_time
            if driver:
                try:
                    driver.quit()
                except:
                    pass
            try:
                mlflow.log_metric("selenium_search_time", execution_time)
                mlflow.log_metric("selenium_results_count", len(results))
            except:
                pass

class SerperSearchTool(BaseSearchTool):
    """Search tool using Serper API"""
    def __init__(self):
        self.api_key = os.getenv("SERPER_API_KEY")
        if not self.api_key:
            raise ValueError("SERPER_API_KEY environment variable is required")

    def search(self, query: str, max_results: int = 5) -> List[Dict]:
        start_time = time.time()
        try:
            headers = {
                "X-API-KEY": self.api_key,
                "Content-Type": "application/json"
            }
            response = requests.get(
                "https://google.serper.dev/search",
                headers=headers,
                params={"q": query, "num": max_results}
            )
            response.raise_for_status()
            results = response.json()["organic"]

            execution_time = time.time() - start_time
            try:
                mlflow.log_metric("serper_search_time", execution_time)
                mlflow.log_metric("serper_results_count", len(results))
            except:
                pass

            return results
        except Exception as e:
            logger.error(f"Serper search error: {str(e)}")
            return []

class SearchManager:
    """Manager for coordinating different search tools"""
    def __init__(self):
        self.selenium_search = SeleniumSearchTool()
        try:
            self.serper_search = SerperSearchTool()
        except ValueError:
            self.serper_search = None
        self._setup_mlflow()

    def _setup_mlflow(self):
        try:
            mlflow.set_tracking_uri(os.getenv("MLFLOW_TRACKING_URI"))
            mlflow.set_experiment("search_performance_monitoring")
        except:
            logger.warning("Failed to setup MLflow tracking")

    def search(self,
              query: str,
              tool: str = "selenium",
              max_results: int = 5) -> List[Dict]:
        """
        Perform search using specified tool
        Args:
            query: Search query
            tool: "selenium" or "serper"
            max_results: Maximum number of results
        """
        with mlflow.start_run(nested=True):
            mlflow.log_params({
                "search_tool": tool,
                "max_results": max_results,
                "query": query
            })

            start_time = time.time()
            try:
                if tool == "selenium":
                    results = self.selenium_search.search(query, max_results=max_results)
                elif tool == "serper" and self.serper_search:
                    results = self.serper_search.search(query, max_results=max_results)
                else:
                    raise ValueError(f"Unsupported search tool: {tool}")

                execution_time = time.time() - start_time
                mlflow.log_metrics({
                    "total_execution_time": execution_time,
                    "results_count": len(results),
                    "success": 1
                })

                return results
            except Exception as e:
                mlflow.log_metrics({
                    "success": 0,
                    "error_count": 1
                })
                raise

    def parallel_search(self,
                       query: str,
                       max_results: int = 5) -> Dict[str, List[Dict]]:
        """Run searches in parallel using all available tools"""
        with mlflow.start_run(nested=True):
            mlflow.log_params({
                "search_mode": "parallel",
                "max_results": max_results,
                "query": query
            })

            results = {}
            start_time = time.time()

            # Add Selenium results
            try:
                results["selenium"] = self.selenium_search.search(
                    query,
                    max_results=max_results
                )
            except Exception as e:
                logger.error(f"Selenium search failed: {str(e)}")
                results["selenium"] = []

            # Add Serper results if available
            if self.serper_search:
                try:
                    results["serper"] = self.serper_search.search(
                        query,
                        max_results=max_results
                    )
                except Exception as e:
                    logger.error(f"Serper search failed: {str(e)}")
                    results["serper"] = []

            execution_time = time.time() - start_time
            mlflow.log_metrics({
                "total_execution_time": execution_time,
                "selenium_results": len(results.get("selenium", [])),
                "serper_results": len(results.get("serper", [])),
                "success": 1 if any(results.values()) else 0
            })

            return results
