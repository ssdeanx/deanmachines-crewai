from typing import Dict, List, Optional
import os
from .model_utils import ModelManager

class ModelCoordinator:
    def __init__(self):
        self.model_manager = ModelManager()
        self.model_priority = eval(os.getenv("MODEL_PRIORITY", "['gemini', 'lmstudio', 'ollama']"))
        self.enable_fallback = os.getenv("ENABLE_MODEL_FALLBACK", "true").lower() == "true"
        self.parallel_execution = os.getenv("PARALLEL_MODEL_EXECUTION", "false").lower() == "true"

    def get_available_models(self) -> List[str]:
        available = []
        for model_type in self.model_priority:
            if self.model_manager.validate_model_config(model_type):
                available.append(model_type)
        return available

    def get_primary_model(self) -> Optional[Dict]:
        available = self.get_available_models()
        if not available:
            raise RuntimeError("No models available")

        primary = available[0]
        if primary == "gemini":
            return {"type": "gemini", "model": self.model_manager.get_gemini_model()}
        elif primary == "lmstudio":
            return {"type": "lmstudio", "model": self.model_manager.get_lmstudio_model()}
        return None

    def get_fallback_model(self, failed_type: str) -> Optional[Dict]:
        if not self.enable_fallback:
            return None

        available = self.get_available_models()
        try:
            current_index = available.index(failed_type)
            if current_index + 1 < len(available):
                next_type = available[current_index + 1]
                if next_type == "gemini":
                    return {"type": "gemini", "model": self.model_manager.get_gemini_model()}
                elif next_type == "lmstudio":
                    return {"type": "lmstudio", "model": self.model_manager.get_lmstudio_model()}
        except ValueError:
            pass
        return None
