from typing import Dict, List, Any, Optional
import json
import os
from pathlib import Path

class KnowledgeManager:
    def __init__(self, base_path: str = "./knowledge"):
        self.base_path = Path(base_path)
        self.base_path.mkdir(parents=True, exist_ok=True)
        self.cache = {}
        self._initialize_structure()

    def _initialize_structure(self):
        (self.base_path / "gemini").mkdir(exist_ok=True)
        (self.base_path / "lmstudio").mkdir(exist_ok=True)
        (self.base_path / "shared").mkdir(exist_ok=True)

    def store_knowledge(self, key: str, data: Any, model_type: Optional[str] = None):
        if model_type:
            path = self.base_path / model_type / f"{key}.json"
        else:
            path = self.base_path / "shared" / f"{key}.json"

        with open(path, "w") as f:
            json.dump(data, f, indent=2)
        self.cache[key] = data

    def get_knowledge(self, key: str, model_type: Optional[str] = None) -> Optional[Any]:
        if key in self.cache:
            return self.cache[key]

        try:
            if model_type:
                path = self.base_path / model_type / f"{key}.json"
            else:
                path = self.base_path / "shared" / f"{key}.json"

            with open(path) as f:
                data = json.load(f)
                self.cache[key] = data
                return data
        except FileNotFoundError:
            return None

    def list_knowledge(self, model_type: Optional[str] = None) -> List[str]:
        if model_type:
            path = self.base_path / model_type
        else:
            path = self.base_path / "shared"

        return [f.stem for f in path.glob("*.json")]

    def share_knowledge(self, key: str, source_model: str):
        data = self.get_knowledge(key, source_model)
        if data:
            self.store_knowledge(key, data)
