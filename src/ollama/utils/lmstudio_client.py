import requests
import json
from typing import Dict, Any, Optional
import os

class LMStudioClient:
    def __init__(self):
        self.api_url = os.getenv("LMSTUDIO_API_URL", "http://localhost:1234")
        self.model = os.getenv("LMSTUDIO_MODEL", "gemma-3-4b-it")

    def generate_text(self, prompt: str, **kwargs) -> Dict[str, Any]:
        headers = {"Content-Type": "application/json"}
        data = {
            "model": self.model,
            "prompt": prompt,
            "max_tokens": kwargs.get("max_tokens", int(os.getenv("LMSTUDIO_MAX_TOKENS", 2048))),
            "temperature": kwargs.get("temperature", float(os.getenv("LMSTUDIO_TEMPERATURE", 0.7))),
            "top_p": kwargs.get("top_p", float(os.getenv("LMSTUDIO_TOP_P", 0.95))),
            "stream": False
        }

        response = requests.post(
            f"{self.api_url}/v1/completions",
            headers=headers,
            json=data
        )
        response.raise_for_status()
        return response.json()

    def chat_completion(self, messages: list, **kwargs) -> Dict[str, Any]:
        headers = {"Content-Type": "application/json"}
        data = {
            "model": self.model,
            "messages": messages,
            "max_tokens": kwargs.get("max_tokens", int(os.getenv("LMSTUDIO_MAX_TOKENS", 2048))),
            "temperature": kwargs.get("temperature", float(os.getenv("LMSTUDIO_TEMPERATURE", 0.7))),
            "top_p": kwargs.get("top_p", float(os.getenv("LMSTUDIO_TOP_P", 0.95))),
            "stream": False
        }

        response = requests.post(
            f"{self.api_url}/v1/chat/completions",
            headers=headers,
            json=data
        )
        response.raise_for_status()
        return response.json()

    def get_model_info(self) -> Optional[Dict[str, Any]]:
        try:
            response = requests.get(f"{self.api_url}/v1/models")
            response.raise_for_status()
            return response.json()
        except:
            return None
