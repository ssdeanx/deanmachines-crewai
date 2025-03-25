from typing import Dict, Any, Optional
import xml.etree.ElementTree as ET
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

class TemplateLoader:
    def __init__(self, template_dir: str = "../templates"):
        self.template_dir = Path(template_dir)
        self.cache = {}

    def load_templates(self, template_type: str) -> Dict[str, Any]:
        """Load templates by type (code or multimodal)"""
        try:
            if template_type == "code":
                template_path = self.template_dir / "code_templates.xml"
            elif template_type == "multimodal":
                template_path = self.template_dir / "multimodal_templates.xml"
            else:
                raise ValueError(f"Unsupported template type: {template_type}")

            if template_path in self.cache:
                return self.cache[template_path]

            tree = ET.parse(template_path)
            root = tree.getroot()

            templates = {}
            for template in root:
                templates[template.tag] = self._parse_template_section(template)

            self.cache[template_path] = templates
            return templates

        except Exception as e:
            logger.error(f"Failed to load {template_type} templates: {str(e)}")
            return {}

    def _parse_template_section(self, element: ET.Element) -> Dict:
        """Parse XML template section"""
        result = {}

        for child in element:
            if child.tag == "template":
                # Extract CDATA content
                if "![CDATA[" in child.text:
                    result["template"] = child.text.split("![CDATA[")[1].split("]]")[0].strip()
                else:
                    result["template"] = child.text.strip()
            elif len(child) > 0:
                result[child.tag] = self._parse_template_section(child)
            else:
                result[child.tag] = child.text.strip() if child.text else ""

        return result

    def get_template(self, template_type: str, category: str, section: Optional[str] = None) -> Optional[Dict]:
        """Get specific template by type, category and section"""
        templates = self.load_templates(template_type)

        if category not in templates:
            return None

        if section and section in templates[category]:
            return templates[category][section]

        return templates[category]

    def validate_parameters(self, template_type: str, category: str, parameters: Dict) -> bool:
        """Validate parameters against template requirements"""
        template = self.get_template(template_type, category)
        if not template or "parameters" not in template:
            return False

        required_params = template["parameters"]
        return all(param in parameters for param in required_params)
