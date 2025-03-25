from typing import Dict, Any, List, Optional
import google.generativeai as genai
from PIL import Image
import os
import base64
from io import BytesIO
import logging
from ..utils.retry_utils import retry_with_backoff

logger = logging.getLogger(__name__)

class CodeExecutor:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY environment variable is required")
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(os.getenv("GEMINI_MODEL", "models/gemini-2.0-flash"))

    @retry_with_backoff(retries=3)
    def execute_code(self, code: str, context: Optional[Dict] = None) -> Dict[str, Any]:
        try:
            response = self.model.generate_content([
                "Execute and analyze this code:\n```python\n" + code + "\n```"
            ])
            return {
                "result": response.text,
                "status": "success"
            }
        except Exception as e:
            logger.error(f"Code execution failed: {str(e)}")
            return {
                "error": str(e),
                "status": "failed"
            }

    @retry_with_backoff(retries=3)
    def generate_code(self, prompt: str, context: Optional[Dict] = None) -> Dict[str, Any]:
        try:
            response = self.model.generate_content([
                "Generate code based on this prompt:\n" + prompt
            ])
            return {
                "code": response.text,
                "status": "success"
            }
        except Exception as e:
            logger.error(f"Code generation failed: {str(e)}")
            return {
                "error": str(e),
                "status": "failed"
            }

class CodeVisionAnalyzer:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY environment variable is required")
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("models/gemini-pro-vision")

    def _encode_image(self, image_path: str) -> str:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode("utf-8")

    @retry_with_backoff(retries=3)
    def analyze_code_image(self, image_path: str) -> Dict[str, Any]:
        try:
            img = Image.open(image_path)
            response = self.model.generate_content(["Analyze this code image:", img])
            return {
                "analysis": response.text,
                "status": "success"
            }
        except Exception as e:
            logger.error(f"Code image analysis failed: {str(e)}")
            return {
                "error": str(e),
                "status": "failed"
            }

    @retry_with_backoff(retries=3)
    def generate_from_diagram(self, image_path: str, context: Optional[Dict] = None) -> Dict[str, Any]:
        try:
            img = Image.open(image_path)
            response = self.model.generate_content([
                "Generate code based on this diagram/flowchart:",
                img
            ])
            return {
                "code": response.text,
                "status": "success"
            }
        except Exception as e:
            logger.error(f"Code generation from diagram failed: {str(e)}")
            return {
                "error": str(e),
                "status": "failed"
            }
