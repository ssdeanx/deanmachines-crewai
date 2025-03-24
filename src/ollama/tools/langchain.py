from langchain.agents import AgentType, initialize_agent
from langchain.chains import LLMChain, AnalyzeDocumentChain
from langchain.prompts import PromptTemplate
from langchain.schema import BaseOutputParser
from langchain.output_parsers import XMLOutputParser
from langchain.memory import ConversationBufferMemory
from typing import Dict, List, Optional, Union
import xml.etree.ElementTree as ET
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

class XMLThinkingOutputParser(BaseOutputParser):
    """Parser for XML-structured thinking patterns"""
    
    def parse(self, text: str) -> Dict:
        try:
            # Clean and normalize XML
            text = text.replace("```xml", "").replace("```", "").strip()
            root = ET.fromstring(text)
            
            return {
                "structure": self._parse_section(root),
                "metadata": {
                    "timestamp": datetime.now().isoformat(),
                    "version": "1.0"
                }
            }
        except ET.ParseError as e:
            logger.error(f"XML parsing error: {str(e)}")
            return {"error": str(e)}

    def _parse_section(self, element: ET.Element) -> Dict:
        """Parse XML section recursively"""
        result = {}
        
        # Handle CDATA sections
        if element.text and "![CDATA[" in element.text:
            result["content"] = element.text.split("![CDATA[")[1].split("]]")[0].strip()
        else:
            result["content"] = element.text.strip() if element.text else ""
        
        # Parse children
        for child in element:
            if child.tag not in result:
                result[child.tag] = self._parse_section(child)
        
        return result

class StructuredThinkingChain(LLMChain):
    """Chain for structured thinking using XML patterns"""
    
    def __init__(
        self,
        llm,
        template_path: str,
        memory: Optional[ConversationBufferMemory] = None,
        verbose: bool = False
    ):
        self.template_path = template_path
        with open(template_path, 'r') as f:
            template_content = f.read()
        
        prompt = PromptTemplate(
            template=template_content,
            input_variables=["context", "objective", "constraints"],
            output_parser=XMLThinkingOutputParser()
        )
        
        super().__init__(
            llm=llm,
            prompt=prompt,
            memory=memory,
            verbose=verbose
        )

class BranchAnalysisChain(LLMChain):
    """Chain for branching analysis patterns"""
    
    def __init__(
        self,
        llm,
        branch_depth: int = 3,
        branch_width: int = 3,
        memory: Optional[ConversationBufferMemory] = None,
        verbose: bool = False
    ):
        self.branch_depth = branch_depth
        self.branch_width = branch_width
        
        template = """
        <branch_analysis>
        <context>
        {context}
        </context>
        <parameters>
        - Depth: {branch_depth}
        - Width: {branch_width}
        - Constraints: {constraints}
        </parameters>
        Generate a comprehensive branch analysis with the specified depth and width.
        </branch_analysis>
        """
        
        prompt = PromptTemplate(
            template=template,
            input_variables=["context", "branch_depth", "branch_width", "constraints"],
            output_parser=XMLThinkingOutputParser()
        )
        
        super().__init__(
            llm=llm,
            prompt=prompt,
            memory=memory,
            verbose=verbose
        )

class ResearchAnalysisChain(AnalyzeDocumentChain):
    """Chain for research analysis with XML structure"""
    
    def __init__(
        self,
        llm,
        research_depth: str = "detailed",
        source_types: List[str] = None,
        verbose: bool = False
    ):
        self.research_depth = research_depth
        self.source_types = source_types or ["academic", "industry", "case-studies"]
        
        template = """
        <research_analysis>
        <parameters>
        - Depth: {research_depth}
        - Sources: {source_types}
        - Focus: {focus_areas}
        </parameters>
        <content>
        {document}
        </content>
        Analyze the document following the specified parameters.
        </research_analysis>
        """
        
        prompt = PromptTemplate(
            template=template,
            input_variables=["document", "research_depth", "source_types", "focus_areas"],
            output_parser=XMLThinkingOutputParser()
        )
        
        super().__init__(
            llm=llm,
            prompt=prompt,
            verbose=verbose
        )

def create_structured_thinking_agent(
    llm,
    tools: List[Dict],
    template_path: str,
    memory: Optional[ConversationBufferMemory] = None,
    verbose: bool = False
) -> AgentType:
    """Create an agent specialized in structured thinking"""
    
    # Initialize chains
    structured_chain = StructuredThinkingChain(
        llm=llm,
        template_path=template_path,
        memory=memory,
        verbose=verbose
    )
    
    branch_chain = BranchAnalysisChain(
        llm=llm,
        memory=memory,
        verbose=verbose
    )
    
    # Combine tools and chains
    all_tools = tools + [
        structured_chain,
        branch_chain
    ]
    
    # Initialize agent
    agent = initialize_agent(
        tools=all_tools,
        llm=llm,
        agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
        verbose=verbose,
        memory=memory
    )
    
    return agent

def create_analysis_pipeline(
    llm,
    template_path: str,
    research_depth: str = "detailed",
    branch_depth: int = 3,
    memory: Optional[ConversationBufferMemory] = None,
    verbose: bool = False
) -> Dict[str, Union[LLMChain, AgentType]]:
    """Create a complete analysis pipeline with all chains"""
    
    structured_chain = StructuredThinkingChain(
        llm=llm,
        template_path=template_path,
        memory=memory,
        verbose=verbose
    )
    
    branch_chain = BranchAnalysisChain(
        llm=llm,
        branch_depth=branch_depth,
        memory=memory,
        verbose=verbose
    )
    
    research_chain = ResearchAnalysisChain(
        llm=llm,
        research_depth=research_depth,
        verbose=verbose
    )
    
    agent = create_structured_thinking_agent(
        llm=llm,
        tools=[],
        template_path=template_path,
        memory=memory,
        verbose=verbose
    )
    
    return {
        "structured": structured_chain,
        "branch": branch_chain,
        "research": research_chain,
        "agent": agent
    }