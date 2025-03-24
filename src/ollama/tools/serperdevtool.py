from typing import Optional, Dict, List, Type
from pydantic import BaseModel, Field
from crewai.tools import BaseTool
import requests
import os
from datetime import datetime

class SerperSearchInput(BaseModel):
    """Input schema for Serper.dev search."""
    query: str = Field(..., description="Search query")
    search_type: str = Field(
        default="search",
        description="Type of search (search, news, places, images)"
    )
    num_results: int = Field(default=10, description="Number of results to return")
    include_domains: Optional[List[str]] = Field(
        default=None,
        description="List of domains to include in search"
    )
    exclude_domains: Optional[List[str]] = Field(
        default=None,
        description="List of domains to exclude from search"
    )

class SerperDevTool(BaseTool):
    name: str = "serper_search_tool"
    description: str = "Perform web searches using Serper.dev API"
    args_schema: Type[BaseModel] = SerperSearchInput
    
    def __init__(self):
        self.api_key = os.getenv("SERPER_API_KEY")
        if not self.api_key:
            raise ValueError("SERPER_API_KEY environment variable not set")
        self.base_url = "https://google.serper.dev"
        
    def _run(
        self,
        query: str,
        search_type: str = "search",
        num_results: int = 10,
        include_domains: Optional[List[str]] = None,
        exclude_domains: Optional[List[str]] = None
    ) -> Dict:
        """
        Perform search using Serper.dev API with advanced filtering
        """
        headers = {
            "X-API-KEY": self.api_key,
            "Content-Type": "application/json"
        }
        
        # Build search parameters
        params = {
            "q": query,
            "num": num_results
        }
        
        # Add domain filters if specified
        if include_domains:
            params["q"] += f" site:({' OR '.join(include_domains)})"
        if exclude_domains:
            params["q"] += f" -site:({' OR '.join(exclude_domains)})"

        # Determine endpoint based on search type
        endpoint = f"/{search_type}"
        
        try:
            response = requests.post(
                f"{self.base_url}{endpoint}",
                headers=headers,
                json=params
            )
            response.raise_for_status()
            
            results = response.json()
            
            # Add metadata to results
            return {
                "timestamp": datetime.now().isoformat(),
                "query": query,
                "search_type": search_type,
                "num_results": num_results,
                "filters": {
                    "include_domains": include_domains,
                    "exclude_domains": exclude_domains
                },
                "results": results
            }
            
        except requests.exceptions.RequestException as e:
            return {
                "error": str(e),
                "timestamp": datetime.now().isoformat(),
                "query": query
            }

class SerperNewsInput(BaseModel):
    """Input schema for news search."""
    query: str = Field(..., description="News search query")
    time_range: str = Field(
        default="all",
        description="Time range for news (day, week, month, year, all)"
    )
    sort_by: str = Field(
        default="relevance",
        description="Sort order (relevance, date)"
    )

class SerperNewsTool(SerperDevTool):
    name: str = "serper_news_tool"
    description: str = "Search news articles using Serper.dev API"
    args_schema: Type[BaseModel] = SerperNewsInput
    
    def _run(
        self,
        query: str,
        time_range: str = "all",
        sort_by: str = "relevance"
    ) -> Dict:
        """
        Perform news search with time range and sorting options
        """
        params = {
            "q": query,
            "type": "news",
            "timeRange": time_range,
            "sortBy": sort_by
        }
        
        return super()._run(**params)