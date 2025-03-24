from datetime import datetime
from crewai import Agent, Task, Crew, Process
import yaml
from pathlib import Path
import os
from typing import Dict, List, Optional
from .tools.custom_tool import (
    FileOutputTool, 
    MarkdownFormatter, 
    PromptTemplateLibrary, 
    PromptTestingTool,
    StructuredThinkingTool,
    BranchAnalysisTool
)

# Load configuration
config_dir = Path(__file__).parent / "config"

with open(config_dir / "agents.yaml", "r") as f:
    agents_config = yaml.safe_load(f)

with open(config_dir / "tasks.yaml", "r") as f:
    tasks_config = yaml.safe_load(f)

class OllamaCrew:
    def __init__(
        self, 
        topic: str = "AI and machine learning", 
        output_dir: str = "./outputs",
        analysis_depth: str = "detailed",
        branch_depth: int = 3
    ):
        self.topic = topic
        self.output_dir = output_dir
        self.analysis_depth = analysis_depth
        self.branch_depth = branch_depth
        self.agents = {}
        self.tasks = {}
        self.tools = self._initialize_tools()
        self.context = {}

    def _initialize_tools(self) -> Dict:
        """Initialize all available tools"""
        return {
            "file_output_tool": FileOutputTool(output_dir=self.output_dir),
            "prompt_testing_tool": PromptTestingTool(),
            "prompt_template_library": PromptTemplateLibrary(),
            "markdown_formatter": MarkdownFormatter(),
            "structured_thinking_tool": StructuredThinkingTool(),
            "branch_analysis_tool": BranchAnalysisTool()
        }

    def _format_agent_variables(self, config: Dict) -> Dict:
        """Format agent configuration variables"""
        formatted = {}
        for key, value in config.items():
            if isinstance(value, str):
                formatted[key] = value.format(
                    topic=self.topic,
                    analysis_depth=self.analysis_depth,
                    branch_depth=self.branch_depth,
                    **self.context
                )
            else:
                formatted[key] = value
        return formatted

    def get_agents(self) -> Dict[str, Agent]:
        """Create agents based on the configuration"""
        for name, config in agents_config.items():
            if config.get("base_config", False):
                continue
            
            # Format configuration variables
            formatted_config = self._format_agent_variables(config)
            
            # Initialize tools based on the agent
            tools = self._get_agent_tools(formatted_config)
            
            self.agents[name] = Agent(
                role=formatted_config["role"],
                goal=formatted_config["goal"],
                backstory=formatted_config["backstory"],
                verbose=True,
                allow_delegation=True,
                tools=tools,
                temperature=formatted_config.get("temperature", 0.7)
            )
        
        return self.agents

    def _get_agent_tools(self, config: Dict) -> List:
        """Get tools for an agent based on configuration"""
        tools = []
        if "tools" in config:
            for tool_name in config["tools"]:
                if tool_name in self.tools:
                    tools.append(self.tools[tool_name])
        return tools

    def _format_task_variables(self, config: Dict) -> Dict:
        """Format task configuration variables"""
        formatted = {}
        for key, value in config.items():
            if isinstance(value, str):
                formatted[key] = value.format(
                    topic=self.topic,
                    analysis_depth=self.analysis_depth,
                    branch_depth=self.branch_depth,
                    **self.context
                )
            elif isinstance(value, dict):
                formatted[key] = {
                    k: v.format(
                        topic=self.topic,
                        analysis_depth=self.analysis_depth,
                        branch_depth=self.branch_depth,
                        **self.context
                    ) if isinstance(v, str) else v
                    for k, v in value.items()
                }
            else:
                formatted[key] = value
        return formatted

    def get_tasks(self) -> List[Task]:
        """Create tasks based on the configuration"""
        if not self.agents:
            self.get_agents()
        
        for name, config in tasks_config.items():
            if name.startswith("task_templates"):
                continue
            
            # Format task configuration
            formatted_config = self._format_task_variables(config)
            
            # Get the agent for this task
            agent = self.agents[formatted_config["agent"]]
            
            # Set up task dependencies
            depends_on = []
            if "depends_on" in formatted_config:
                for dep in formatted_config["depends_on"]:
                    if dep in self.tasks:
                        depends_on.append(self.tasks[dep])
            
            # Create task with additional context
            self.tasks[name] = Task(
                description=formatted_config["description"],
                expected_output=formatted_config["expected_output"],
                agent=agent,
                depends_on=depends_on,
                context=formatted_config.get("context", {}),
                tools=self._get_agent_tools(formatted_config.get("agent_config", {}))
            )
        
        return list(self.tasks.values())

    def add_context(self, context: Dict) -> None:
        """Add additional context for variable formatting"""
        self.context.update(context)

    def run(self, process_type: Process = Process.sequential) -> Dict:
        """Run the crew with specified process type"""
        crew = Crew(
            agents=list(self.agents.values()),
            tasks=list(self.tasks.values()),
            verbose=2,
            process=process_type
        )
        
        try:
            result = crew.kickoff()
            
            # Save results using FileOutputTool
            output_tool = self.tools["file_output_tool"]
            output_tool._execute(
                content=result,
                file_name=f"{self.topic.lower().replace(' ', '_')}_analysis.md",
                format="markdown",
                metadata={
                    "topic": self.topic,
                    "analysis_depth": self.analysis_depth,
                    "branch_depth": self.branch_depth,
                    "timestamp": str(datetime.now())
                }
            )
            
            return result
            
        except Exception as e:
            print(f"Error during crew execution: {str(e)}")
            return {"error": str(e), "status": "failed"}
