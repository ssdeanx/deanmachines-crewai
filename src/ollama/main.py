#!/usr/bin/env python
import argparse
import json
import sys
import warnings
import os
import psutil  # Add missing import for memory monitoring
import dotenv
import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Union
from concurrent.futures import ThreadPoolExecutor  # Add for parallel processing
import time
from functools import wraps
from src.ollama.monitoring.mlflow_dashboard import MLflowDashboard
import yaml

from src import ollama
from src.ollama.crew import OllamaCrew
from src.ollama.tools.custom_tool import ValidationLevel  # Add for validation

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('ollama.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

# Ignore specific warnings
warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# Load environment variables
dotenv.load_dotenv()

class PerformanceMonitor:
    """Monitor and optimize system performance"""
    def __init__(self):
        self.metrics = {
            "execution_times": [],
            "success_rates": [],
            "error_rates": [],
            "validation_scores": []
        }
        
    def track_execution(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            try:
                result = func(*args, **kwargs)
                self.metrics["success_rates"].append(1)
                return result
            except Exception as e:
                self.metrics["error_rates"].append(1)
                raise
            finally:
                execution_time = time.time() - start_time
                self.metrics["execution_times"].append(execution_time)
        return wrapper

class OllamaRunner:
    def __init__(
        self,
        topic: str = "AI LLMs",
        output_dir: str = "./outputs",
        analysis_depth: str = "detailed",
        branch_depth: int = 3,
        validation_level: str = "normal"
    ):
        self.topic = topic
        self.output_dir = Path(output_dir)
        self.analysis_depth = analysis_depth
        self.branch_depth = branch_depth
        self.validation_level = validation_level
        self.crew = None
        self.setup_environment()
        
        # Initialize MLflow dashboard
        with open(Path(__file__).parent / "config" / "mlflow_config.yaml", "r") as f:
            mlflow_config = yaml.safe_load(f)
        
        self.dashboard = MLflowDashboard(
            experiment_name=mlflow_config["dashboard"]["experiment_name"],
            tracking_uri=mlflow_config["dashboard"]["tracking_uri"],
            artifacts_path=mlflow_config["dashboard"]["artifacts_path"]
        )

    def setup_environment(self) -> None:
        """Setup necessary directories and configurations"""
        self.output_dir.mkdir(parents=True, exist_ok=True)
        logger.info(f"Initialized OllamaRunner with topic: {self.topic}")

    def get_default_inputs(self) -> Dict:
        """Get default input parameters"""
        return {
            "topic": self.topic,
            "current_year": str(datetime.now().year),
            "analysis_depth": self.analysis_depth,
            "branch_depth": self.branch_depth,
            "validation_level": self.validation_level
        }

    def initialize_crew(self, custom_inputs: Optional[Dict] = None) -> None:
        """Initialize the crew with inputs"""
        inputs = self.get_default_inputs()
        if custom_inputs:
            inputs.update(custom_inputs)
        
        self.crew = OllamaCrew(
            topic=inputs["topic"],
            output_dir=str(self.output_dir),
            analysis_depth=inputs["analysis_depth"],
            branch_depth=inputs["branch_depth"]
        )
        logger.info("Crew initialized successfully")

    def validate_configuration(self) -> bool:
        """Validate runner configuration"""
        try:
            assert self.analysis_depth in ["basic", "detailed", "comprehensive"], "Invalid analysis depth"
            assert self.branch_depth > 0, "Branch depth must be positive"
            assert self.validation_level in ["strict", "normal", "relaxed"], "Invalid validation level"
            assert self.output_dir.exists(), "Output directory does not exist"
            return True
        except AssertionError as e:
            logger.error(f"Configuration validation failed: {str(e)}")
            return False

    @PerformanceMonitor().track_execution
    def run(self, custom_inputs: Optional[Dict] = None) -> Dict:
        """Run the crew with structured thinking patterns and performance monitoring"""
        try:
            if not self.validate_configuration():
                raise ValueError("Invalid configuration")

            self.dashboard.start_run(
                run_name=f"analysis_{self.topic.lower().replace(' ', '_')}",
                tags={"topic": self.topic, "depth": self.analysis_depth}
            )
            
            self.initialize_crew(custom_inputs)
            logger.info("Starting crew execution")
            
            start_time = time.time()
            result = self.crew.run()
            execution_time = time.time() - start_time
            
            # Log enhanced metrics
            self.dashboard.log_performance_data(
                execution_time=execution_time,
                memory_usage=psutil.Process().memory_info().rss / (1024 * 1024),
                success_rate=1.0 if result.get("status") != "failed" else 0.0,
                complexity_score=result.get("complexity_score", 0.0)
            )
            
            if "validation" in result:
                self.dashboard.log_validation_results(result["validation"])
            
            self._save_execution_metadata(result)
            self.dashboard.end_run()
            
            return {
                **result,
                "execution_metrics": {
                    "time": execution_time,
                    "memory_usage_mb": psutil.Process().memory_info().rss / (1024 * 1024),
                    "validation_level": self.validation_level
                }
            }
            
        except Exception as e:
            logger.error(f"Error during crew execution: {str(e)}")
            if hasattr(self, 'dashboard'):
                self.dashboard.log_metrics({"error_count": 1})
                self.dashboard.end_run()
            raise

    def train(self, n_iterations: int, filename: str, custom_inputs: Optional[Dict] = None, max_workers: int = 3) -> Dict:
        """Train the crew with parallel iterations"""
        try:
            self.initialize_crew(custom_inputs)
            logger.info(f"Starting crew training for {n_iterations} iterations")
            
            results = []
            with ThreadPoolExecutor(max_workers=max_workers) as executor:
                future_to_iteration = {
                    executor.submit(self._run_training_iteration, i): i 
                    for i in range(n_iterations)
                }
                
                for future in future_to_iteration:
                    try:
                        result = future.result()
                        results.append(result)
                        logger.info(f"Completed iteration {future_to_iteration[future]+1}/{n_iterations}")
                    except Exception as e:
                        logger.error(f"Error in iteration {future_to_iteration[future]+1}: {str(e)}")
            
            # Save and analyze results
            self._save_training_results(results, filename)
            analysis = self._analyze_training_results(results)
            
            return {
                "iterations": n_iterations,
                "results": results,
                "analysis": analysis
            }
        except Exception as e:
            logger.error(f"Error during training: {str(e)}")
            raise

    def _run_training_iteration(self, iteration: int) -> Dict:
        """Run a single training iteration"""
        try:
            result = self.crew.run()
            return {
                "iteration": iteration,
                "result": result,
                "timestamp": datetime.now().isoformat(),
                "metrics": {
                    "memory_usage": psutil.Process().memory_info().rss / (1024 * 1024),
                    "success": result.get("status") != "failed"
                }
            }
        except Exception as e:
            logger.error(f"Training iteration {iteration} failed: {str(e)}")
            return {
                "iteration": iteration,
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            }

    def _analyze_training_results(self, results: List[Dict]) -> Dict:
        """Analyze training results"""
        successful = [r for r in results if r.get("metrics", {}).get("success", False)]
        return {
            "success_rate": len(successful) / len(results) if results else 0,
            "average_memory": sum(r.get("metrics", {}).get("memory_usage", 0) for r in results) / len(results if results else 0),
            "completion_time": (datetime.now() - self.start_time).total_seconds() if hasattr(self, 'start_time') else 0
        }

    def test(
        self,
        n_iterations: int,
        model_name: str,
        custom_inputs: Optional[Dict] = None
    ) -> Dict:
        """Test crew performance"""
        try:
            self.initialize_crew(custom_inputs)
            logger.info(f"Starting crew testing with {model_name}")
            
            test_results = {
                "model": model_name,
                "iterations": n_iterations,
                "results": [],
                "metrics": {
                    "success_rate": 0.0,
                    "average_score": 0.0,
                    "validation_stats": {}
                }
            }
            
            for i in range(n_iterations):
                logger.info(f"Test iteration {i+1}/{n_iterations}")
                result = self.crew.run()
                test_results["results"].append(result)
            
            self._calculate_test_metrics(test_results)
            self._save_test_results(test_results)
            
            return test_results
        except Exception as e:
            logger.error(f"Error during testing: {str(e)}")
            raise

    def _save_execution_metadata(self, result: Dict) -> None:
        """Save execution metadata"""
        metadata_path = self.output_dir / "execution_metadata.json"
        metadata = {
            "timestamp": datetime.now().isoformat(),
            "topic": self.topic,
            "analysis_depth": self.analysis_depth,
            "branch_depth": self.branch_depth,
            "validation_level": self.validation_level,
            "result_summary": result.get("summary", {})
        }
        with open(metadata_path, 'w') as f:
            json.dump(metadata, f, indent=2)

    def _save_training_results(self, results: List[Dict], filename: str) -> None:
        """Save training results"""
        training_path = self.output_dir / filename
        with open(training_path, 'w') as f:
            json.dump(results, f, indent=2)

    def _save_test_results(self, results: Dict) -> None:
        """Save test results"""
        test_path = self.output_dir / f"test_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(test_path, 'w') as f:
            json.dump(results, f, indent=2)

    def _calculate_test_metrics(self, test_results: Dict) -> None:
        """Calculate test metrics"""
        successful = sum(1 for r in test_results["results"] if r.get("valid", False))
        test_results["metrics"]["success_rate"] = successful / len(test_results["results"])
        test_results["metrics"]["average_score"] = sum(
            r.get("score", 0) for r in test_results["results"]
        ) / len(test_results["results"])

def main():
    try:
        parser = argparse.ArgumentParser(description="Run the Structured Thinking Crew")
        parser.add_argument("--topic", default="Prompt Engineering", help="Topic to focus on")
        parser.add_argument("--output-dir", default="./outputs", help="Output directory")
        parser.add_argument("--mode", choices=["run", "train", "test"], default="run", help="Operation mode")
        parser.add_argument("--analysis-depth", default="detailed", choices=["basic", "detailed", "comprehensive"])
        parser.add_argument("--branch-depth", type=int, default=3, help="Depth of branching analysis")
        parser.add_argument("--validation-level", default="normal", choices=["strict", "normal", "relaxed"])
        parser.add_argument("--parallel", action="store_true", help="Enable parallel processing")
        parser.add_argument("--max-workers", type=int, default=3, help="Maximum number of parallel workers")
        
        args = parser.parse_args()

        # Validate output directory
        output_dir = Path(args.output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        # Initialize logging
        setup_logging(output_dir)

        runner = OllamaRunner(
            topic=args.topic,
            output_dir=str(output_dir),
            analysis_depth=args.analysis_depth,
            branch_depth=args.branch_depth,
            validation_level=args.validation_level
        )
        
        if not runner.validate_configuration():
            raise ValueError("Invalid configuration")

        result = None
        if args.mode == "run":
            result = runner.run()
        elif args.mode == "train":
            result = runner.train(
                n_iterations=3, 
                filename="training_results.json",
                max_workers=args.max_workers if args.parallel else 1
            )
        elif args.mode == "test":
            result = runner.test(n_iterations=3, model_name="gemma")
        
        logger.info(f"Execution completed successfully in {args.mode} mode!")
        
        # Save final results
        results_file = output_dir / f"results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(results_file, 'w') as f:
            json.dump(result, f, indent=2)
        
        print(json.dumps(result, indent=2))
        return 0
        
    except Exception as e:
        logger.error(f"Execution failed: {str(e)}", exc_info=True)
        return 1

def setup_logging(output_dir: Path) -> None:
    """Setup logging configuration"""
    log_file = output_dir / f"ollama_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler(sys.stdout)
        ]
    )

if __name__ == "__main__":
    sys.exit(main())
