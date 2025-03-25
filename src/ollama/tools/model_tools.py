from abc import ABC, abstractmethod
from typing import Dict, Any, Optional
from ..utils.model_coordinator import ModelCoordinator

class BaseModelTool(ABC):
    def __init__(self):
        self.coordinator = ModelCoordinator()
        self.current_model = None

    @abstractmethod
    def execute(self, **kwargs) -> Dict[str, Any]:
        pass

    def _get_model(self) -> Optional[Dict]:
        if not self.current_model:
            self.current_model = self.coordinator.get_primary_model()
        return self.current_model

    def _handle_fallback(self) -> bool:
        if not self.current_model:
            return False
        fallback = self.coordinator.get_fallback_model(self.current_model["type"])
        if fallback:
            self.current_model = fallback
            return True
        return False

class TextCompletionTool(BaseModelTool):
    def execute(self, prompt: str, **kwargs) -> Dict[str, Any]:
        model = self._get_model()
        try:
            if model["type"] == "gemini":
                response = model["model"].generate_text(prompt, **kwargs)
                return {"text": response.text, "model": "gemini"}
            elif model["type"] == "lmstudio":
                # LM Studio API call implementation
                pass
        except Exception as e:
            if self._handle_fallback():
                return self.execute(prompt, **kwargs)
            raise e

class StructuredOutputTool(BaseModelTool):
    def execute(self, prompt: str, format_schema: Dict, **kwargs) -> Dict[str, Any]:
        model = self._get_model()
        try:
            if model["type"] == "gemini":
                response = model["model"].generate_text(
                    f"{prompt}\nOutput in JSON format following schema: {format_schema}",
                    **kwargs
                )
                return {"result": response.text, "model": "gemini"}
            elif model["type"] == "lmstudio":
                # LM Studio API call implementation
                pass
        except Exception as e:
            if self._handle_fallback():
                return self.execute(prompt, format_schema, **kwargs)
            raise e
