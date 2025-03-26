from pathlib import Path
import yaml
import json
from datetime import datetime
from typing import Dict, List, Any, Optional
import logging
import mlflow
import os

logger = logging.getLogger(__name__)

class KnowledgeManager:
    def __init__(self, base_path: str = "./knowledge"):
        self.base_path = Path(base_path)
        self.config = self._load_config()
        self.categories = self._load_categories()
        self.schema = self._load_schema()
        self._validate_structure()
        self._setup_mlflow()

    def _setup_mlflow(self):
        try:
            mlflow.set_tracking_uri(os.getenv("MLFLOW_TRACKING_URI"))
            mlflow.set_experiment("knowledge_search_monitoring")
        except Exception as e:
            logger.warning(f"Failed to setup MLflow tracking: {str(e)}")

    def _load_config(self) -> Dict:
        with open(self.base_path / "config.yaml") as f:
            return yaml.safe_load(f)

    def _load_categories(self) -> Dict:
        with open(self.base_path / "categories.yaml") as f:
            return yaml.safe_load(f)

    def _load_schema(self) -> Dict:
        with open(self.base_path / "schemas" / "entry.yaml") as f:
            return yaml.safe_load(f)

    def _validate_structure(self) -> None:
        required_dirs = ["schemas", "templates", "model-specific", "prompt-templates"]
        for dir_name in required_dirs:
            (self.base_path / dir_name).mkdir(exist_ok=True)

    def store_entry(self, category: str, entry_id: str, content: Dict) -> bool:
        try:
            self._validate_entry(content)
            path = self._get_entry_path(category, entry_id)
            path.parent.mkdir(parents=True, exist_ok=True)

            content["metadata"] = {
                "updated_at": datetime.now().isoformat(),
                "version": content.get("metadata", {}).get("version", "1.0.0")
            }

            with open(path, "w") as f:
                yaml.dump(content, f)
            return True
        except Exception as e:
            logger.error(f"Failed to store entry: {str(e)}")
            return False

    def get_entry(self, category: str, entry_id: str) -> Optional[Dict]:
        try:
            path = self._get_entry_path(category, entry_id)
            if not path.exists():
                return None
            with open(path) as f:
                return yaml.safe_load(f)
        except Exception as e:
            logger.error(f"Failed to get entry: {str(e)}")
            return None

    def list_entries(self, category: str) -> List[str]:
        path = self.base_path / category
        if not path.exists():
            return []
        return [f.stem for f in path.glob("*.yaml")]

    def get_category_info(self, category: str) -> Optional[Dict]:
        return self.categories.get(category)

    def _get_entry_path(self, category: str, entry_id: str) -> Path:
        return self.base_path / category / f"{entry_id}.yaml"

    def _validate_entry(self, content: Dict) -> bool:
        # Basic validation - could be expanded with JSON Schema validation
        required_fields = self.schema["required"]
        for field in required_fields:
            if field not in content:
                raise ValueError(f"Missing required field: {field}")
        return True

    def search_entries(self, query: str, categories: Optional[List[str]] = None) -> List[Dict]:
        results = []
        search_categories = categories or list(self.categories.keys())

        for category in search_categories:
            entries = self.list_entries(category)
            for entry_id in entries:
                entry = self.get_entry(category, entry_id)
                if entry and self._matches_query(entry, query):
                    results.append({
                        "category": category,
                        "id": entry_id,
                        "entry": entry
                    })
        return results

    def _matches_query(self, entry: Dict, query: str) -> bool:
        # Simple text matching - could be enhanced with better search
        query = query.lower()
        searchable_text = json.dumps(entry).lower()
        return query in searchable_text

    def update_model_capabilities(self, model_id: str, capabilities: Dict) -> bool:
        try:
            template_path = self.base_path / "templates" / "model-capabilities.yaml"
            with open(template_path) as f:
                template = yaml.safe_load(f)

            # Validate capabilities against template
            for required in template["required"]:
                if required not in capabilities:
                    raise ValueError(f"Missing required capability: {required}")

            return self.store_entry("model-specific", model_id, capabilities)
        except Exception as e:
            logger.error(f"Failed to update model capabilities: {str(e)}")
            return False

    def get_model_capabilities(self, model_id: str) -> Optional[Dict]:
        return self.get_entry("model-specific", model_id)

    def store_search_results(self, query: str, results: List[Dict], source: str) -> bool:
        try:
            with mlflow.start_run(nested=True):
                mlflow.log_params({
                    "query": query,
                    "source": source,
                    "results_count": len(results)
                })

                results_path = self.base_path / "search_results"
                results_path.mkdir(exist_ok=True)

                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                file_path = results_path / f"search_{timestamp}.json"

                search_data = {
                    "query": query,
                    "source": source,
                    "timestamp": timestamp,
                    "results": results
                }

                with open(file_path, "w") as f:
                    json.dump(search_data, f, indent=2)

                mlflow.log_metric("success", 1)
                return True

        except Exception as e:
            logger.error(f"Failed to store search results: {str(e)}")
            if mlflow.active_run():
                mlflow.log_metric("success", 0)
            return False

    def get_search_history(self,
                          source: Optional[str] = None,
                          limit: int = 10) -> List[Dict]:
        """Get recent search results with optional filtering"""
        try:
            results_path = self.base_path / "search_results"
            if not results_path.exists():
                return []

            files = sorted(
                results_path.glob("search_*.json"),
                key=lambda x: x.stat().st_mtime,
                reverse=True
            )

            history = []
            for file in files[:limit]:
                with open(file) as f:
                    data = json.load(f)
                    if not source or data.get("source") == source:
                        history.append(data)

            return history

        except Exception as e:
            logger.error(f"Failed to get search history: {str(e)}")
            return []

    def analyze_search_performance(self,
                                 source: Optional[str] = None,
                                 days: int = 7) -> Dict[str, Any]:
        """Analyze search performance metrics"""
        try:
            with mlflow.start_run(nested=True):
                history = self.get_search_history(source=source, limit=1000)

                metrics = {
                    "total_searches": len(history),
                    "avg_results_per_search": sum(
                        len(h["results"]) for h in history
                    ) / len(history) if history else 0,
                    "sources": {}
                }

                for entry in history:
                    source = entry["source"]
                    if source not in metrics["sources"]:
                        metrics["sources"][source] = {
                            "count": 0,
                            "total_results": 0
                        }
                    metrics["sources"][source]["count"] += 1
                    metrics["sources"][source]["total_results"] += len(entry["results"])

                mlflow.log_metrics({
                    "total_searches": metrics["total_searches"],
                    "avg_results": metrics["avg_results_per_search"]
                })

                return metrics

        except Exception as e:
            logger.error(f"Failed to analyze search performance: {str(e)}")
            return {}

    """
    Knowledge management module for storing and retrieving information from the knowledge base.
    """
    import os
    import json
    import logging
    from pathlib import Path
    from typing import Dict, Any, Optional

    class KnowledgeManager:
        """
        Manages storing and retrieving entries from the knowledge base.
        """

        def __init__(self, knowledge_base_path: str = None):
            """
            Initialize the KnowledgeManager with a path to the knowledge base.

            Args:
                knowledge_base_path: The path to the knowledge base directory.
                                    If None, uses the default "knowledge" directory in the project root.
            """
            self.logger = logging.getLogger(__name__)

            if knowledge_base_path is None:
                # Default path is "knowledge" in the project root
                project_root = Path(__file__).parent.parent.parent.parent
                knowledge_base_path = os.path.join(project_root, "knowledge")

            self.knowledge_base_path = knowledge_base_path
            self.entries_dir = os.path.join(self.knowledge_base_path, "entries")

            # Ensure directories exist
            self._ensure_directories()

            self.logger.info(f"Knowledge manager initialized with base path: {self.knowledge_base_path}")

        def _ensure_directories(self):
            """Ensure all required directories exist."""
            os.makedirs(self.entries_dir, exist_ok=True)

        def save_entry(self, category: str, entry_id: str, content: Dict[str, Any]) -> bool:
            """
            Save an entry to the knowledge base.

            Args:
                category: The category of the entry (e.g., "reports", "facts")
                entry_id: A unique identifier for the entry
                content: The content to save (must be JSON serializable)

            Returns:
                True if saving was successful, False otherwise
            """
            try:
                # Create category directory if it doesn't exist
                category_dir = os.path.join(self.entries_dir, category)
                os.makedirs(category_dir, exist_ok=True)

                # Create the entry file path
                file_path = os.path.join(category_dir, f"{entry_id}.json")

                # Add metadata to content
                content_with_metadata = {
                    "id": entry_id,
                    "category": category,
                    "data": content
                }

                # Write the content to the file
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(content_with_metadata, f, indent=2, ensure_ascii=False)

                self.logger.info(f"Successfully saved entry {entry_id} in category {category}")
                return True

            except Exception as e:
                self.logger.error(f"Error saving entry {entry_id} in category {category}: {e}")
                return False

        def get_entry(self, category: str, entry_id: str) -> Optional[Dict[str, Any]]:
            """
            Retrieve an entry from the knowledge base.

            Args:
                category: The category of the entry
                entry_id: The unique identifier for the entry

            Returns:
                The entry content as a dictionary, or None if not found
            """
            try:
                file_path = os.path.join(self.entries_dir, category, f"{entry_id}.json")

                if not os.path.exists(file_path):
                    self.logger.warning(f"Entry {entry_id} in category {category} not found")
                    return None

                with open(file_path, 'r', encoding='utf-8') as f:
                    content = json.load(f)

                self.logger.info(f"Successfully retrieved entry {entry_id} from category {category}")
                return content

            except Exception as e:
                self.logger.error(f"Error retrieving entry {entry_id} from category {category}: {e}")
                return None

        def list_entries(self, category: str = None) -> Dict[str, list]:
            """
            List all entries in the knowledge base, optionally filtered by category.

            Args:
                category: Optional category to filter by

            Returns:
                Dictionary mapping categories to lists of entry IDs
            """
            try:
                result = {}

                if category:
                    # List entries in the specific category
                    category_dir = os.path.join(self.entries_dir, category)
                    if os.path.exists(category_dir) and os.path.isdir(category_dir):
                        entries = [f.replace('.json', '') for f in os.listdir(category_dir)
                                  if f.endswith('.json') and os.path.isfile(os.path.join(category_dir, f))]
                        result[category] = entries
                else:
                    # List entries in all categories
                    for dir_name in os.listdir(self.entries_dir):
                        dir_path = os.path.join(self.entries_dir, dir_name)
                        if os.path.isdir(dir_path):
                            entries = [f.replace('.json', '') for f in os.listdir(dir_path)
                                      if f.endswith('.json') and os.path.isfile(os.path.join(dir_path, f))]
                            result[dir_name] = entries

                return result

            except Exception as e:
                self.logger.error(f"Error listing entries: {e}")
                return {}
