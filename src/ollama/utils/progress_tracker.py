import mlflow
from typing import Dict, Any
import time
from datetime import datetime

class ProgressTracker:
    def __init__(self, model_type: str):
        self.model_type = model_type
        self.start_time = None
        self.metrics = {}

    def start_run(self):
        experiment = f"{self.model_type}_crew_monitoring"
        mlflow.set_experiment(experiment)
        self.start_time = time.time()
        return mlflow.start_run()

    def log_metric(self, key: str, value: float, step: int = None):
        self.metrics[key] = value
        mlflow.log_metric(key, value, step=step)

    def log_execution(self, task_name: str, success: bool, **metrics):
        execution_time = time.time() - self.start_time

        self.log_metric("execution_time", execution_time)
        self.log_metric("success", int(success))

        for key, value in metrics.items():
            if isinstance(value, (int, float)):
                self.log_metric(key, value)

        mlflow.log_params({
            "task": task_name,
            "model_type": self.model_type,
            "timestamp": datetime.now().isoformat()
        })

    def get_summary(self) -> Dict[str, Any]:
        return {
            "model_type": self.model_type,
            "execution_time": self.metrics.get("execution_time", 0),
            "success_rate": self.metrics.get("success", 0),
            "metrics": self.metrics
        }
