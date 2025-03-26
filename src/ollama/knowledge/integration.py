from typing import Dict, List, Optional, Any
from .manager import KnowledgeManager
import logging
from pathlib import Path
import json

logger = logging.getLogger(__name__)

class KnowledgeIntegration:
    def __init__(self, base_path: str = "./knowledge"):
        self.manager = KnowledgeManager(base_path)

    def get_model_config(self, model_id: str) -> Optional[Dict]:
        """Get model-specific configuration and capabilities"""
        capabilities = self.manager.get_model_capabilities(model_id)
        if not capabilities:
            logger.warning(f"No capabilities found for model: {model_id}")
            return None
        return self._enrich_model_config(capabilities)

    def _enrich_model_config(self, capabilities: Dict) -> Dict:
        """Enrich model config with best practices and optimization"""
        model_id = capabilities.get("model_id")

        # Get related knowledge entries
        best_practices = self.manager.search_entries(
            model_id,
            categories=["best-practices"]
        )

        # Enrich with additional context
        return {
            **capabilities,
            "context": {
                "best_practices": best_practices,
                "recommended_templates": self._get_recommended_templates(capabilities)
            }
        }

    def _get_recommended_templates(self, capabilities: Dict) -> List[str]:
        """Find templates that work well with model capabilities"""
        templates = []
        if capabilities.get("capabilities", {}).get("text_generation"):
            templates.extend(self.manager.list_entries("prompt-templates"))
        return templates

    def get_prompt_template(self, template_id: str) -> Optional[Dict]:
        """Get prompt template with enriched context"""
        template = self.manager.get_entry("prompt-templates", template_id)
        if not template:
            return None

        # Add related entries and usage examples
        related = self.manager.search_entries(
            template_id,
            categories=["prompt-templates", "best-practices"]
        )

        return {
            **template,
            "related_content": related
        }

    def validate_model_compatibility(self, template_id: str, model_id: str) -> bool:
        """Check if template is compatible with model"""
        template = self.manager.get_entry("prompt-templates", template_id)
        capabilities = self.manager.get_model_capabilities(model_id)

        if not template or not capabilities:
            return False

        # Check compatibility based on features needed
        model_features = capabilities.get("capabilities", {})
        required_features = template.get("required_capabilities", [])

        return all(
            model_features.get(feature, False)
            for feature in required_features
        )

    def get_domain_knowledge(self, domain: str) -> List[Dict]:
        """Get domain-specific knowledge entries"""
        return self.manager.search_entries(
            domain,
            categories=["domain-knowledge"]
        )

    def update_model_performance(self, model_id: str, metrics: Dict) -> bool:
        """Update model performance metrics"""
        capabilities = self.manager.get_model_capabilities(model_id)
        if not capabilities:
            return False

        capabilities["performance_metrics"].update(metrics)
        return self.manager.update_model_capabilities(model_id, capabilities)

    def get_optimization_tips(self, model_id: str) -> List[str]:
        """Get model-specific optimization tips"""
        capabilities = self.manager.get_model_capabilities(model_id)
        if not capabilities:
            return []

        return capabilities.get("optimization_tips", [])

    def get_latest_index_file(self, index_files: List[Path]) -> Dict:
        """Get the latest index file based on modification time"""
        latest = max(index_files, key=lambda x: x.stat().st_mtime)
        with open(latest) as f:
            return json.load(f)
