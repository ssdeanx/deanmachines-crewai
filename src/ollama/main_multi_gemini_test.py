"""
Main entry point for the Gemini multi-agent test harness.
Validates Gemini API connectivity, CrewAI sequential task execution, and MLflow PostgreSQL logging.
"""
import os
import logging
import mlflow
import sys
from dotenv import load_dotenv
from src.ollama.multi_gemini_crew import GeminiMultiCrew

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

# MLflow setup
def setup_mlflow():
    """
    Set up MLflow tracking with PostgreSQL backend.

    Returns:
        bool: True if setup was successful, False otherwise
    """
    tracking_uri = os.getenv("MLFLOW_TRACKING_URI")
    if not tracking_uri:
        logger.error("MLFLOW_TRACKING_URI environment variable not set. Must point to a PostgreSQL database.")
        return False

    try:
        mlflow.set_tracking_uri(tracking_uri)
        logger.info(f"MLflow tracking URI set to: {tracking_uri}")

        # Create or get the experiment
        experiment_name = "Simple_Gemini_Test"
        mlflow.set_experiment(experiment_name)
        logger.info(f"MLflow experiment set to: {experiment_name}")
        return True
    except Exception as e:
        logger.error(f"Failed to set up MLflow: {e}")
        return False

def main():
    """
    Main execution function for the Gemini multi-agent test.
    """
    # Topic to analyze
    topic = "climate change impacts on agriculture"

    # Set up MLflow
    if not setup_mlflow():
        logger.error("Exiting due to MLflow setup failure")
        return

    logger.info("Starting Gemini Multi-Agent Test")

    run_active = False
    try:
        # Instantiate the crew
        crew = GeminiMultiCrew(topic=topic)

        # Start MLflow run
        mlflow.start_run()
        run_active = True

        # Log parameters
        mlflow.log_param("topic", topic)
        mlflow.log_param("model_provider", "Gemini")
        mlflow.log_param("crew_type", "multi-agent-simple")

        # Execute the crew
        logger.info("Executing GeminiMultiCrew...")
        result = crew.run()

        # Log success metric and result snippet
        mlflow.log_metric("success", 1.0)
        result_snippet = result[:500] + "..." if len(result) > 500 else result
        mlflow.log_text(result_snippet, "final_result_snippet.txt")

        logger.info("Gemini Multi-Agent Test completed successfully")
        logger.info(f"Result snippet: {result_snippet}")

        return result

    except Exception as e:
        logger.error(f"Error during Gemini Multi-Agent Test: {e}")
        if run_active:
            mlflow.log_metric("success", 0.0)
            mlflow.set_tag("error", str(e))
        return None

    finally:
        if run_active:
            mlflow.end_run()
            logger.info("MLflow run ended")

if __name__ == "__main__":
    main()
