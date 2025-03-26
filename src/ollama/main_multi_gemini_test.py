"""
Main entry point for the Gemini multi-agent test harness.
Validates Gemini API connectivity, CrewAI sequential task execution, and MLflow PostgreSQL logging.
"""
import os
import logging
import mlflow
from typing import Optional
from pathlib import Path
from dotenv import load_dotenv
from src.ollama.multi_gemini_crew import GeminiMultiCrew

# Initialize logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

def setup_mlflow() -> bool:
    """
    Set up MLflow tracking with PostgreSQL backend.

    Returns:
        bool: True if setup was successful, False otherwise

    Notes:
        Expects MLFLOW_TRACKING_URI environment variable to point
        to a valid PostgreSQL connection string:
        postgresql://user:pass@host:port/db
    """
    tracking_uri = os.getenv("MLFLOW_TRACKING_URI")
    if not tracking_uri:
        logger.error("MLFLOW_TRACKING_URI environment variable not set")
        logger.error("Must point to a PostgreSQL database, e.g.: postgresql://user:pass@host:port/db")
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

def save_result_snippet(result: str, max_length: int = 500) -> str:
    """
    Save a snippet of the result, truncating if necessary.

    Args:
        result: The full result text
        max_length: Maximum length of the snippet

    Returns:
        The snippet text
    """
    try:
        snippet = result[:max_length] + "..." if len(result) > max_length else result
        mlflow.log_text(snippet, "final_result_snippet.txt")
        logger.info("Successfully saved result snippet to MLflow")
        return snippet
    except Exception as e:
        logger.error(f"Failed to save result snippet: {e}")
        return ""

def save_full_report(result: str) -> bool:
    """
    Save the full result text to a local file and log it with MLflow.

    Args:
        result: The complete result text from the crew execution

    Returns:
        bool: True if saving was successful, False otherwise
    """
    try:
        # Create reports directory if it doesn't exist
        reports_dir = Path("reports")
        reports_dir.mkdir(exist_ok=True)

        # Generate timestamped filename
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"gemini_report_{timestamp}.txt"
        file_path = reports_dir / filename

        # Save locally
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(result)

        # Log with MLflow
        mlflow.log_artifact(str(file_path), "reports")

        logger.info(f"Full report saved to: {file_path} and logged to MLflow")
        return True
    except Exception as e:
        logger.error(f"Failed to save full report: {e}")
        return False

def main() -> Optional[str]:
    """
    Main execution function for the Gemini multi-agent test.

    Returns:
        The final result text if successful, None if an error occurred
    """
    # Load environment variables
    load_dotenv()

    # Topic to analyze
    topic = "climate change impacts on agriculture"

    # Set up MLflow
    if not setup_mlflow():
        logger.error("Exiting due to MLflow setup failure")
        return None

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
        mlflow.log_param("report_saved", "true")

        # Execute the crew
        logger.info("Executing GeminiMultiCrew...")
        result = crew.run()

        # Log success metric and result snippet
        mlflow.log_metric("success", 1.0)
        result_snippet = save_result_snippet(result)

        # Save full report
        save_full_report(result)

        logger.info("Gemini Multi-Agent Test completed successfully")
        if result_snippet:
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
