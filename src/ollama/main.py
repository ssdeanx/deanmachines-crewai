#!/usr/bin/env python
import json
import sys
import warnings
import os
import dotenv
import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional
import time
from functools import wraps

from src import ollama
from src.ollama.crew import OllamaCrew

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

    def run(self, custom_inputs: Optional[Dict] = None) -> Dict:
        """Run the crew with structured thinking patterns"""
        try:
            self.initialize_crew(custom_inputs)
            logger.info("Starting crew execution")
            result = self.crew.run()
            
            # Save execution metadata
            self._save_execution_metadata(result)
            
            return result
        except Exception as e:
            logger.error(f"Error during crew execution: {str(e)}")
            raise

    def train(self, n_iterations: int, filename: str, custom_inputs: Optional[Dict] = None) -> Dict:
        """Train the crew with specific iterations"""
        try:
            self.initialize_crew(custom_inputs)
            logger.info(f"Starting crew training for {n_iterations} iterations")
            
            results = []
            for i in range(n_iterations):
                logger.info(f"Training iteration {i+1}/{n_iterations}")
                result = self.crew.run()
                results.append(result)
                
            # Save training results
            self._save_training_results(results, filename)
            
            return {"iterations": n_iterations, "results": results}
        except Exception as e:
            logger.error(f"Error during training: {str(e)}")
            raise

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
    import argparse
    parser = argparse.ArgumentParser(description="Run the Structured Thinking Crew")
    parser.add_argument("--topic", default="Prompt Engineering", help="Topic to focus on")
    parser.add_argument("--output-dir", default="./outputs", help="Output directory")
    parser.add_argument("--mode", choices=["run", "train", "test"], default="run", help="Operation mode")
    parser.add_argument("--analysis-depth", default="detailed", choices=["basic", "detailed", "comprehensive"])
    parser.add_argument("--branch-depth", type=int, default=3, help="Depth of branching analysis")
    parser.add_argument("--validation-level", default="normal", choices=["strict", "normal", "relaxed"])
    
    args = parser.parse_args()

    runner = OllamaRunner(
        topic=args.topic,
        output_dir=args.output_dir,
        analysis_depth=args.analysis_depth,
        branch_depth=args.branch_depth,
        validation_level=args.validation_level
    )
    
    try:
        if args.mode == "run":
            result = runner.run()
        elif args.mode == "train":
            result = runner.train(n_iterations=3, filename="training_results.json")
        elif args.mode == "test":
            result = runner.test(n_iterations=3, model_name="gemma")
        
        logger.info(f"Execution completed successfully in {args.mode} mode!")
        print(result)
    except Exception as e:
        logger.error(f"Execution failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
