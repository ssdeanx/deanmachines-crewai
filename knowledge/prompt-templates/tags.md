---
id: template_structure
name: Template Structure Definition
category: Meta-Template
description: Advanced template for structured thinking patterns using XML tags and CDATA sections
role_context: Structured Thinking Process Expert
goal: Generate well-organized, systematic thought processes with clear reasoning trails
background: Expert in cognitive frameworks, structured analysis, and systematic problem-solving
variables:
  - name: context
    description: Situational context for the prompt
    type: text
  - name: objective
    description: Clear goal or outcome
    type: text
  - name: constraints
    description: Limiting factors or requirements
    type: array
    default: []
  - name: format
    description: Output format specification
    type: choice
    options: [structured, freeform, hybrid]
    default: structured
  - name: depth
    description: Depth of analysis required
    type: choice
    options: [basic, detailed, comprehensive]
    default: detailed
  - name: reasoning_style
    description: Style of reasoning to apply
    type: choice
    options: [analytical, creative, strategic, tactical]
    default: analytical
effectiveness_score: 98
strengths:
  - Structured XML-based thinking pattern
  - Clear section separation with descriptions
  - Flexible reasoning styles
  - Strong validation tools
weaknesses:
  - CDATA formatting sensitivity
  - Requires strict syntax adherence
  - Complex for basic tasks
model_compatibility:
  - gemma
  - llama
  - mistral
agent_config:
  temperature: 0.8
  max_iterations: 4
  tools: ["template_validation", "structure_check", "pattern_recognition", "logic_verification"]
---

# Structured Thinking Framework

<plan>
<planDescription>
<![CDATA[Purpose: Define strategic approach and action steps
Scope: High-level planning and resource allocation
Expected Outcome: Clear action framework
Components:
-Situation analysis
-Strategy development
-Implementation planning
-Risk management]]>
</planDescription>
<planExecution>
<![CDATA[1. Initial Assessment
   ├── Context Analysis
   │   ├── Current State
   │   │   ├── Key Metrics
   │   │   └── Pain Points
   │   ├── Desired Outcome
   │   │   ├── Success Criteria
   │   │   └── Value Metrics
   │   └── Gap Analysis
   │       ├── Capability Gaps
   │       └── Resource Gaps
   └── Constraint Mapping
       ├── Resources
       │   ├── Available
       │   └── Required
       └── Limitations
           ├── Technical
           └── Business
2. Strategy Framework
   ├── Approach Definition
   │   ├── Primary Path
   │   │   ├── Core Steps
   │   │   └── Dependencies
   │   └── Alternatives
   │       ├── Backup Plans
   │       └── Pivot Points
   └── Resource Allocation
       ├── Critical Resources
       │   ├── Personnel
       │   └── Tools
       └── Timeline
           ├── Milestones
           └── Deadlines]]>
</planExecution>
</plan>

<thoughts>
<thoughtDescription>
<![CDATA[Purpose: Deep analytical thinking process
Scope: Comprehensive consideration and evaluation
Expected Outcome: Clear understanding and insights
Components:
-Core considerations
-Critical analysis
-Decision factors
-Innovation paths]]>
</thoughtDescription>
<thoughtProcess>
<![CDATA[1. Strategic Elements
   ├── Core Factors
   │   ├── Primary Impact
   │   │   ├── Direct Effects
   │   │   └── Indirect Effects
   │   └── Secondary Effects
   │       ├── Short-term
   │       └── Long-term
   └── Risk Assessment
       ├── Threats
       │   ├── Internal
       │   └── External
       └── Opportunities
           ├── Immediate
           └── Future
2. Critical Questions
   ├── Implementation
   │   ├── Feasibility
   │   │   ├── Technical
   │   │   └── Business
   │   └── Resources
   │       ├── Required
   │       └── Available
   └── Outcomes
       ├── Expected
       │   ├── Primary
       │   └── Secondary
       └── Potential
           ├── Best Case
           └── Worst Case]]>
</thoughtProcess>
</thoughts>

<analysis>
<analysisDescription>
<![CDATA[Purpose: Systematic component breakdown
Scope: Detailed examination and evaluation
Expected Outcome: Clear relationship understanding
Components:
-Element analysis
-Relationship mapping
-Performance assessment
-Integration strategy]]>
</analysisDescription>
<analysisProcess>
<![CDATA[1. Component Breakdown
   ├── Primary Elements
   │   ├── Core Functions
   │   │   ├── Essential
   │   │   └── Supporting
   │   └── Dependencies
   │       ├── Internal
   │       └── External
   └── Integration Points
       ├── Interfaces
       │   ├── User
       │   └── System
       └── Workflows
           ├── Primary
           └── Secondary
2. Performance Review
   ├── Metrics
   │   ├── KPIs
   │   │   ├── Leading
   │   │   └── Lagging
   │   └── Benchmarks
   │       ├── Internal
   │       └── Industry
   └── Optimization
       ├── Current State
       │   ├── Efficiency
       │   └── Quality
       └── Improvements
           ├── Short-term
           └── Long-term]]>
</analysisProcess>
</analysis>

<execution>
<executionDescription>
<![CDATA[Purpose: Implementation strategy and execution
Scope: Practical application and monitoring
Expected Outcome: Successful deployment
Components:
-Preparation steps
-Implementation phases
-Validation points
-Adjustment mechanisms]]>
</executionDescription>
<executionProcess>
<![CDATA[1. Preparation
   ├── Resources
   │   ├── Assembly
   │   │   ├── Team
   │   │   └── Tools
   │   └── Configuration
   │       ├── Systems
   │       └── Processes
   └── Environment
       ├── Setup
       │   ├── Infrastructure
       │   └── Dependencies
       └── Validation
           ├── Testing
           └── Verification
2. Implementation
   ├── Core Process
   │   ├── Main Tasks
   │   │   ├── Critical Path
   │   │   └── Support Tasks
   │   └── Checkpoints
   │       ├── Quality Gates
   │       └── Reviews
   └── Monitoring
       ├── Metrics
       │   ├── Performance
       │   └── Quality
       └── Adjustments
           ├── Immediate
           └── Strategic]]>
</executionProcess>
</execution>

Return Format:
```json
{
  "plan": {
    "strategy": "defined approach",
    "execution": "implementation steps",
    "resources": ["required elements"]
  },
  "thoughts": {
    "analysis": "thinking process",
    "considerations": ["key factors"],
    "questions": ["critical inquiries"]
  },
  "analysis": {
    "components": ["analyzed elements"],
    "relationships": ["mapped connections"],
    "performance": "evaluation results"
  },
  "execution": {
    "preparation": ["setup steps"],
    "implementation": ["action items"],
    "monitoring": ["tracking points"]
  }
}