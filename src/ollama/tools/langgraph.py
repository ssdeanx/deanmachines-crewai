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

class AnalysisPhase(str, Enum):
    """Phases of structured thinking process"""
    PLAN = "plan"
    THOUGHTS = "thoughts"
    ANALYSIS = "analysis"
    EXECUTION = "execution"
    REVIEW = "review"
    COMPLETE = "complete"

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
    
    def should_continue(state: ThinkingState) -> Tuple[bool, str]:
        """Determine if thinking process should continue"""
        if state.analysis_depth >= max_iterations:
            return False, "MAX_DEPTH"
        if state.current_phase == AnalysisPhase.COMPLETE:
            return False, "COMPLETE"
        return True, state.current_phase
    
    def process_phase(
        state: ThinkingState,
        phase: AnalysisPhase,
        messages: List[BaseMessage]
    ) -> ThinkingState:
        """Process current thinking phase"""
        try:
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
    
    # Create the graph
    workflow = StateGraph(ThinkingState)
    
    # Add nodes for each phase
    workflow.add_node("plan", lambda x: process_phase(x, AnalysisPhase.PLAN, x.messages))
    workflow.add_node("thoughts", lambda x: process_phase(x, AnalysisPhase.THOUGHTS, x.messages))
    workflow.add_node("analysis", lambda x: process_phase(x, AnalysisPhase.ANALYSIS, x.messages))
    workflow.add_node("execution", lambda x: process_phase(x, AnalysisPhase.EXECUTION, x.messages))
    
    # Add conditional edges
    workflow.add_edge("plan", "thoughts")
    workflow.add_edge("thoughts", "analysis")
    workflow.add_edge("analysis", "execution")
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
            "analysis": "analysis"
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
    
    graph = create_thinking_graph(
        llm=llm,
        tools=tools,
        template_path=template_path
    )
    
    # Initialize state
    state = ThinkingState(
        current_phase=AnalysisPhase.PLAN,
        context=initial_state or {},
        metadata={
            "start_time": datetime.now().isoformat(),
            "template": template_path
        }
    )
    
    return {
        "graph": graph,
        "initial_state": state,
        "tools": tools
    }