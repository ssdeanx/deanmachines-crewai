"""
Simplified agent definitions for CrewAI test harnesses.
Provides consistent agent creation functions for testing with different LLMs.
"""
import logging
from typing import Dict, Optional, Any
from crewai import Agent

def get_gemini_agents(gemini_llm, tools: Optional[Dict[str, Any]] = None) -> Dict[str, Agent]:
    """
    Create three simplified agents (researcher, summarizer, reporter) all using Gemini LLM.

    Args:
        gemini_llm: The Gemini LLM instance to use for all agents
        tools: Optional dictionary of tools to assign to specific agents
               e.g., {"researcher": [web_search_tool]}

    Returns:
        Dictionary of Agent instances keyed by role name
    """
    logger = logging.getLogger(__name__)
    logger.info("Creating three Gemini agents: researcher, summarizer, reporter")

    # Initialize tools for each agent - safely handle None
    researcher_tools = tools.get("researcher", []) if tools else []
    summarizer_tools = tools.get("summarizer", []) if tools else []
    reporter_tools = tools.get("reporter", []) if tools else []

    # Create the agents
    researcher = Agent(
        role="Research Specialist",
        goal="Find accurate, comprehensive information about the assigned topic",
        backstory="You are an expert research analyst with a talent for finding and synthesizing information. You're meticulous and always cite your sources.",
        verbose=True,
        allow_delegation=False,
        tools=researcher_tools,
        llm=gemini_llm
    )

    summarizer = Agent(
        role="Content Summarizer",
        goal="Create concise, structured summaries that capture the key points",
        backstory="You are a skilled editor who can extract essential insights and organize them into bullet points and summaries. You value clarity and brevity.",
        verbose=True,
        allow_delegation=False,
        tools=summarizer_tools,
        llm=gemini_llm
    )

    reporter = Agent(
        role="Report Generator",
        goal="Create polished, comprehensive reports based on summarized information",
        backstory="You are a professional writer and communicator who excels at creating well-organized, engaging reports. You focus on clarity, flow, and reader engagement.",
        verbose=True,
        allow_delegation=False,
        tools=reporter_tools,
        llm=gemini_llm
    )

    return {
        "researcher": researcher,
        "summarizer": summarizer,
        "reporter": reporter
    }

def get_lmstudio_agents(lmstudio_llm, tools: Optional[Dict[str, Any]] = None) -> Dict[str, Agent]:
    """
    Create three simplified agents (researcher, summarizer, reporter) all using LM Studio LLM.

    Args:
        lmstudio_llm: The LM Studio LLM instance to use for all agents
        tools: Optional dictionary of tools to assign to specific agents
               e.g., {"researcher": [web_search_tool]}

    Returns:
        Dictionary of Agent instances keyed by role name
    """
    logger = logging.getLogger(__name__)
    logger.info("Creating three LM Studio agents: researcher, summarizer, reporter")

    # Initialize tools for each agent - safely handle None
    researcher_tools = tools.get("researcher", []) if tools else []
    summarizer_tools = tools.get("summarizer", []) if tools else []
    reporter_tools = tools.get("reporter", []) if tools else []

    # Create the agents
    researcher = Agent(
        role="Research Specialist (LM Studio)",
        goal="Find accurate, comprehensive information about the assigned topic",
        backstory="You are an expert research analyst with a talent for finding and synthesizing information. You're meticulous and always cite your sources.",
        verbose=True,
        allow_delegation=False,
        tools=researcher_tools,
        llm=lmstudio_llm
    )

    summarizer = Agent(
        role="Content Summarizer (LM Studio)",
        goal="Create concise, structured summaries that capture the key points",
        backstory="You are a skilled editor who can extract essential insights and organize them into bullet points and summaries. You value clarity and brevity.",
        verbose=True,
        allow_delegation=False,
        tools=summarizer_tools,
        llm=lmstudio_llm
    )

    reporter = Agent(
        role="Report Generator (LM Studio)",
        goal="Create polished, comprehensive reports based on summarized information",
        backstory="You are a professional writer and communicator who excels at creating well-organized, engaging reports. You focus on clarity, flow, and reader engagement.",
        verbose=True,
        allow_delegation=False,
        tools=reporter_tools,
        llm=lmstudio_llm
    )

    return {
        "researcher": researcher,
        "summarizer": summarizer,
        "reporter": reporter
    }

def get_combo_agents(gemini_llm, lmstudio_llm, tools: Optional[Dict[str, Any]] = None) -> Dict[str, Agent]:
    """
    Create three agents with mixed LLM assignment:
    - Researcher: Using Gemini
    - Summarizer: Using LM Studio
    - Reporter: Using Gemini

    Args:
        gemini_llm: The Gemini LLM instance to use
        lmstudio_llm: The LM Studio LLM instance to use
        tools: Optional dictionary of tools to assign to specific agents
               e.g., {"researcher": [web_search_tool]}

    Returns:
        Dictionary of Agent instances keyed by role name
    """
    logger = logging.getLogger(__name__)
    logger.info("Creating combo agents with mixed LLM assignment: Gemini→LM Studio→Gemini")

    # Initialize tools for each agent - safely handle None
    researcher_tools = tools.get("researcher", []) if tools else []
    summarizer_tools = tools.get("summarizer", []) if tools else []
    reporter_tools = tools.get("reporter", []) if tools else []

    # Create the agents with specific LLM assignments
    researcher = Agent(
        role="Research Specialist (Gemini)",
        goal="Find accurate, comprehensive information about the assigned topic",
        backstory="You are an expert research analyst with a talent for finding and synthesizing information. You're meticulous and always cite your sources.",
        verbose=True,
        allow_delegation=False,
        tools=researcher_tools,
        llm=gemini_llm
    )

    summarizer = Agent(
        role="Content Summarizer (LM Studio)",
        goal="Create concise, structured summaries that capture the key points",
        backstory="You are a skilled editor who can extract essential insights and organize them into bullet points and summaries. You value clarity and brevity.",
        verbose=True,
        allow_delegation=False,
        tools=summarizer_tools,
        llm=lmstudio_llm
    )

    reporter = Agent(
        role="Report Generator (Gemini)",
        goal="Create polished, comprehensive reports based on summarized information",
        backstory="You are a professional writer and communicator who excels at creating well-organized, engaging reports. You focus on clarity, flow, and reader engagement.",
        verbose=True,
        allow_delegation=False,
        tools=reporter_tools,
        llm=gemini_llm
    )

    return {
        "researcher": researcher,
        "summarizer": summarizer,
        "reporter": reporter
    }
