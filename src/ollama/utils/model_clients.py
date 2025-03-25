import os
import google.generativeai as genai
import requests
from typing import Dict, Any, List
from ..tools.search_tools import SearchManager

class GeminiClient:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(os.getenv("GEMINI_MODEL", "models/gemini-2.0-flash"))
        self.search_manager = SearchManager()

    def generate_text(self, prompt: str, **kwargs) -> Dict[str, Any]:
        response = self.model.generate_content(prompt)
        return {"text": response.text, "model": "gemini"}

    def chat_completion(self, messages: List[Dict[str, str]], **kwargs) -> Dict[str, Any]:
        chat = self.model.start_chat(history=[])
        response = chat.send_message(messages[-1]["content"])
        return {"response": response.text, "model": "gemini"}

    def search_and_generate(self, query: str, search_tool: str = "selenium") -> Dict[str, Any]:
        # First perform web search
        search_results = self.search_manager.search(query, tool=search_tool)

        # Format search results for model context
        context = "Based on these search results:\n"
        for result in search_results:
            context += f"- {result['title']}: {result['snippet']}\n"

        # Generate response with search context
        response = self.model.generate_content(f"{context}\n\nAnalyze and summarize the information about: {query}")
        return {
            "text": response.text,
            "model": "gemini",
            "search_results": search_results
        }

class LMStudioClient:
    def __init__(self):
        self.api_url = os.getenv("LMSTUDIO_API_URL", "http://localhost:1234")
        self.model = os.getenv("LMSTUDIO_MODEL", "gemma-3-4b-it")
        self.search_manager = SearchManager()

    def generate_text(self, prompt: str, **kwargs) -> Dict[str, Any]:
        response = requests.post(
            f"{self.api_url}/v1/completions",
            json={
                "model": self.model,
                "prompt": prompt,
                "max_tokens": int(os.getenv("LMSTUDIO_MAX_TOKENS", 2048)),
                "temperature": float(os.getenv("LMSTUDIO_TEMPERATURE", 0.7))
            }
        )
        response.raise_for_status()
        return {
            "text": response.json()["choices"][0]["text"],
            "model": "lmstudio"
        }

    def chat_completion(self, messages: List[Dict[str, str]], **kwargs) -> Dict[str, Any]:
        response = requests.post(
            f"{self.api_url}/v1/chat/completions",
            json={
                "model": self.model,
                "messages": messages,
                "max_tokens": int(os.getenv("LMSTUDIO_MAX_TOKENS", 2048)),
                "temperature": float(os.getenv("LMSTUDIO_TEMPERATURE", 0.7))
            }
        )
        response.raise_for_status()
        return {
            "response": response.json()["choices"][0]["message"]["content"],
            "model": "lmstudio"
        }

    def search_and_generate(self, query: str, search_tool: str = "selenium") -> Dict[str, Any]:
        search_results = self.search_manager.search(query, tool=search_tool)

        context = "Based on these search results:\n"
        for result in search_results:
            context += f"- {result['title']}: {result['snippet']}\n"

        response = self.generate_text(f"{context}\n\nAnalyze and summarize the information about: {query}")
        return {
            "text": response["text"],
            "model": "lmstudio",
            "search_results": search_results
        }
