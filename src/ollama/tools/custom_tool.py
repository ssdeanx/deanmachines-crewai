import json
import logging
from multiprocessing import util
import os
import time
import xml.etree.ElementTree as ET
from datetime import datetime
from dataclasses import dataclass
from enum import Enum
from functools import wraps
from pathlib import Path
from typing import Any, Dict, List, Optional, Type, Union

from crewai import Tool
from crewai.tools import BaseTool
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

class XMLValidationError(Exception):
    """Custom exception for XML validation errors."""
    pass

class StructureError(Exception):
    """Custom exception for structure-related errors."""
    pass

@dataclass
class ValidationResult:
    """Structured validation result."""
    valid: bool
    score: float
    issues: List[str]
    details: Dict[str, Any]

class ValidationLevel(Enum):
    """Validation severity levels."""
    STRICT = "strict"
    NORMAL = "normal"
    RELAXED = "relaxed"

class XMLStructureInput(BaseModel):
    """Input schema for XML structure validation."""
    content: str = Field(..., description="XML content to validate")
    required_tags: List[str] = Field(
        default=["plan", "thoughts", "analysis", "execution"]
    )
    check_cdata: bool = Field(
        default=True,
        description="Whether to check CDATA sections"
    )

class BranchAnalysisInput(BaseModel):
    """Input schema for branch analysis."""
    scenario: str = Field(..., description="Initial scenario to analyze")
    depth: int = Field(default=3, description="Branch depth")
    width: int = Field(default=3, description="Maximum alternatives per node")

class SmartRecoveryMixin:
    """Add to tools for intelligent error recovery."""
    
    def recover_from_error(self, error: Exception, context: Dict) -> Dict:
        """Attempt to recover from various error types."""
        try:
            if isinstance(error, XMLValidationError):
                return self._fix_xml_structure(context)
            if isinstance(error, StructureError):
                return self._reorganize_structure(context)
            return self._general_recovery(context)
        except Exception as e:
            logger.error(f"Recovery failed: {str(e)}")
            return {"status": "failed", "error": str(e)}

    def _fix_xml_structure(self, context: Dict) -> Dict:
        """Fix common XML structure issues."""
        # Implementation here
        return {"status": "fixed", "context": context}

    def _reorganize_structure(self, context: Dict) -> Dict:
        """Reorganize malformed structure."""
        # Implementation here
        return {"status": "reorganized", "context": context}

    def _general_recovery(self, context: Dict) -> Dict:
        """General error recovery strategy."""
        # Implementation here
        return {"status": "recovered", "context": context}

class MyCustomToolInput(BaseModel):
    """Input schema for MyCustomTool."""
    argument: str = Field(..., description="Description of the argument.")

class PatternRecognitionInput(BaseModel):
    """Input schema for pattern recognition in thinking structures."""
    content: str = Field(..., description="Content to analyze")
    pattern_types: List[str] = Field(
        default=["decision", "analysis", "implementation"]
    )

class StructuredThinkingTool(BaseTool, SmartRecoveryMixin):
    """Tool for structured thinking pattern validation and analysis."""
    name: str = "structured_thinking_tool"
    description: str = "Validate and analyze XML-structured thinking patterns"
    args_schema: Type[BaseModel] = XMLStructureInput

    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger(__name__)

    def _validate_cdata(self, elem: ET.Element) -> List[str]:
        """Validate CDATA sections in an element."""
        issues = []
        try:
            if not any(child.tag == '![CDATA[' for child in elem):
                issues.append(f"Missing CDATA in {elem.tag}")
            for child in elem:
                if child.tag == '![CDATA[' and not child.text.strip():
                    issues.append(f"Empty CDATA in {elem.tag}")
        except Exception as e:
            self.logger.error(f"CDATA validation error in {elem.tag}: {str(e)}")
            issues.append(f"CDATA validation failed: {str(e)}")
        return issues

    def _calculate_score(
        self, 
        total: int, 
        missing: int, 
        issues: int,
        weights: Dict[str, float] = {"missing": 1.0, "issues": 0.5}
    ) -> float:
        """Calculate weighted structure score."""
        if total == 0:
            return 0.0
        weighted_deductions = (missing * weights["missing"]) + (issues * weights["issues"])
        score = max(0.0, min(1.0, 1.0 - (weighted_deductions / total)))
        return round(score, 2)

    def _run(
        self, 
        content: str, 
        required_tags: List[str], 
        check_cdata: bool,
        validation_level: ValidationLevel = ValidationLevel.NORMAL
    ) -> Dict:
        """Run validation with enhanced error handling."""
        try:
            result = ValidationResult(
                valid=True,
                score=0.0,
                issues=[],
                details={
                    "missing_tags": [],
                    "cdata_issues": [],
                    "structure_warnings": [],
                    "validation_level": validation_level.value
                }
            )

            try:
                root = ET.fromstring(content)
            except ET.ParseError as e:
                raise XMLValidationError(f"XML parsing error: {str(e)}")

            self._validate_content(root, required_tags, check_cdata, 
                                validation_level, result)

            return {
                "valid": result.valid,
                "score": result.score,
                "issues": result.issues,
                "details": result.details,
                "timestamp": datetime.now().isoformat()
            }

        except XMLValidationError as e:
            self.logger.error(f"XML validation failed: {str(e)}")
            return {
                "valid": False,
                "error": str(e),
                "score": 0.0,
                "timestamp": datetime.now().isoformat()
            }
        except Exception as e:
            self.logger.error(f"Unexpected error: {str(e)}")
            return {
                "valid": False,
                "error": f"Internal error: {str(e)}",
                "score": 0.0,
                "timestamp": datetime.now().isoformat()
            }

    def _validate_content(
        self,
        root: ET.Element,
        required_tags: List[str],
        check_cdata: bool,
        validation_level: ValidationLevel,
        result: ValidationResult
    ) -> None:
        """Validate content structure and requirements."""
        for tag in required_tags:
            elem = root.find(tag)
            if elem is None:
                result.valid = False
                result.issues.append(f"Missing required tag: {tag}")
                result.details["missing_tags"].append(tag)
            elif check_cdata:
                self._process_cdata_issues(elem, validation_level, result)

        try:
            self._validate_structure(root, result)
        except StructureError as e:
            result.details["structure_warnings"].append(str(e))
            if validation_level == ValidationLevel.STRICT:
                result.valid = False
                result.issues.append(str(e))

        result.score = self._calculate_score(
            total=len(required_tags),
            missing=len(result.details["missing_tags"]),
            issues=len(result.details["cdata_issues"])
        )

    def _process_cdata_issues(
        self,
        elem: ET.Element,
        validation_level: ValidationLevel,
        result: ValidationResult
    ) -> None:
        """Process CDATA validation issues."""
        cdata_issues = self._validate_cdata(elem)
        if cdata_issues:
            result.details["cdata_issues"].extend(cdata_issues)
            if validation_level == ValidationLevel.STRICT:
                result.valid = False
            result.issues.extend(cdata_issues)

class MyCustomTool(BaseTool):
    name: str = "Name of my tool"
    description: str = (
        "Clear description for what this tool is useful for, your agent will need this information to use it."
    )
    args_schema: Type[BaseModel] = MyCustomToolInput

    def _run(self, argument: str) -> str:
        # Implementation goes here
        return "this is an example of a tool output, ignore it and move along."

class BranchAnalysisTool(BaseTool):
    name: str = "branch_analysis_tool"
    description: str = "Analyze decision trees and branching patterns"
    args_schema: Type[BaseModel] = BranchAnalysisInput

    def _run(self, scenario: str, depth: int, width: int) -> Dict:
        analysis = {
            "root": scenario,
            "branches": [],
            "metrics": {
                "total_paths": 0,
                "max_depth": 0,
                "complexity_score": 0.0
            }
        }
        
        def generate_branches(node: str, current_depth: int) -> List[Dict]:
            if current_depth >= depth:
                return []
                
            branches = []
            for i in range(width):
                branch = {
                    "id": f"branch_{current_depth}_{i}",
                    "description": f"Alternative {i+1} for {node}",
                    "sub_branches": generate_branches(f"Alternative {i+1}", current_depth + 1)
                }
                branches.append(branch)
                analysis["metrics"]["total_paths"] += 1
            
            return branches
        
        analysis["branches"] = generate_branches(scenario, 0)
        analysis["metrics"]["max_depth"] = depth
        analysis["metrics"]["complexity_score"] = (depth * width) / 10.0
        
        return analysis

class FileOutputTool(Tool):
    name: str = "file_output_tool"
    description: str = "Write structured content to files with various formats"
    
    def __init__(self, output_dir="./outputs"):
        self.output_dir = output_dir
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
    
    def _execute(
        self, 
        content: str, 
        file_name: str, 
        format: str = "markdown",
        metadata: Optional[Dict] = None
    ) -> str:
        """Write content to file with metadata and formatting."""
        file_path = os.path.join(self.output_dir, file_name)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        # Add metadata if provided
        if metadata:
            if format == "markdown":
                content = f"---\n{json.dumps(metadata, indent=2)}\n---\n\n{content}"
            elif format == "xml":
                content = f"<!-- metadata: {json.dumps(metadata)} -->\n{content}"
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return f"Successfully wrote {format} content to {file_path}"

class PromptTestingTool(Tool):
    name: str = "prompt_testing_tool"
    description: str = "Comprehensive prompt testing and validation"
    
    def _execute(
        self, 
        prompt: str,
        test_cases: List[Dict],
        criteria: Dict[str, float],
        validation_rules: Optional[List[str]] = None
    ) -> Dict:
        results = {
            "timestamp": datetime.now().isoformat(),
            "prompt": prompt,
            "test_results": [],
            "overall_score": 0.0,
            "recommendations": []
        }
        
        # Implement testing logic here
        return results

class PromptTemplateLibrary:
    name: str = "prompt_template_library"
    description: str = "Manage prompt templates"
    
    def _execute(self, action: str, template_id=None, category=None, template=None):
        # Implement template management
        pass
        
class MarkdownFormatter:
    name: str = "markdown_formatter"
    description: str = "Format content as markdown"
    
    def _execute(self, content: dict, template_type="documentation"):
        # Implement markdown formatting
        pass

class DocumentationGenerator:
    """Generate comprehensive documentation"""
    def generate_docs(self, analysis_results: Dict) -> str:
        template = """
# Analysis Documentation

## Overview
{overview}

## Structured Analysis
{xml_structure}

## Branch Analysis
{branch_tree}

## Validation Results
{validation}

## Performance Metrics
{metrics}
        """
        return template.format(**self._format_sections(analysis_results))

class AdvancedValidator:
    """Enhanced validation with pattern matching"""
    def validate_structure(self, content: str) -> ValidationResult:
        patterns = {
            "xml_structure": r"<(\w+)>.*?</\1>",
            "cdata_sections": r"<!\[CDATA\[.*?\]\]>",
            "branch_patterns": r"├──|└──"
        }
        
        return self._check_patterns(content, patterns)

class PerformanceMonitor:
    """Monitor and optimize system performance"""
    def __init__(self):
        self.metrics = {
            "execution_times": [],
            "success_rates": [],
            "error_rates": [],
            "validation_scores": [],
            "memory_usage": [],
            "complexity_scores": []
        }
        self.start_time = datetime.now()
        
    def track_execution(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            memory_start = util.Process().memory_info().rss
            try:
                result = func(*args, **kwargs)
                self.metrics["success_rates"].append(1)
                self.metrics["error_rates"].append(0)
                return result
            except Exception as e:
                self.metrics["success_rates"].append(0)
                self.metrics["error_rates"].append(1)
                raise
            finally:
                execution_time = time.time() - start_time
                memory_used = (util.Process().memory_info().rss - memory_start) / (1024 * 1024)
                self.metrics["execution_times"].append(execution_time)
                self.metrics["memory_usage"].append(memory_used)
        return wrapper

    def get_performance_summary(self) -> Dict:
        """Get summary of performance metrics"""
        return {
            "average_execution_time": sum(self.metrics["execution_times"]) / len(self.metrics["execution_times"]) if self.metrics["execution_times"] else 0,
            "success_rate": sum(self.metrics["success_rates"]) / len(self.metrics["success_rates"]) if self.metrics["success_rates"] else 0,
            "error_rate": sum(self.metrics["error_rates"]) / len(self.metrics["error_rates"]) if self.metrics["error_rates"] else 0,
            "average_memory_usage": sum(self.metrics["memory_usage"]) / len(self.metrics["memory_usage"]) if self.metrics["memory_usage"] else 0,
            "total_runtime": (datetime.now() - self.start_time).total_seconds()
        }

# Add to template files
current_date = datetime.now().strftime("%Y-%m-%d")
template = f"""
version: "2.0"
last_updated: "{current_date}"
changelog: 
  - version: "2.0"
    changes:
      - "Added XML structure validation"
      - "Enhanced branching patterns"
      - "Improved error recovery"
  - version: "1.0"
    changes:
      - "Initial implementation"
"""

