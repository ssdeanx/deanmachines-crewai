from typing import Dict, List, Any
import mlflow
from datetime import datetime, timedelta
import pandas as pd

class ModelAnalyzer:
    def __init__(self):
        self.experiments = {
            "gemini": "gemini_crew_monitoring",
            "lmstudio": "lmstudio_crew_monitoring",
            "ollama": "ollama_crew_monitoring"
        }

    def get_model_metrics(self, model_type: str, days: int = 7) -> Dict[str, Any]:
        experiment = mlflow.get_experiment_by_name(self.experiments[model_type])
        if not experiment:
            return {}

        runs = mlflow.search_runs(
            experiment_ids=[experiment.experiment_id],
            filter_string=f"attributes.start_time > {int((datetime.now() - timedelta(days=days)).timestamp() * 1000)}"
        )

        if len(runs) == 0:
            return {}

        metrics = {
            "success_rate": runs["metrics.success"].mean(),
            "avg_execution_time": runs["metrics.execution_time"].mean(),
            "total_runs": len(runs),
            "failed_runs": len(runs[runs["metrics.success"] == 0])
        }

        return metrics

    def compare_models(self, days: int = 7) -> Dict[str, Dict]:
        results = {}
        for model_type in self.experiments.keys():
            metrics = self.get_model_metrics(model_type, days)
            if metrics:
                results[model_type] = metrics

        return results

    def get_performance_trends(self, model_type: str, metric: str, days: int = 7) -> List[Dict]:
        experiment = mlflow.get_experiment_by_name(self.experiments[model_type])
        if not experiment:
            return []

        runs = mlflow.search_runs(
            experiment_ids=[experiment.experiment_id],
            filter_string=f"attributes.start_time > {int((datetime.now() - timedelta(days=days)).timestamp() * 1000)}"
        )

        if len(runs) == 0:
            return []

        df = pd.DataFrame({
            "timestamp": pd.to_datetime(runs["start_time"], unit="ms"),
            "value": runs[f"metrics.{metric}"]
        })

        df = df.sort_values("timestamp")
        return df.to_dict("records")
