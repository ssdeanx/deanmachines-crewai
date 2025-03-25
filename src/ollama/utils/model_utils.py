from typing import Dict, Optional
import os
import google.generativeai as genai
import requests
from ..config import load_model_config

class ModelManager:
    def __init__(self):
        self.model_config = load_model_config()
        self._initialize_clients()

    def _initialize_clients(self):
        # Initialize Gemini
        api_key = os.getenv("GEMINI_API_KEY")
        if api_key:
            genai.configure(api_key=api_key)
            self.default_model = os.getenv("GEMINI_MODEL", "models/gemini-2.0-flash")

        # Initialize LM Studio
        self.lmstudio_url = os.getenv("LMSTUDIO_API_URL", "http://localhost:1234")

    def get_gemini_model(self, model_name: Optional[str] = None) -> genai.GenerativeModel:
        model = model_name or self.default_model
        generation_config = {
            "temperature": float(os.getenv("GEMINI_TEMPERATURE", 0.7)),
            "top_p": float(os.getenv("GEMINI_TOP_P", 0.95)),
            "max_output_tokens": int(os.getenv("GEMINI_MAX_TOKENS", 8192))
        }
        return genai.GenerativeModel(
            model_name=model,
            generation_config=generation_config
        )

    def get_lmstudio_model(self, model_name: Optional[str] = None) -> Dict:
        model = model_name or os.getenv("LMSTUDIO_MODEL", "gemma-3-4b-it")
        return {
            "model": model,
            "api_base": self.lmstudio_url,
            "context_size": int(os.getenv("LMSTUDIO_CONTEXT_SIZE", 4096)),
            "max_tokens": int(os.getenv("LMSTUDIO_MAX_TOKENS", 2048)),
            "temperature": float(os.getenv("LMSTUDIO_TEMPERATURE", 0.7)),
            "top_p": float(os.getenv("LMSTUDIO_TOP_P", 0.95))
        }

    def validate_model_config(self, model_type: str) -> bool:
        if model_type == "gemini":
            return bool(os.getenv("GEMINI_API_KEY"))
        elif model_type == "lmstudio":
            try:
                response = requests.get(f"{self.lmstudio_url}/v1/models")
                return response.status_code == 200
            except:
                return False
        return False
