# src/main/utils/mlflow_manager.py
import os
import re
import yaml
import mlflow
from typing import Dict, Any

class MLflowManager:
    """MLflow manager utility for CrewAI agents."""

    def __init__(self, config_path: str = "src/main/config/mlflow.yaml"):
        """Initialize MLflow manager with configuration."""
        self.config = self._load_config(config_path)
        self._initialize_mlflow()

    def _load_config(self, config_path: str) -> Dict[str, Any]:
        """Load configuration with environment variable substitution."""
        with open(config_path, 'r') as file:
            # Load the raw YAML content
            content = file.read()

            # Replace environment variables (format: ${ENV_VAR})
            def replace_env_var(match):
                env_var = match.group(1)
                return os.environ.get(env_var, '')

            processed_content = re.sub(r'\${([^}]+)}', replace_env_var, content)

            # Parse the processed YAML
            return yaml.safe_load(processed_content)

    def _initialize_mlflow(self):
        """Initialize MLflow with configuration settings."""
        server_config = self.config.get('server', {})
        tracking_config = self.config.get('tracking', {})

        # Set tracking URI
        host = server_config.get('host', '127.0.0.1')
        port = server_config.get('port', 5000)
        mlflow.set_tracking_uri(f"http://{host}:{port}")

        # Set experiment
        experiment_name = tracking_config.get('experiment_name', 'ai_agents')
        mlflow.set_experiment(experiment_name)

    def start_run(self, run_id: str = None, run_name: str = None):
        """Start MLflow run with optional name."""
        prefix = self.config.get('tracking', {}).get('run_name_prefix', 'workflow_')
        if run_name:
            run_name = f"{prefix}{run_name}"
        return mlflow.start_run(run_id=run_id, run_name=run_name)

    def log_task_metrics(self, task_id: str, metrics: Dict[str, float]):
        """Log task-specific metrics."""
        for name, value in metrics.items():
            mlflow.log_metric(f"task.{task_id}.{name}", value)

    def log_workflow_metrics(self, metrics: Dict[str, float]):
        """Log workflow-level metrics."""
        for name, value in metrics.items():
            mlflow.log_metric(f"workflow.{name}", value)

    def log_agent_metrics(self, agent_id: str, metrics: Dict[str, float]):
        """Log agent-specific metrics."""
        for name, value in metrics.items():
            mlflow.log_metric(f"agent.{agent_id}.{name}", value)

    def end_run(self):
        """End current MLflow run."""
        mlflow.end_run()

    def log_param(self, key: str, value: Any):
        """Log a single parameter."""
        mlflow.log_param(key, value)

    def log_artifact(self, local_path: str):
        """Log a local file or directory as an artifact."""
        mlflow.log_artifact(local_path)
