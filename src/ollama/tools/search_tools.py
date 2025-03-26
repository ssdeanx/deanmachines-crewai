"""
Search tools implementation with Serper API integration.
Includes MLflow performance tracking and error handling.
"""
from typing import Dict, List
import os
import json
import time
import logging
import mlflow
import requests
from ..utils.retry_utils import retry_with_backoff

# Configure logging
logger = logging.getLogger(__name__)

class SearchResult(Dict):
    """Type hint for search result structure"""
    title: str
    link: str
    snippet: str

class SerperSearchTool:
    """Search tool using Serper API with error handling and metrics"""

    def __init__(self):
        """Initialize Serper API tool"""
        self.api_key = os.getenv("SERPER_API_KEY")
        if not self.api_key:
            raise ValueError("SERPER_API_KEY environment variable is required")
        self._setup_mlflow()

    def _setup_mlflow(self) -> None:
        """Set up MLflow tracking"""
        try:
            if tracking_uri := os.getenv("MLFLOW_TRACKING_URI"):
                mlflow.set_tracking_uri(tracking_uri)
                mlflow.set_experiment("search_tools_monitoring")
                logger.info("MLflow tracking configured successfully")
        except Exception as e:
            logger.warning(f"Failed to setup MLflow tracking: {e}")

    def _log_metrics(self, metrics: Dict[str, float]) -> None:
        """Log metrics to MLflow if available"""
        try:
            mlflow.log_metrics(metrics)
        except Exception as e:
            logger.debug(f"Failed to log metrics: {e}")

    @retry_with_backoff(max_attempts=3)
    def search(self, query: str, max_results: int = 5) -> List[SearchResult]:
        """
        Execute search using Serper API

        Args:
            query: Search query string
            max_results: Maximum number of results to return

        Returns:
            List of search results

        Raises:
            requests.RequestException: If API request fails
            ValueError: If API response is invalid
        """
        start_time = time.time()
        results = []  # Define results here for finally block
        try:
            headers = {
                "X-API-KEY": self.api_key,
                "Content-Type": "application/json"
            }

            response = requests.get(
                "https://google.serper.dev/search",
                headers=headers,
                params={"q": query, "num": max_results},
                timeout=10
            )
            response.raise_for_status()

            raw_results = response.json().get("organic", [])
            results = [
                SearchResult({
                    "title": result.get("title", ""),
                    "link": result.get("link", ""),
                    "snippet": result.get("snippet", "")
                })
                for result in raw_results[:max_results]
            ]

            return results

        except requests.RequestException as e:
            logger.error(f"Serper API request failed: {e}")
            return []
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON response: {e}")
            return []
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            return []
        finally:
            execution_time = time.time() - start_time
            # Log metrics
            self._log_metrics({
                "serper_search_time": execution_time,
                "serper_results_count": len(results),
                "serper_success": 1 if results else 0
            })

def get_search_tool() -> SerperSearchTool:
    """Factory function to get a configured search tool instance"""
    return SerperSearchTool()
