"""
Simplified task definitions for CrewAI test harnesses.
Provides consistent task creation function for testing with different LLMs.
"""
import logging
from typing import Dict, List, Any
from crewai import Task

def get_sequential_tasks(
    agents: Dict[str, Any],
    topic: str = "climate change impacts on agriculture"
) -> List[Task]:
    """
    Create three sequential tasks with proper context passing between them.

    Args:
        agents: Dictionary of agent instances with keys "researcher", "summarizer", "reporter"
        topic: The topic to research, summarize, and report on

    Returns:
        List of Task objects in the correct execution order: [research_task, summarize_task, report_task]

    Notes:
        CrewAI context passing works through the context=[previous_task] mechanism.
        This is what enables output from one task to be used as input for the next task.
        Task order in the returned list is crucial for sequential processing.

    Raises:
        ValueError: If any required agent role is missing from the agents dictionary
    """
    logger = logging.getLogger(__name__)
    logger.info(f"Creating sequential tasks for topic: {topic}")

    # Validate required agents
    required_agents = ["researcher", "summarizer", "reporter"]
    for agent_role in required_agents:
        if agent_role not in agents:
            error_msg = f"Missing required agent: {agent_role}"
            logger.error(error_msg)
            raise ValueError(error_msg)

    # Create the research task (first task, no dependencies)
    research_task = Task(
        description=f"""
        Conduct thorough research on the topic: "{topic}".

        Your research should include:
        1. Key facts and statistics
        2. Different perspectives on the issue
        3. Recent developments
        4. Notable experts and their viewpoints
        5. Potential future implications

        Be thorough and cite sources when possible.
        """,
        expected_output="A comprehensive research document with key information on the topic",
        agent=agents["researcher"]
    )

    # Create the summarize task (depends on research_task)
    summarize_task = Task(
        description=f"""
        Create a structured summary of the research on: "{topic}".

        Your summary should:
        1. Extract the most important points from the research
        2. Organize information into clear categories
        3. Present information in bullet point format for easy scanning
        4. Highlight key statistics and facts
        5. Identify knowledge gaps if any exist

        Focus on clarity and brevity in your summary.
        """,
        expected_output="A well-structured summary with bullet points highlighting key findings",
        agent=agents["summarizer"],
        context=[research_task]  # This is how context is passed from research_task
    )

    # Create the report task (depends on summarize_task)
    report_task = Task(
        description=f"""
        Create a comprehensive report on: "{topic}" based on the provided summary.

        Your report should:
        1. Begin with an executive summary
        2. Include an introduction to the topic
        3. Present findings in a logical, organized manner
        4. Include a conclusion with implications
        5. End with recommendations or next steps if appropriate

        Make the report engaging and professional.
        """,
        expected_output="A complete, professional report synthesizing all the information",
        agent=agents["reporter"],
        context=[summarize_task]  # This is how context is passed from summarize_task
    )

    logger.info("Successfully created sequential tasks with proper context dependencies")
    return [research_task, summarize_task, report_task]
