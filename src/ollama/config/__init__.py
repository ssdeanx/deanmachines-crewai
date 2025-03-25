import yaml
from pathlib import Path
from typing import Dict

def load_model_config() -> Dict:
    config_path = Path(__file__).parent / "models.yaml"
    if not config_path.exists():
        return {}
    with open(config_path) as f:
        return yaml.safe_load(f)

def load_mlflow_config() -> Dict:
    config_path = Path(__file__).parent / "mlflow_config.yaml"
    if not config_path.exists():
        return {}
    with open(config_path) as f:
        return yaml.safe_load(f)
