import json
import logging
import os
import sys
import yaml
import psutil
import platform
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Union

import mlflow
import mlflow.sklearn
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

logger = logging.getLogger(__name__)

class MLflowDashboard:
    """MLflow dashboard for monitoring and tracking Ollama Crew performance."""
    
    def __init__(
        self,
        experiment_name: str = "ollama_crew_monitoring",
        tracking_uri: str = "sqlite:///mlflow.db",
        artifacts_path: str = "./mlflow-artifacts",
        config_path: Optional[str] = None
    ) -> None:
        """Initialize MLflow dashboard with configuration."""
        self.experiment_name = experiment_name
        self.tracking_uri = tracking_uri
        self.artifacts_path = Path(artifacts_path)
        self.artifacts_path.mkdir(parents=True, exist_ok=True)
        
        self.config = self._load_config(config_path)
        self._initialize_mlflow()
        
        self.current_metrics: Dict[str, float] = {}
        self.historical_metrics: List[Dict] = []
        self.current_visualizations: Dict[str, go.Figure] = {}

    def _load_config(self, config_path: Optional[str]) -> Dict:
        """Load dashboard configuration"""
        if config_path and Path(config_path).exists():
            with open(config_path) as f:
                return yaml.safe_load(f)
        return self._get_default_config()

    def _get_default_config(self) -> Dict:
        """Get default configuration"""
        return {
            "metrics": {
                "validation": {
                    "score_threshold": 0.8,
                    "error_threshold": 5
                },
                "performance": {
                    "execution_time_threshold": 30.0,
                    "memory_threshold": 1000
                }
            },
            "visualization": {
                "theme": "plotly_dark",
                "refresh_interval": 60
            }
        }

    def _initialize_mlflow(self) -> None:
        """Initialize MLflow experiment"""
        try:
            mlflow.set_tracking_uri(self.tracking_uri)
            self.experiment = mlflow.get_experiment_by_name(self.experiment_name)
            
            if not self.experiment:
                self.experiment_id = mlflow.create_experiment(
                    self.experiment_name,
                    artifact_location=str(self.artifacts_path)
                )
            else:
                self.experiment_id = self.experiment.experiment_id
                
        except Exception as e:
            logger.error(f"Error initializing MLflow: {str(e)}")
            raise

    def start_run(
        self,
        run_name: Optional[str] = None,
        tags: Optional[Dict] = None,
        nested: bool = False
    ) -> None:
        """Start a new MLflow run with enhanced tracking"""
        try:
            run_name = run_name or f"run_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            
            # Add system info to tags
            system_tags = {
                "python_version": sys.version,
                "platform": platform.platform(),
                "memory_total": psutil.virtual_memory().total,
                "cpu_count": os.cpu_count()
            }
            
            if tags:
                system_tags.update(tags)
            
            self.current_run = mlflow.start_run(
                experiment_id=self.experiment_id,
                run_name=run_name,
                tags=system_tags,
                nested=nested
            )
            
            # Initialize run metrics
            self.current_metrics = {}
            
        except Exception as e:
            logger.error(f"Error starting MLflow run: {str(e)}")
            raise

    def log_metrics(self, metrics: Dict[str, float], step: Optional[int] = None) -> None:
        """Log metrics with validation and alerting"""
        try:
            # Update current metrics
            self.current_metrics.update(metrics)
            
            # Log to MLflow
            mlflow.log_metrics(metrics, step=step)
            
            # Check thresholds and send alerts
            self._check_metric_thresholds(metrics)
            
            # Store for historical tracking
            self.historical_metrics.append({
                "timestamp": datetime.now().isoformat(),
                "metrics": metrics.copy()
            })
            
        except Exception as e:
            logger.error(f"Error logging metrics: {str(e)}")

    def _check_metric_thresholds(self, metrics: Dict[str, float]) -> None:
        """Check metrics against thresholds and trigger alerts"""
        for metric_name, value in metrics.items():
            if metric_name in self.config["metrics"]["validation"]:
                threshold = self.config["metrics"]["validation"][f"{metric_name}_threshold"]
                if value < threshold:
                    self._trigger_alert(
                        f"Validation metric {metric_name} below threshold: {value} < {threshold}"
                    )
            elif metric_name in self.config["metrics"]["performance"]:
                threshold = self.config["metrics"]["performance"][f"{metric_name}_threshold"]
                if value > threshold:
                    self._trigger_alert(
                        f"Performance metric {metric_name} above threshold: {value} > {threshold}"
                    )

    def _trigger_alert(self, message: str, level: str = "WARNING") -> None:
        """Trigger alerts based on configuration"""
        logger.warning(message)
        if self.config["alerts"]["enabled"]:
            for channel in self.config["alerts"]["channels"]:
                if channel["type"] == "email" and channel["on_warning"]:
                    self._send_email_alert(message)

    def create_performance_visualizations(self) -> None:
        """Generate comprehensive performance visualizations"""
        try:
            if not self.historical_metrics:
                logger.warning("No metrics available for visualization")
                return
            
            # Create main dashboard
            dashboard = self._create_dashboard()
            
            # Create individual metric plots
            self._create_metric_plots()
            
            # Save visualizations
            self._save_visualizations()
            
        except Exception as e:
            logger.error(f"Error creating visualizations: {str(e)}")

    def _create_dashboard(self) -> go.Figure:
        """Create main performance dashboard"""
        df = pd.DataFrame([
            {
                "timestamp": m["timestamp"],
                **m["metrics"]
            } for m in self.historical_metrics
        ])
        
        fig = make_subplots(
            rows=3, cols=2,
            subplot_titles=(
                "Execution Time", "Memory Usage",
                "Success Rate", "Validation Score",
                "Error Count", "Complexity Score"
            )
        )
        
        # Add traces for each metric
        metrics_config = [
            ("execution_time", 1, 1),
            ("memory_usage_mb", 1, 2),
            ("success_rate", 2, 1),
            ("validation_score", 2, 2),
            ("error_count", 3, 1),
            ("complexity_score", 3, 2)
        ]
        
        for metric, row, col in metrics_config:
            if metric in df.columns:
                fig.add_trace(
                    go.Scatter(
                        x=df["timestamp"],
                        y=df[metric],
                        name=metric,
                        mode='lines+markers'
                    ),
                    row=row, col=col
                )
        
        fig.update_layout(
            height=1000,
            title_text="Performance Dashboard",
            showlegend=True,
            template=self.config["visualization"]["theme"]
        )
        
        return fig

    def end_run(self, status: str = "FINISHED") -> None:
        """End the current MLflow run with final metrics and visualizations"""
        try:
            # Create final visualizations
            self.create_performance_visualizations()
            
            # Calculate and log final metrics
            final_metrics = self._calculate_final_metrics()
            self.log_metrics(final_metrics)
            
            # End the run
            mlflow.end_run(status=status)
            
        except Exception as e:
            logger.error(f"Error ending MLflow run: {str(e)}")
            mlflow.end_run(status="FAILED")

    def _calculate_final_metrics(self) -> Dict[str, float]:
        """Calculate final aggregate metrics"""
        metrics_df = pd.DataFrame([m["metrics"] for m in self.historical_metrics])
        
        return {
            "final_success_rate": metrics_df["success_rate"].mean(),
            "avg_execution_time": metrics_df["execution_time"].mean(),
            "max_memory_usage": metrics_df["memory_usage_mb"].max(),
            "avg_validation_score": metrics_df["validation_score"].mean() if "validation_score" in metrics_df else 0.0,
            "total_errors": metrics_df["error_count"].sum() if "error_count" in metrics_df else 0
        }

    def _save_visualizations(self) -> None:
        """Save all visualizations as artifacts"""
        try:
            for fig_name, fig in self.current_visualizations.items():
                path = self.artifacts_path / f"{fig_name}.html"
                fig.write_html(str(path))
                mlflow.log_artifact(str(path))
        except Exception as e:
            logger.error(f"Error saving visualizations: {str(e)}")