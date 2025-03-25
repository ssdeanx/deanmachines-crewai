from typing import Dict, List, Tuple, Any, Optional
from langchain.schema import BaseMessage, HumanMessage, AIMessage
from langchain.prompts import ChatPromptTemplate
from langchain_core.graphs import StateGraph, END
from langgraph.prebuilt import ToolExecutor
import operator
from pydantic import BaseModel, Field
from enum import Enum
import logging
from datetime import datetime
import mlflow

logger = logging.getLogger(__name__)

class ThinkingState(BaseModel):
    """State management for thinking process"""
    messages: List[BaseMessage] = Field(default_factory=list)
    current_phase: str = Field(default="plan")
    next_steps: List[str] = Field(default_factory=list)
    analysis_depth: int = Field(default=0)
    branch_points: List[Dict] = Field(default_factory=list)
    context: Dict = Field(default_factory=dict)
    metadata: Dict = Field(default_factory=dict)
    code_executions: List[Dict] = Field(default_factory=list)
    vision_analyses: List[Dict] = Field(default_factory=list)

class AnalysisPhase(str, Enum):
    """Phases of structured thinking process"""
    PLAN = "plan"
    THOUGHTS = "thoughts"
    ANALYSIS = "analysis"
    EXECUTION = "execution"
    REVIEW = "review"
    COMPLETE = "complete"
    CODE_EXECUTION = "code_execution"
    VISION_ANALYSIS = "vision_analysis"

def create_thinking_graph(
    llm,
    tools: List[Dict],
    template_path: str,
    max_iterations: int = 5
) -> StateGraph:
    """Create a graph for structured thinking process"""

    # Initialize tools
    tool_executor = ToolExecutor(tools)

    # Load template
    with open(template_path, 'r') as f:
        template_content = f.read()

    # Create prompts for different phases
    planning_prompt = ChatPromptTemplate.from_template("""
    <plan>
    <planDescription>
    <![CDATA[
    Based on the current context and state, develop a strategic plan.
    Current State: {current_state}
    Objective: {objective}
    Constraints: {constraints}
    ]]>
    </planDescription>
    </plan>
    """)

    analysis_prompt = ChatPromptTemplate.from_template("""
    <analysis>
    <analysisDescription>
    <![CDATA[
    Analyze the current situation and previous steps.
    Current Phase: {current_phase}
    Previous Results: {previous_results}
    Branch Points: {branch_points}
    ]]>
    </analysisDescription>
    </analysis>
    """)

    # Add code execution prompt
    code_execution_prompt = ChatPromptTemplate.from_template("""
    <code_execution>
    <executionContext>
    <![CDATA[
    Execute and analyze code in current context.
    Code: {code}
    Previous Results: {previous_results}
    Vision Analysis: {vision_analysis}
    ]]>
    </executionContext>
    </code_execution>
    """)

    def should_continue(state: ThinkingState) -> Tuple[bool, str]:
        """Determine if thinking process should continue"""
        if state.analysis_depth >= max_iterations:
            return False, "MAX_DEPTH"
        if state.current_phase == AnalysisPhase.COMPLETE:
            return False, "COMPLETE"
        return True, state.current_phase

    def track_state_transition(state: ThinkingState, phase: str) -> None:
        """Track state transition metrics in MLflow"""
        try:
            with mlflow.start_run(nested=True):
                mlflow.log_params({
                    "phase": phase,
                    "analysis_depth": state.analysis_depth,
                    "has_code": bool(state.code_executions),
                    "has_vision": bool(state.vision_analyses)
                })

                # Track phase-specific metrics
                metrics = {
                    "branch_points": len(state.branch_points),
                    "next_steps": len(state.next_steps)
                }

                if phase == AnalysisPhase.CODE_EXECUTION:
                    metrics.update({
                        "code_executions": len(state.code_executions),
                        "code_success_rate": sum(1 for x in state.code_executions if x.get("status") == "success") / len(state.code_executions) if state.code_executions else 0
                    })

                if phase == AnalysisPhase.VISION_ANALYSIS:
                    metrics.update({
                        "vision_analyses": len(state.vision_analyses),
                        "vision_success_rate": sum(1 for x in state.vision_analyses if x.get("status") == "success") / len(state.vision_analyses) if state.vision_analyses else 0
                    })

                mlflow.log_metrics(metrics)

        except Exception as e:
            logger.error(f"Failed to track state transition: {str(e)}")

    def process_phase(
        state: ThinkingState,
        phase: AnalysisPhase,
        messages: List[BaseMessage]
    ) -> ThinkingState:
        """Process current thinking phase with MLflow tracking"""
        try:
            track_state_transition(state, phase)

            # Update state with new messages
            state.messages.extend(messages)

            # Process based on phase
            if phase == AnalysisPhase.PLAN:
                # Planning phase logic
                state.next_steps = ["thoughts", "analysis"]
                state.context.update({"plan_completed": datetime.now().isoformat()})

            elif phase == AnalysisPhase.THOUGHTS:
                # Thought process logic
                state.branch_points.append({
                    "phase": "thoughts",
                    "timestamp": datetime.now().isoformat(),
                    "branches": []  # Add actual branches here
                })

            elif phase == AnalysisPhase.ANALYSIS:
                # Analysis logic
                state.analysis_depth += 1
                state.context.update({"analysis_depth": state.analysis_depth})

            elif phase == AnalysisPhase.EXECUTION:
                # Execution logic
                if not state.next_steps:
                    state.current_phase = AnalysisPhase.COMPLETE

            # Update metadata
            state.metadata.update({
                "last_update": datetime.now().isoformat(),
                "current_phase": phase,
                "iterations": state.analysis_depth
            })

            return state

        except Exception as e:
            logger.error(f"Error in phase {phase}: {str(e)}")
            state.metadata["errors"] = state.metadata.get("errors", []) + [str(e)]
            return state

    def process_code_execution(state: ThinkingState) -> ThinkingState:
        """Process code execution phase with MLflow tracking"""
        try:
            track_state_transition(state, AnalysisPhase.CODE_EXECUTION)

            # Execute code and store results
            if "code" in state.context:
                execution_result = tools["code_executor"].execute_code(
                    state.context["code"],
                    state.context.get("vision_analysis")
                )
                state.code_executions.append(execution_result)
                state.context["last_execution"] = execution_result

            state.metadata.update({
                "last_code_execution": datetime.now().isoformat()
            })

            return state
        except Exception as e:
            logger.error(f"Code execution error: {str(e)}")
            state.metadata["errors"] = state.metadata.get("errors", []) + [str(e)]
            return state

    def process_vision_analysis(state: ThinkingState) -> ThinkingState:
        """Process vision analysis phase with MLflow tracking"""
        try:
            track_state_transition(state, AnalysisPhase.VISION_ANALYSIS)

            # Analyze code images if present
            if "image_path" in state.context:
                vision_result = tools["vision_analyzer"].analyze_code_image(
                    state.context["image_path"]
                )
                state.vision_analyses.append(vision_result)
                state.context["last_vision_analysis"] = vision_result

            state.metadata.update({
                "last_vision_analysis": datetime.now().isoformat()
            })

            return state
        except Exception as e:
            logger.error(f"Vision analysis error: {str(e)}")
            state.metadata["errors"] = state.metadata.get("errors", []) + [str(e)]
            return state

    # Create the graph
    workflow = StateGraph(ThinkingState)

    # Add nodes for each phase including new code and vision nodes
    workflow.add_node("plan", lambda x: process_phase(x, AnalysisPhase.PLAN, x.messages))
    workflow.add_node("thoughts", lambda x: process_phase(x, AnalysisPhase.THOUGHTS, x.messages))
    workflow.add_node("analysis", lambda x: process_phase(x, AnalysisPhase.ANALYSIS, x.messages))
    workflow.add_node("code_execution", process_code_execution)
    workflow.add_node("vision_analysis", process_vision_analysis)
    workflow.add_node("execution", lambda x: process_phase(x, AnalysisPhase.EXECUTION, x.messages))

    # Add edges including new nodes
    workflow.add_edge("plan", "thoughts")
    workflow.add_edge("thoughts", "analysis")
    workflow.add_edge("analysis", "code_execution")
    workflow.add_edge("code_execution", "vision_analysis")
    workflow.add_edge("vision_analysis", "execution")
    workflow.add_edge("execution", "plan")

    # Add conditional branching
    workflow.add_conditional_edges(
        "execution",
        should_continue,
        {
            "COMPLETE": END,
            "MAX_DEPTH": END,
            "plan": "plan",
            "thoughts": "thoughts",
            "analysis": "analysis",
            "code_execution": "code_execution",
            "vision_analysis": "vision_analysis"
        }
    )

    return workflow.compile()

def create_analysis_workflow(
    llm,
    tools: List[Dict],
    template_path: str,
    initial_state: Optional[Dict] = None
) -> Any:
    """Create a complete analysis workflow"""

    # Ensure code and vision tools are available
    required_tools = ["code_executor", "vision_analyzer"]
    for tool in required_tools:
        if tool not in tools:
            logger.warning(f"Missing required tool: {tool}")

    graph = create_thinking_graph(
        llm=llm,
        tools=tools,
        template_path=template_path
    )

    # Initialize state with code and vision support
    state = ThinkingState(
        current_phase=AnalysisPhase.PLAN,
        context=initial_state or {},
        metadata={
            "start_time": datetime.now().isoformat(),
            "template": template_path,
            "code_execution_enabled": "code_executor" in tools,
            "vision_analysis_enabled": "vision_analyzer" in tools
        }
    )

    return {
        "graph": graph,
        "initial_state": state,
        "tools": tools
    }
