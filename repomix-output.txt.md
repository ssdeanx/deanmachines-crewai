# This file is a merged representation of the entire codebase, combined into a single document by Repomix

## The content has been processed where content has been formatted for parsing in markdown style, content has been compressed (code blocks are separated by ⋮---- delimiter)

## File Summary

## Purpose

This file contains a packed representation of the entire repository's contents.
It is designed to be easily consumable by AI systems for analysis, code review,
or other automated processes.

## File Format

The content is organized as follows:

1. This summary section
2. Repository information
3. Directory structure
4. Multiple file entries, each consisting of:
  a. A header with the file path (## File: path/to/file)
  b. The full contents of the file in a code block

## Usage Guidelines

- This file should be treated as read-only. Any changes should be made to the
  original repository files, not this packed version.
- When processing this file, use the file path to distinguish
  between different files in the repository.
- Be aware that this file may contain sensitive information. Handle it with
  the same level of security as you would the original repository.

## Notes

- Some files may have been excluded based on .gitignore rules and Repomix's configuration
- Binary files are not included in this packed representation. Please refer to the Repository Structure section for a complete list of file paths, including binary files
- Files matching patterns in .gitignore are excluded
- Files matching default ignore patterns are excluded
- Content has been formatted for parsing in markdown style
- Content has been compressed - code blocks are separated by ⋮---- delimiter
- Files are sorted by Git change count (files with more changes are at the bottom)

## Additional Info

# Directory Structure

```
knowledge/archive/
knowledge/categories/
mlflow-artifacts/
mlruns/.trash/
mlruns/models/
model-registry/
tests/
.env.example
.gitignore
.repomix/bundles.json
CHANGELOG.md
knowledge/categories.yaml
knowledge/config.yaml
knowledge/domain-knowledge/llm-optimization.yaml
knowledge/model-specific/gemini-pro.yaml
knowledge/prompt-templates/branch-thinking.md
knowledge/prompt-templates/code-generation.md
knowledge/prompt-templates/creative.md
knowledge/prompt-templates/meta-prompts.md
knowledge/prompt-templates/model-optimization.yaml
knowledge/prompt-templates/reasoning.md
knowledge/prompt-templates/research.md
knowledge/prompt-templates/tags.md
knowledge/prompt-templates/task-specific.md
knowledge/schemas/entry.yaml
knowledge/templates/model-capabilities.yaml
knowledge/user_preference.txt
mlruns/0/meta.yaml
mlruns/628510843323994625/meta.yaml
mlruns/628510843323994625/tags/mlflow.sharedViewState.3894e7dac091113a949e1a0b144bdfbf23f857b1cfb2b6251e919052fe25b155
New folder/current-2025-03-25T3-29pm.drawio
New folder/current-2025-03-25T5-19pm.drawio
New folder/current-2025-03-25T5-22pm.drawio
Progress.md
pyproject.toml
README.md
requirements.txt
src/ollama/__init__.py
src/ollama/config/__init__.py
src/ollama/config/agents.yaml
src/ollama/config/mlflow_config.yaml
src/ollama/config/models.yaml
src/ollama/config/search_tools.yaml
src/ollama/config/tasks.yaml
src/ollama/config/tools.yaml
src/ollama/crew.py
src/ollama/crews/model_crews.py
src/ollama/knowledge/integration.py
src/ollama/knowledge/manager.py
src/ollama/knowledge/search.py
src/ollama/main.py
src/ollama/templates/code_templates.xml
src/ollama/templates/multimodal_templates.xml
src/ollama/tools/advanced_tools.py
src/ollama/tools/agent_tools.py
src/ollama/tools/coding-tools.py
src/ollama/tools/custom_tool.py
src/ollama/tools/generation_tools.py
src/ollama/tools/langchain.py
src/ollama/tools/langgraph.py
src/ollama/tools/model_tools.py
src/ollama/tools/search_tools.py
src/ollama/tools/serperdevtool.py
src/ollama/tools/tool_factory.py
src/ollama/utils/knowledge_manager.py
src/ollama/utils/lmstudio_client.py
src/ollama/utils/mlflow_dashboard.py
src/ollama/utils/model_analyzer.py
src/ollama/utils/model_clients.py
src/ollama/utils/model_coordinator.py
src/ollama/utils/model_utils.py
src/ollama/utils/progress_tracker.py
src/ollama/utils/retry_utils.py
src/ollama/utils/template_loader.py
src/ollama/utils/webdriver_utils.py
```

# Files

## File: .repomix/bundles.json

````json
{
  "bundles": {}
}
````

## File: CHANGELOG.md

````markdown
# Changelog

All notable changes to this project will be documented in this file following [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) format.

## [Unreleased]

### Added

- Multiple model support with dynamic assignment
- Gemini Flash model integration with 1M token context
- LM Studio embedding model support
- Advanced model switching and fallback logic
- Selenium search tool integration
- Enhanced MLflow PostgreSQL tracking

### Enhanced

- Agent memory configuration with 1M token support
- Model coordination and task assignment
- Parallel processing between models
- Knowledge base with proper categorization
- Task pipeline with model-specific assignments
- Real-time performance comparison between models

### Fixed

- Model context handling for large inputs
- Memory management across different models
- Token calculation and tracking
- Task assignment logic
- Performance monitoring accuracy

## [2.1.0] - 2024-03-24

### Added

- MLflow integration for advanced performance monitoring
- Real-time dashboard with custom metrics
- Advanced validation patterns in XML processing
- Smart error recovery with context preservation
- Performance monitoring with memory tracking
- Template versioning system with metadata

### Enhanced

- Structured thinking patterns with branching analysis
- Task pipeline with parallel processing
- Agent configurations for specialized roles
- Documentation generation with Mermaid diagrams
- Dashboard visualization capabilities
- Testing framework with comprehensive metrics

### Fixed

- Memory leak in performance monitoring
- XML validation edge cases
- Template inheritance conflicts
- Task dependency resolution
- Agent communication patterns
- Dashboard data persistence

## [2.0.0] - 2024-03-20

### Added

- XML-structured thinking patterns with CDATA
- Advanced branching analysis capabilities
- Comprehensive validation framework
- Smart error recovery system
- Performance monitoring and metrics
- Template version control

### Changed

- Enhanced agent configurations
- Improved task pipeline
- Updated tool implementations
- Refined template structures

### Fixed

- CDATA formatting issues
- XML validation handling
- Branch analysis calculations
- Template inheritance bugs

## [1.0.0] - 2024-03-15

### Initial Release

- Base framework implementation
- Agent configuration system
- Task management framework
- File output capabilities
- Basic template system
- Documentation structure
````

## File: knowledge/config.yaml

````yaml
# Knowledge Base Configuration
storage:
  base_path: "./knowledge"
  index_type: "simple"
  formats:
    - md
    - json
    - yaml
    - txt

categories:
  - name: prompt-templates
    description: "Structured prompting patterns and templates"
    subcategories:
      - reasoning
      - research
      - creative
      - technical
      - meta
  - name: model-specific
    description: "Model-specific knowledge and capabilities"
    subcategories:
      - gemini
      - llama
      - mistral
  - name: domain-knowledge
    description: "Specialized domain information"
    subcategories:
      - machine-learning
      - software-engineering
      - data-science
  - name: best-practices
    description: "Guidelines and recommended practices"
    subcategories:
      - code
      - architecture
      - testing
      - deployment

indexing:
  update_frequency: "daily"
  max_file_size: 10485760  # 10MB
  exclude_patterns:
    - "*.tmp"
    - "*.log"
    - "*.bak"

validation:
  schema_validation: true
  content_validation: true
  format_validation: true
  relationship_validation: true

relationships:
  enable_cross_references: true
  track_dependencies: true
  maintain_hierarchy: true

caching:
  enabled: true
  max_size: 1073741824  # 1GB
  ttl: 3600  # 1 hour
````

## File: knowledge/domain-knowledge/llm-optimization.yaml

````yaml
id: llm-optimization
name: "LLM Optimization Techniques"
category: "domain-knowledge"
description: "Comprehensive guide to optimizing large language model performance and output quality"

variables:
  - name: model_type
    description: Type of LLM being optimized
    type: choice
    options: [transformer, mixture-of-experts, sparse]
  - name: optimization_target
    description: Primary optimization goal
    type: choice
    options: [latency, throughput, quality, memory]
  - name: deployment_context
    description: Deployment environment details
    type: object

effectiveness_score: 95
use_cases:
  - Performance optimization
  - Resource utilization
  - Quality improvement
  - Cost reduction

key_concepts:
  architectural:
    - name: "Model Parallelism"
      description: "Splitting model across multiple devices"
      impact_score: 9
    - name: "Quantization"
      description: "Reducing numerical precision"
      impact_score: 8
    - name: "Pruning"
      description: "Removing unnecessary weights"
      impact_score: 7

  operational:
    - name: "Batching"
      description: "Processing multiple requests together"
      impact_score: 9
    - name: "Caching"
      description: "Storing frequent responses"
      impact_score: 8
    - name: "Request Optimization"
      description: "Optimizing input processing"
      impact_score: 7

implementation_patterns:
  - pattern: "Token Streaming"
    description: "Stream tokens for faster response"
    code_example: |
      async for token in model.stream(prompt):
          yield token

  - pattern: "Batch Processing"
    description: "Process multiple prompts efficiently"
    code_example: |
      results = model.generate_batch(prompts, batch_size=16)

best_practices:
  - "Implement proper error handling"
  - "Monitor resource utilization"
  - "Use appropriate batch sizes"
  - "Enable response streaming"
  - "Implement retry mechanisms"

optimization_metrics:
  - metric: "Latency"
    unit: "ms"
    target_range: "50-200"
  - metric: "Throughput"
    unit: "requests/second"
    target_range: "10-100"
  - metric: "Memory Usage"
    unit: "GB"
    target_range: "8-32"

model_compatibility:
  - gemini
  - llama
  - mistral

related_topics:
  - "model-quantization"
  - "parallel-processing"
  - "cache-strategies"
  - "load-balancing"
````

## File: knowledge/model-specific/gemini-pro.yaml

````yaml
model_id: "gemini-pro"
version: "2.5-pro-exp-03-25"
base_model: "gemini"
capabilities:
  text_generation: true
  chat: true
  code: true
  vision: false
  embedding: true

context_window: 1000000  # 1M tokens
max_tokens: 64000
supported_languages:
  - python
  - javascript
  - typescript
  - go
  - java
  - cpp
  - rust

performance_metrics:
  throughput: 150  # tokens/second
  latency: 0.8    # seconds
  memory_usage: 16 # GB

quantization_options:
  - float16
  - int8
  - int4

deployment:
  platforms:
    - cloud
    - api
  requirements:
    api_key: required
    rate_limits: true
    concurrent_requests: 100

fine_tuning:
  supported: false
  methods: []

best_practices:
  - category: "performance"
    recommendations:
      - "Use structured prompts for better responses"
      - "Enable response streaming for faster results"
      - "Implement proper error handling and retry logic"
      - "Cache frequently used prompts and responses"
  - category: "quality"
    recommendations:
      - "Use chain-of-thought prompting for complex tasks"
      - "Implement validation for generated content"
      - "Set appropriate temperature for the task"
      - "Use system prompts to define behavior"

limitations:
  - "Knowledge cutoff: January 2025"
  - "No fine-tuning support"
  - "Rate limits apply"
  - "Output token limits"

optimization_tips:
  - "Use parallel processing for multiple requests"
  - "Implement proper caching strategies"
  - "Monitor and adjust temperature settings"
  - "Break large tasks into smaller chunks"

integration_guides:
  - platform: "Python"
    guide: "Use google.generativeai package"
    examples:
      - "Text generation"
      - "Chat completion"
      - "Code generation"
  - platform: "REST API"
    guide: "Direct API integration"
    examples:
      - "Authentication"
      - "Request formatting"
      - "Response handling"

metadata:
  created_at: "2024-03-25T00:00:00Z"
  updated_at: "2024-03-25T00:00:00Z"
  version: "1.0.0"
  author: "system"
  tags:
    - "large-language-model"
    - "text-generation"
    - "code-generation"
    - "enterprise"
````

## File: knowledge/prompt-templates/branch-thinking.md

````markdown
---
id: branch-thinking-framework
name: Branch Thinking Analysis Framework
category: Advanced Analysis
description: Template for exploring multiple solution paths and decision branches with comprehensive analysis of each branch
role_context: Expert Decision Tree Analyst
goal: Develop comprehensive branched analysis with evaluation of multiple paths and outcomes
background: Extensive experience in decision analysis, scenario planning, and systematic branch exploration
variables:
  - name: initial_scenario
    description: Starting point for analysis
    type: text
  - name: branch_depth
    description: How many levels deep to explore
    type: number
    default: 3
  - name: branch_width
    description: Maximum number of alternatives per node
    type: number
    default: 3
  - name: evaluation_criteria
    description: Criteria for evaluating branches
    type: array
    default: ["feasibility", "impact", "resource_requirements"]
  - name: confidence_threshold
    description: Minimum confidence level for including a branch
    type: number
    default: 0.7
  - name: optimization_goal
    description: What to optimize for in the analysis
    type: choice
    options: [efficiency, reliability, innovation, cost, speed]
    default: efficiency
  - name: context_constraints
    description: Limiting factors to consider
    type: array
    default: []
  - name: insight_depth
    description: Level of insight analysis required
    type: choice
    options: [basic, detailed, comprehensive]
    default: detailed
  - name: crossref_sources
    description: External knowledge bases to cross-reference
    type: array
    default: ["domain_knowledge", "historical_cases", "best_practices"]
effectiveness_score: 95
use_cases:
  - Decision analysis
  - Strategy planning
  - Risk assessment
  - Solution exploration
  - Alternative analysis
limitations:
  - Complexity increases exponentially with depth
  - Requires clear evaluation criteria
  - May need domain-specific expertise
model_compatibility:
  - gemma
  - llama
  - mistral
agent_config:
  temperature: 0.8
  max_iterations: 4
  tools: ["branch_analysis", "probability_calculation", "decision_mapping", "insight_generation", "cross_reference"]
---

# Branch Thinking Framework

You are an Expert Decision Tree Analyst specializing in comprehensive branch analysis.

### Initial Context
Scenario: {initial_scenario}
Depth: {branch_depth} levels
Width: {branch_width} alternatives per node
Optimization Goal: {optimization_goal}
Insight Depth: {insight_depth}

### Analysis Structure

1. Root Analysis
   - Initial scenario assessment
   - Key variables identification
   - Constraint mapping: {context_constraints}

2. Branch Development
   ```
   [Root] {initial_scenario}
   ├── Branch A
   │   ├── Sub-branch A1
   │   └── Sub-branch A2
   ├── Branch B
   │   ├── Sub-branch B1
   │   └── Sub-branch B2
   └── Branch C
       ├── Sub-branch C1
       └── Sub-branch C2
   ```

3. Branch Evaluation
   For each branch:
   - Feasibility Score (0-1)
   - Impact Assessment
   - Resource Requirements
   - Risk Factors
   - Confidence Level

4. Cross-Branch Analysis
   - Interdependencies
   - Mutual exclusivity
   - Synergy opportunities
   - Resource conflicts

5. Optimization Analysis
   - Path optimization for {optimization_goal}
   - Resource allocation
   - Timeline considerations
   - Risk mitigation strategies

6. Insight Generation
   - Pattern recognition
   - Hidden dependencies
   - Emerging opportunities
   - Risk correlations
   - Strategic implications

7. Cross-Reference Analysis
   Sources: {crossref_sources}
   - Historical precedents
   - Domain best practices
   - Similar case studies
   - Expert recommendations
   - Industry standards

### Quality Criteria
1. Evaluation Standards
   - Minimum confidence: {confidence_threshold}
   - Evidence requirements
   - Validation methods

2. Branch Quality Checks
   - Completeness
   - Consistency
   - Independence
   - Relevance

Return Format:
```json
{
  "analysis_tree": {
    "root": "initial scenario",
    "branches": [
      {
        "path": "branch description",
        "sub_branches": [],
        "evaluation": {
          "feasibility": 0.0,
          "impact": "impact description",
          "resources": ["required resources"],
          "confidence": 0.0
        }
      }
    ]
  },
  "insights": {
    "patterns": ["identified patterns"],
    "hidden_dependencies": ["discovered dependencies"],
    "opportunities": ["emerging opportunities"],
    "risks": ["correlated risks"],
    "strategic_implications": ["key implications"]
  },
  "cross_references": {
    "historical_matches": ["relevant cases"],
    "best_practices": ["applicable practices"],
    "expert_insights": ["expert recommendations"],
    "standards_alignment": ["relevant standards"]
  },
  "recommendations": {
    "optimal_paths": ["path1", "path2"],
    "risk_factors": ["risk1", "risk2"],
    "implementation_notes": "strategic guidance"
  },
  "meta_analysis": {
    "branch_coverage": "coverage metrics",
    "confidence_distribution": "confidence analysis",
    "resource_optimization": "resource allocation strategy"
  }
}
````

## File: knowledge/prompt-templates/code-generation.md

````markdown
---
id: advanced-code-generator
name: Advanced Code Generation Specialist
category: Development
description: Advanced template for generating high-quality code with architecture patterns and testing
role_context: Senior Software Architect and Developer
goal: Generate production-ready code with proper architecture and testing
background: Extensive experience in software architecture, design patterns, and test-driven development
variables:
  - name: language
    description: Programming language to use
    type: text
  - name: task_description
    description: What the code should do
    type: text
  - name: architecture_style
    description: Desired architecture pattern
    type: choice
    options: [modular, layered, microservices, event-driven, hexagonal]
    default: modular
  - name: design_patterns
    description: Design patterns to incorporate
    type: array
    default: []
  - name: code_style
    description: Coding style guidelines
    type: object
    properties:
      formatting: string
      conventions: string
      complexity_limit: number
  - name: testing_requirements
    description: Testing specifications
    type: object
    properties:
      unit_tests: boolean
      integration_tests: boolean
      coverage_threshold: number
      test_framework: string
  - name: documentation_level
    description: Level of documentation detail
    type: choice
    options: [minimal, standard, comprehensive]
    default: standard
  - name: performance_requirements
    description: Performance criteria
    type: object
    properties:
      time_complexity: string
      space_complexity: string
      optimization_level: number
effectiveness_score: 95
use_cases:
  - Complex system design
  - Microservice implementation
  - API development
  - Performance-critical components
  - Test suite generation
limitations:
  - Requires detailed specifications
  - Language-specific optimizations needed
  - Complex architecture patterns need context
model_compatibility:
  - gemma
  - llama
  - mistral
agent_config:
  temperature: 0.7
  max_iterations: 5
  tools: ["code_analysis", "test_generation", "documentation"]
---

# Advanced Code Generation Template

You are a Senior Software Architect and Developer specializing in {language} with expertise in {architecture_style} architecture.

### Context
Task Description: {task_description}
Architecture Style: {architecture_style}
Design Patterns: {design_patterns}
Performance Requirements:
- Time Complexity: {performance_requirements.time_complexity}
- Space Complexity: {performance_requirements.space_complexity}

### Design Phase
1. System Architecture
   - Component diagram
   - Interaction flows
   - Data structures
   - API contracts

2. Implementation Design
   - Class/module structure
   - Interface definitions
   - Design pattern implementation
   - Error handling strategy

3. Code Implementation
   ```{language}
   // Implementation here with proper structure
   ```

4. Testing Strategy
{testing_requirements.unit_tests ? """
   Unit Tests:
   - Test cases
   - Edge cases
   - Mocking strategy
   - Coverage requirements: {testing_requirements.coverage_threshold}%
""" : ""}
{testing_requirements.integration_tests ? """
   Integration Tests:
   - Service integration
   - System workflows
   - Performance benchmarks
""" : ""}

5. Documentation ({documentation_level})
   - API documentation
   - Implementation details
   - Usage examples
   - Performance considerations
   - Deployment notes

### Quality Requirements
1. Code Style
   - Follow: {code_style.formatting}
   - Maximum complexity: {code_style.complexity_limit}
   - Naming conventions: {code_style.conventions}

2. Performance Optimization
   - Optimization level: {performance_requirements.optimization_level}
   - Resource usage considerations
   - Scalability factors

3. Error Handling
   - Exception hierarchy
   - Recovery strategies
   - Logging requirements

Return Format:
```json
{
  "design": {
    "architecture": "detailed architecture description",
    "components": ["list of components"],
    "interfaces": ["interface definitions"]
  },
  "implementation": {
    "code": "actual code implementation",
    "tests": "test suite code",
    "documentation": "comprehensive documentation"
  },
  "quality_metrics": {
    "complexity": "analysis",
    "coverage": "percentage",
    "performance": "benchmarks"
  }
}
````

## File: knowledge/prompt-templates/creative.md

````markdown
---
id: advanced_creative_framework
name: Advanced Creative Content Generator
category: Creative Generation
description: Sophisticated framework for generating creative content with advanced control parameters and style management
variables:
  - name: content_type
    description: Specific type of creative content
    type: choice
    options: [narrative, marketing, technical, visual-description, dialogue]
  - name: creative_parameters
    description: Advanced creative control settings
    type: object
    properties:
      tone:
        type: choice
        options: [professional, casual, academic, poetic, technical]
      style:
        type: choice
        options: [descriptive, concise, elaborate, metaphorical]
      complexity:
        type: number
        range: [1-10]
      innovation_level:
        type: choice
        options: [conventional, moderate, experimental]
  - name: audience_data
    description: Detailed audience characteristics
    type: object
    properties:
      expertise_level: [beginner, intermediate, expert]
      industry_focus: string
      cultural_context: string
  - name: format_requirements
    description: Specific formatting and structure requirements
    type: object
effectiveness_score: 92
use_cases:
  - Marketing campaigns
  - Technical documentation
  - Story development
  - Product descriptions
  - Educational content
  - Brand messaging
  - UX writing
limitations:
  - Style consistency in long-form content
  - Cultural nuance handling
  - Technical accuracy in specialized fields
model_compatibility:
  - gemma
  - llama
  - mistral
---

# Creative Framework Template

### Context Initialization
Content Type: {content_type}
Innovation Level: {creative_parameters.innovation_level}
Audience: {audience_data.expertise_level} in {audience_data.industry_focus}

### Style Configuration
Tone: {creative_parameters.tone}
Style: {creative_parameters.style}
Complexity: {creative_parameters.complexity}
Cultural Context: {audience_data.cultural_context}

### Content Structure

1. Opening Component
   - Hook development
   - Context setting
   - Tone establishment

2. Core Content Development
   - Primary message articulation
   - Supporting elements
   - Engagement mechanisms
   - Flow management

3. Enhancement Elements
   - Sensory details
   - Emotional resonance
   - Audience connection points
   - Cultural relevance markers

4. Technical Requirements
   - Format: {format_requirements}
   - Structure: Hierarchical with clear progression
   - Engagement: Interactive elements where appropriate
   - Accessibility: Universal design principles

5. Quality Assurance
   - Style consistency check
   - Tone alignment verification
   - Cultural sensitivity review
   - Technical accuracy validation

### Output Specifications

1. Primary Content Block
2. Alternative Versions
3. Enhancement Suggestions

# Example Usage

Input variables:
```yaml
content_type: "marketing"
creative_parameters:
  tone: "professional"
  style: "descriptive"
  complexity: 7
  innovation_level: "moderate"
audience_data:
  expertise_level: "intermediate"
  industry_focus: "technology"
  cultural_context: "global tech community"
format_requirements:
  structure: "modular"
  length: "medium"
  special_elements: ["metaphors", "technical analogies"]
````

## File: knowledge/prompt-templates/meta-prompts.md

````markdown
---
id: meta-prompt-optimization
name: Meta-Prompt Performance Optimizer
category: Meta-Prompting
description: Template for creating and optimizing other prompts with advanced control and validation mechanisms
role_context: Expert Prompt Engineer and System Architect
goal: Design and optimize high-performance prompts for specific tasks and models
background: Extensive experience in prompt engineering, system architecture, and performance optimization
variables:
  - name: target_task
    description: The specific task the prompt should accomplish
    type: text
  - name: complexity_level
    description: Desired complexity level
    type: choice
    options: [basic, intermediate, advanced]
    default: intermediate
  - name: model_name
    description: Target language model
    type: choice
    options: [gemma, llama, mistral]
    default: gemma
  - name: architecture_type
    description: Prompt architecture pattern
    type: choice
    options: [simple, chain, tree, recursive]
    default: simple
  - name: performance_metrics
    description: Key metrics to optimize
    type: object
    properties:
      accuracy: number
      consistency: number
      response_time: string
  - name: validation_criteria
    description: Success criteria for the prompt
    type: array
    default: ["output_format", "content_quality", "edge_cases"]
  - name: output_format
    description: Required response structure
    type: object
    properties:
      style: string
      structure: string
      validation: boolean
effectiveness_score: 95
use_cases:
  - Prompt optimization
  - System design
  - Agent behavior definition
  - Chain-of-thought development
  - Response quality improvement
limitations:
  - Requires clear task definition
  - Model-specific optimizations needed
  - Complex validation requirements
model_compatibility:
  - gemma
  - llama
  - mistral
agent_config:
  temperature: 0.7
  max_iterations: 4
  tools: ["prompt_testing", "performance_analysis", "validation"]
---

# Meta-Prompt Optimization Framework

You are an Expert Prompt Engineer specializing in {model_name} optimization with focus on {complexity_level} tasks.

### Context
Task: {target_task}
Architecture: {architecture_type}
Performance Goals: {performance_metrics}

### Design Process

1. Task Analysis
   - Requirements breakdown
   - Constraint identification
   - Success criteria definition
   - Edge case mapping

2. Architecture Design
   - Component structure
   - Interaction patterns
   - Control mechanisms
   - Validation points

3. Prompt Engineering
   - Core instructions
   - Context setting
   - Parameter handling
   - Output formatting
   - Error management

4. Optimization Strategy
   - Performance tuning
   - Response quality
   - Consistency checks
   - Resource efficiency

5. Validation Framework
   - Success metrics: {validation_criteria}
   - Quality assurance
   - Edge case handling
   - Performance monitoring

### Implementation Guide

1. Base Structure
   ```text
   System: [Role and Context]
   Task: [Clear Objective]
   Parameters: [Key Variables]
   Instructions: [Step-by-Step Guide]
   Validation: [Quality Checks]
   Output: [Format Specification]
   ```

2. Control Mechanisms
   - Input validation
   - Process monitoring
   - Output verification
   - Error handling

3. Quality Assurance
   - Consistency checks
   - Performance metrics
   - Validation rules
   - Success criteria

Return Format:
```json
{
  "prompt_design": {
    "structure": "prompt architecture details",
    "components": ["list of components"],
    "control_flow": "interaction patterns"
  },
  "implementation": {
    "base_prompt": "core prompt text",
    "variations": ["context-specific variations"],
    "validation": ["validation rules"]
  },
  "optimization": {
    "performance_metrics": "metric values",
    "quality_scores": "quality assessments",
    "improvement_areas": ["optimization targets"]
  },
  "documentation": {
    "usage_guide": "implementation notes",
    "examples": ["example uses"],
    "limitations": ["known constraints"]
  }
}
````

## File: knowledge/prompt-templates/model-optimization.yaml

````yaml
id: model-optimization
name: Model Performance Optimization
category: Technical
description: Template for optimizing model performance and resource utilization
variables:
  - name: model_name
    description: Name of the model to optimize
    type: text
  - name: performance_target
    description: Primary optimization goal
    type: choice
    options: [latency, throughput, memory, quality]
    default: latency
  - name: resource_constraints
    description: Available system resources
    type: object
    properties:
      max_memory: number
      max_concurrent: number
  - name: batch_settings
    description: Batch processing configuration
    type: object
    properties:
      enabled: boolean
      size: number
      timeout: number
  - name: streaming
    description: Enable response streaming
    type: boolean
    default: true

effectiveness_score: 92
use_cases:
  - Production deployment optimization
  - Resource utilization improvement
  - Response time optimization
  - Quality-performance balance

template: |
  System: You are an expert in {model_name} optimization with deep understanding of model behavior and system resources.

  Objective: Optimize model performance for {performance_target} while respecting resource constraints:
  - Max Memory: {resource_constraints.max_memory}GB
  - Max Concurrent Requests: {resource_constraints.max_concurrent}

  Consider the following aspects:

  1. Resource Management:
     - Memory allocation strategies
     - CPU/GPU utilization patterns
     - Cache management approaches
     - Request queuing mechanisms

  2. Processing Optimization:
     {% if batch_settings.enabled %}
     - Batch processing configuration:
       * Batch size: {batch_settings.size}
       * Timeout: {batch_settings.timeout}ms
     {% endif %}
     {% if streaming %}
     - Streaming optimization:
       * Token delivery patterns
       * Buffer management
       * Client connection handling
     {% endif %}

  3. Quality Controls:
     - Response validation
     - Error handling
     - Fallback strategies
     - Monitoring points

  Provide specific optimization recommendations following this structure:
  ```json
  {
    "configuration": {
      "memory_settings": {},
      "processing_settings": {},
      "quality_controls": {}
    },
    "implementation": {
      "code_examples": [],
      "monitoring_setup": {},
      "fallback_strategy": {}
    },
    "validation": {
      "success_metrics": [],
      "warning_signs": [],
      "monitoring_points": []
    }
  }
  ```

model_compatibility:
  - gemini
  - llama
  - mistral

limitations:
  - Model-specific optimizations may vary
  - Resource measurements needed
  - Requires system-level access
````

## File: knowledge/prompt-templates/reasoning.md

````markdown
---
id: analytical-reasoning
name: Analytical Reasoning Framework
category: Problem-Solving
description: Template for complex problem analysis and solution development
role_context: Expert Analytical Reasoner
goal: Provide comprehensive problem analysis and solution development
background: Extensive experience in systematic problem-solving and decision analysis
variables:
  - name: problem_domain
    description: Specific area of focus
    type: text
  - name: analysis_depth
    description: How deep to analyze (surface, detailed, comprehensive)
    type: choice
    default: detailed
  - name: structured_output
    description: How to structure the response
    type: text
  - name: task_context
    description: Additional context from previous tasks
    type: text
    default: ""
  - name: chain_results
    description: Results from previous chain steps
    type: array
    default: []
effectiveness_score: 90
use_cases:
  - Complex problem solving
  - Decision analysis
  - Strategy development
limitations:
  - Requires clear problem definition
  - May need domain expertise
model_compatibility:
  - gemma
  - llama
  - mistral
agent_config:
  temperature: 0.7
  max_iterations: 3
  tools: ["research", "analyze", "summarize"]
---

# Reasoning Template

You are an Expert Analytical Reasoner with deep experience in problem-solving and decision analysis.

Context: You are analyzing a problem in {problem_domain} at {analysis_depth} level.
Previous Context: {task_context}
Chain Results: {chain_results}

Approach:

1. Problem Definition
   - Clear statement of the problem
   - Key constraints and requirements
   - Integration with previous findings

2. Analysis Framework
   - Break down into components
   - Identify relationships
   - Map dependencies
   - Consider cross-task implications

3. Solution Development
   - Generate alternatives
   - Evaluate options
   - Select optimal approach
   - Validate against previous results

4. Implementation Strategy
   - Step-by-step plan
   - Resource requirements
   - Timeline and milestones
   - Integration points

5. Chain Integration
   - Connect with previous analyses
   - Prepare outputs for next steps
   - Document dependencies

Output your analysis in {structured_output} format.

Return Format:
{
  "analysis": "detailed analysis here",
  "recommendations": ["list", "of", "recommendations"],
  "next_steps": ["subsequent", "actions"],
  "chain_data": {"key": "data for next agent"}
}
````

## File: knowledge/prompt-templates/research.md

````markdown
---
id: advanced-research
name: Advanced Research Framework
category: Research
description: Comprehensive template for conducting in-depth research and analysis across multiple domains
role_context: Expert Research Analyst
goal: Conduct thorough research and provide well-structured insights
background: Extensive experience in academic and industry research methodologies
variables:
  - name: research_topic
    description: Main subject of research
    type: text
  - name: research_depth
    description: How deep to investigate
    type: choice
    options: [overview, detailed, comprehensive]
    default: detailed
  - name: source_types
    description: Types of sources to consider
    type: array
    default: ["academic", "industry", "case-studies"]
  - name: time_range
    description: Temporal scope of research
    type: object
    properties:
      start_year: number
      end_year: number
      default: current_year
  - name: focus_areas
    description: Specific aspects to emphasize
    type: array
    default: []
  - name: output_format
    description: How to structure the findings
    type: choice
    options: [summary, detailed-report, analytical-breakdown]
    default: detailed-report
  - name: cross_references
    description: Related research to consider
    type: array
    default: []
effectiveness_score: 95
use_cases:
  - Academic research
  - Market analysis
  - Technical investigation
  - Trend analysis
  - Literature review
limitations:
  - Source availability constraints
  - Time-sensitive information
  - Domain expertise requirements
model_compatibility:
  - gemma
  - llama
  - mistral
agent_config:
  temperature: 0.7
  max_iterations: 4
  tools: ["web_search", "document_analysis", "citation_check"]
---

# Research Framework

You are an Expert Research Analyst with extensive experience in systematic research methodologies.

### Context
Topic: {research_topic}
Depth: {research_depth}
Time Range: {time_range.start_year} to {time_range.end_year}
Focus Areas: {focus_areas}

### Research Process

1. Initial Assessment
   - Topic scope definition
   - Research questions formulation
   - Methodology selection
   - Source identification: {source_types}

2. Data Collection
   - Primary source gathering
   - Secondary source analysis
   - Cross-reference verification
   - Source quality assessment

3. Analysis Framework
   - Data categorization
   - Pattern identification
   - Gap analysis
   - Cross-validation

4. Synthesis
   - Key findings extraction
   - Relationship mapping
   - Insight development
   - Evidence correlation

5. Validation
   - Source verification
   - Fact-checking
   - Bias assessment
   - Consistency review

6. Documentation
   - Findings organization
   - Citation management
   - Evidence linking
   - Context preservation

Output your research in {output_format} format.

Return Format:
```json
{
  "research_summary": {
    "key_findings": ["list of main findings"],
    "evidence": ["supporting evidence"],
    "sources": ["cited sources"]
  },
  "analysis": {
    "patterns": ["identified patterns"],
    "gaps": ["research gaps"],
    "implications": ["key implications"]
  },
  "recommendations": {
    "next_steps": ["suggested actions"],
    "further_research": ["areas for investigation"]
  },
  "metadata": {
    "confidence_level": "0-1 score",
    "completeness": "coverage assessment",
    "limitations": ["noted constraints"]
  }
}
````

## File: knowledge/prompt-templates/tags.md

````markdown
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
````

## File: knowledge/prompt-templates/task-specific.md

````markdown
---
id: template_id
name: Template Name
category: Category
description: Description of what this prompt template does
variables:
  - name: variable_name
    description: what this variable is for
    type: text|number|choice
    default: default value (optional)
effectiveness_score: 0-100
use_cases:
  - use case 1
  - use case 2
limitations:
  - limitation 1
  - limitation 2
model_compatibility:
  - gemma
  - llama
  - mistral
---

# Prompt Template

{your_variable} Your prompt text here with {variables} in curly braces

# Example Usage

Input variables:
````

## File: knowledge/schemas/entry.yaml

````yaml
type: object
required:
  - id
  - name
  - category
  - description
properties:
  id:
    type: string
    pattern: ^[a-z0-9-_]+$
  name:
    type: string
    minLength: 3
  category:
    type: string
    enum:
      - prompt-templates
      - model-specific
      - domain-knowledge
      - best-practices
  description:
    type: string
    minLength: 10
  variables:
    type: array
    items:
      type: object
      required:
        - name
        - description
        - type
      properties:
        name:
          type: string
        description:
          type: string
        type:
          type: string
          enum:
            - text
            - number
            - choice
            - array
            - object
        default:
          type: [string, number, array, object, "null"]
  effectiveness_score:
    type: number
    minimum: 0
    maximum: 100
  use_cases:
    type: array
    items:
      type: string
  limitations:
    type: array
    items:
      type: string
  model_compatibility:
    type: array
    items:
      type: string
      enum:
        - gemini
        - llama
        - mistral
  agent_config:
    type: object
    properties:
      temperature:
        type: number
        minimum: 0
        maximum: 1
      max_iterations:
        type: integer
        minimum: 1
      tools:
        type: array
        items:
          type: string
  metadata:
    type: object
    properties:
      created_at:
        type: string
        format: date-time
      updated_at:
        type: string
        format: date-time
      version:
        type: string
      author:
        type: string
      tags:
        type: array
        items:
          type: string
  relationships:
    type: object
    properties:
      dependencies:
        type: array
        items:
          type: string
      related_entries:
        type: array
        items:
          type: string
      parent_category:
        type: string
      subcategory:
        type: string
````

## File: knowledge/templates/model-capabilities.yaml

````yaml
type: object
required:
  - model_id
  - version
  - capabilities
properties:
  model_id:
    type: string
  version:
    type: string
  base_model:
    type: string
  capabilities:
    type: object
    properties:
      text_generation:
        type: boolean
      chat:
        type: boolean
      code:
        type: boolean
      vision:
        type: boolean
      embedding:
        type: boolean
  context_window:
    type: integer
  max_tokens:
    type: integer
  supported_languages:
    type: array
    items:
      type: string
  performance_metrics:
    type: object
    properties:
      throughput:
        type: number
      latency:
        type: number
      memory_usage:
        type: number
  quantization_options:
    type: array
    items:
      type: string
  deployment:
    type: object
    properties:
      platforms:
        type: array
        items:
          type: string
      requirements:
        type: object
  fine_tuning:
    type: object
    properties:
      supported:
        type: boolean
      methods:
        type: array
        items:
          type: string
  best_practices:
    type: array
    items:
      type: object
      properties:
        category:
          type: string
        recommendations:
          type: array
          items:
            type: string
  limitations:
    type: array
    items:
      type: string
  optimization_tips:
    type: array
    items:
      type: string
  integration_guides:
    type: array
    items:
      type: object
      properties:
        platform:
          type: string
        guide:
          type: string
        examples:
          type: array
          items:
            type: string
````

## File: knowledge/user_preference.txt

````
User name is John Doe.
User is an AI Engineer.
User is interested in AI Agents.
User is based in San Francisco, California.
````

## File: mlruns/0/meta.yaml

````yaml
artifact_location: mlflow-artifacts:/0
creation_time: 1742860362940
experiment_id: '0'
last_update_time: 1742860362940
lifecycle_stage: active
name: Default
````

## File: mlruns/628510843323994625/meta.yaml

````yaml
artifact_location: file:C:/Users/dm/Documents/ollama/mlflow-artifacts
creation_time: 1742860435637
experiment_id: '628510843323994625'
last_update_time: 1742860435637
lifecycle_stage: active
name: ollama_crew_monitoring
````

## File: mlruns/628510843323994625/tags/mlflow.sharedViewState.3894e7dac091113a949e1a0b144bdfbf23f857b1cfb2b6251e919052fe25b155

````
deflate;eJxdUtFO4zAQ/JWTnysEr3kLpdwhWoRSqE6qTq1rb8lKjh1519Ac6r+zbgIpPO7szOx61u+KQEdT36JjiKpQaqJCtBCvu3vopNbMEXeJgS6IdeQNYwMjqSSjir12BBN16j/ldqHK+VxIDvdgOuPgy740jK9ZbzVrAqbPzvrfRDXBgltBJAx+VDj3q0qeREPgwDDYaXCpEaRYn6+3XYYUDWyFeI4usin9RG/68VslY6O4zw6t9hasKt6PPfKI3ud6PTD+oLXgx3qFhDt0yN1Ct6Osp+WhsvvtXbV82lxdbqrnh6Vs8IrwttAHbPB/th5yE9kciT8HDChSaYykLFlUcEr7TJIIfseQWrAr7RLQnZ/WEr5EwjFJv0YLs6bl7jv8kjXXclafnBvKH0/XiUMF+whUz7zeuYwPYhd22s3Rw8l0GvweX0SkDuUBqf8txNCe7u5h2YTAtQeS6Zfj7f5m8gLkEqaXqOPxA/ej5lc=
````

## File: New folder/current-2025-03-25T3-29pm.drawio

````
<?xml version="1.0" encoding="UTF-8"?>
      <mxfile host="codeviz.app" modified="2025-03-25T19:29:21.244Z" agent="CodeViz Exporter" version="14.6.5" type="device">
        <diagram id="codeviz-diagram" name="System Diagram">
          <mxGraphModel dx="1000" dy="1000" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1169" pageHeight="827" math="0" shadow="0">
            <root>
              <mxCell id="0"/>
              <mxCell id="1" parent="0"/>
              <mxCell id="subGraph4" value="" style="html=1;whiteSpace=wrap;container=1;fillColor=#dae8fc;strokeColor=#6c8ebf;dashed=1;fillOpacity=20;strokeWidth=2;containerType=none;recursiveResize=0;movable=1;resizable=1;autosize=0;dropTarget=0" vertex="1" parent="1">
                <mxGeometry x="873" y="687" width="520" height="220" as="geometry"/>
              </mxCell>
              <mxCell id="subGraph4_label" value="Core Processing" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;labelBackgroundColor=white;spacing=5" vertex="1" parent="1">
                <mxGeometry x="881" y="695" width="444" height="24" as="geometry"/>
              </mxCell>
<mxCell id="subGraph3" value="" style="html=1;whiteSpace=wrap;container=1;fillColor=#dae8fc;strokeColor=#6c8ebf;dashed=1;fillOpacity=20;strokeWidth=2;containerType=none;recursiveResize=0;movable=1;resizable=1;autosize=0;dropTarget=0" vertex="1" parent="1">
                <mxGeometry x="902" y="359.5" width="461" height="300" as="geometry"/>
              </mxCell>
              <mxCell id="subGraph3_label" value="Tools Integration" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;labelBackgroundColor=white;spacing=5" vertex="1" parent="1">
                <mxGeometry x="910" y="367.5" width="385" height="24" as="geometry"/>
              </mxCell>
<mxCell id="subGraph2" value="" style="html=1;whiteSpace=wrap;container=1;fillColor=#dae8fc;strokeColor=#6c8ebf;dashed=1;fillOpacity=20;strokeWidth=2;containerType=none;recursiveResize=0;movable=1;resizable=1;autosize=0;dropTarget=0" vertex="1" parent="1">
                <mxGeometry x="532" y="352" width="380" height="300" as="geometry"/>
              </mxCell>
              <mxCell id="subGraph2_label" value="MLflow Monitoring" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;labelBackgroundColor=white;spacing=5" vertex="1" parent="1">
                <mxGeometry x="540" y="360" width="304" height="24" as="geometry"/>
              </mxCell>
<mxCell id="subGraph1" value="" style="html=1;whiteSpace=wrap;container=1;fillColor=#dae8fc;strokeColor=#6c8ebf;dashed=1;fillOpacity=20;strokeWidth=2;containerType=none;recursiveResize=0;movable=1;resizable=1;autosize=0;dropTarget=0" vertex="1" parent="1">
                <mxGeometry x="22" y="352" width="520" height="320" as="geometry"/>
              </mxCell>
              <mxCell id="subGraph1_label" value="Knowledge Management" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;labelBackgroundColor=white;spacing=5" vertex="1" parent="1">
                <mxGeometry x="30" y="360" width="444" height="24" as="geometry"/>
              </mxCell>
<mxCell id="subGraph0" value="" style="html=1;whiteSpace=wrap;container=1;fillColor=#dae8fc;strokeColor=#6c8ebf;dashed=1;fillOpacity=20;strokeWidth=2;containerType=none;recursiveResize=0;movable=1;resizable=1;autosize=0;dropTarget=0" vertex="1" parent="1">
                <mxGeometry x="583" y="22" width="550" height="310" as="geometry"/>
              </mxCell>
              <mxCell id="subGraph0_label" value="Model Coordination Layer" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;labelBackgroundColor=white;spacing=5" vertex="1" parent="1">
                <mxGeometry x="591" y="30" width="474" height="24" as="geometry"/>
              </mxCell>
              <mxCell id="geminiCoord" value="Gemini Coordinator" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f5f5f5" vertex="1" parent="subGraph0">
                    <mxGeometry x="40" y="120" width="120" height="60" as="geometry"/>
                  </mxCell>
<mxCell id="lmCoord" value="LMStudio Coordinator" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f5f5f5" vertex="1" parent="subGraph0">
                    <mxGeometry x="180" y="120" width="120" height="60" as="geometry"/>
                  </mxCell>
<mxCell id="ollamaCoord" value="Ollama Coordinator" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f5f5f5" vertex="1" parent="subGraph0">
                    <mxGeometry x="320" y="120" width="120" height="60" as="geometry"/>
                  </mxCell>
<mxCell id="crewInterface" value="Common Crew Interface" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f5f5f5" vertex="1" parent="subGraph0">
                    <mxGeometry x="350" y="210" width="120" height="60" as="geometry"/>
                  </mxCell>
<mxCell id="knowledgeManager" value="Knowledge Manager" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f5f5f5" vertex="1" parent="subGraph1">
                    <mxGeometry x="76" y="120" width="120" height="60" as="geometry"/>
                  </mxCell>
<mxCell id="indexStore" value="Index Store" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f5f5f5" vertex="1" parent="subGraph1">
                    <mxGeometry x="180" y="220" width="120" height="60" as="geometry"/>
                  </mxCell>
<mxCell id="categoryManager" value="Category Manager" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f5f5f5" vertex="1" parent="subGraph1">
                    <mxGeometry x="320" y="220" width="120" height="60" as="geometry"/>
                  </mxCell>
<mxCell id="entryManager" value="Entry Manager" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f5f5f5" vertex="1" parent="subGraph1">
                    <mxGeometry x="40" y="220" width="120" height="60" as="geometry"/>
                  </mxCell>
<mxCell id="mlflowDashboard" value="MLflow Dashboard" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f5f5f5" vertex="1" parent="subGraph2">
                    <mxGeometry x="50" y="120" width="120" height="60" as="geometry"/>
                  </mxCell>
<mxCell id="metricTracker" value="Metric Tracking" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f5f5f5" vertex="1" parent="subGraph2">
                    <mxGeometry x="40" y="200" width="120" height="60" as="geometry"/>
                  </mxCell>
<mxCell id="experimentManager" value="Experiment Manager" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f5f5f5" vertex="1" parent="subGraph2">
                    <mxGeometry x="180" y="200" width="120" height="60" as="geometry"/>
                  </mxCell>
<mxCell id="langchainTools" value="LangChain Tools" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f5f5f5" vertex="1" parent="subGraph3">
                    <mxGeometry x="261" y="120" width="120" height="60" as="geometry"/>
                  </mxCell>
<mxCell id="customTools" value="Custom Tools" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f5f5f5" vertex="1" parent="subGraph3">
                    <mxGeometry x="60" y="120" width="120" height="60" as="geometry"/>
                  </mxCell>
<mxCell id="formatterTools" value="Formatter Tools" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f5f5f5" vertex="1" parent="subGraph3">
                    <mxGeometry x="180" y="200" width="120" height="60" as="geometry"/>
                  </mxCell>
<mxCell id="searchTools" value="Search Tools" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f5f5f5" vertex="1" parent="subGraph3">
                    <mxGeometry x="40" y="200" width="120" height="60" as="geometry"/>
                  </mxCell>
<mxCell id="structuredThinking" value="Structured Thinking" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f5f5f5" vertex="1" parent="subGraph4">
                    <mxGeometry x="180" y="120" width="120" height="60" as="geometry"/>
                  </mxCell>
<mxCell id="branchAnalysis" value="Branch Analysis" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f5f5f5" vertex="1" parent="subGraph4">
                    <mxGeometry x="320" y="120" width="120" height="60" as="geometry"/>
                  </mxCell>
<mxCell id="researchAnalysis" value="Research Analysis" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f5f5f5" vertex="1" parent="subGraph4">
                    <mxGeometry x="40" y="120" width="120" height="60" as="geometry"/>
                  </mxCell>
              <mxCell id="edge-L_ollamaCoord_crewInterface_0" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#808080;strokeWidth=2;jumpStyle=arc;jumpSize=10;spacing=15;labelBackgroundColor=white;labelBorderColor=none" edge="1" parent="1" source="ollamaCoord" target="crewInterface">
                  <mxGeometry relative="1" as="geometry"/>
                </mxCell>
<mxCell id="edge-L_crewInterface_customTools_1" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#808080;strokeWidth=2;jumpStyle=arc;jumpSize=10;spacing=15;labelBackgroundColor=white;labelBorderColor=none" edge="1" parent="1" source="crewInterface" target="customTools">
                  <mxGeometry relative="1" as="geometry"/>
                </mxCell>
<mxCell id="edge-L_knowledgeManager_indexStore_2" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#808080;strokeWidth=2;jumpStyle=arc;jumpSize=10;spacing=15;labelBackgroundColor=white;labelBorderColor=none" edge="1" parent="1" source="knowledgeManager" target="indexStore">
                  <mxGeometry relative="1" as="geometry"/>
                </mxCell>
<mxCell id="edge-L_knowledgeManager_categoryManager_3" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#808080;strokeWidth=2;jumpStyle=arc;jumpSize=10;spacing=15;labelBackgroundColor=white;labelBorderColor=none" edge="1" parent="1" source="knowledgeManager" target="categoryManager">
                  <mxGeometry relative="1" as="geometry"/>
                </mxCell>
<mxCell id="edge-L_knowledgeManager_entryManager_4" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#808080;strokeWidth=2;jumpStyle=arc;jumpSize=10;spacing=15;labelBackgroundColor=white;labelBorderColor=none" edge="1" parent="1" source="knowledgeManager" target="entryManager">
                  <mxGeometry relative="1" as="geometry"/>
                </mxCell>
<mxCell id="edge-L_mlflowDashboard_metricTracker_5" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#808080;strokeWidth=2;jumpStyle=arc;jumpSize=10;spacing=15;labelBackgroundColor=white;labelBorderColor=none" edge="1" parent="1" source="mlflowDashboard" target="metricTracker">
                  <mxGeometry relative="1" as="geometry"/>
                </mxCell>
<mxCell id="edge-L_mlflowDashboard_experimentManager_6" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#808080;strokeWidth=2;jumpStyle=arc;jumpSize=10;spacing=15;labelBackgroundColor=white;labelBorderColor=none" edge="1" parent="1" source="mlflowDashboard" target="experimentManager">
                  <mxGeometry relative="1" as="geometry"/>
                </mxCell>
<mxCell id="edge-L_langchainTools_structuredThinking_7" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#808080;strokeWidth=2;jumpStyle=arc;jumpSize=10;spacing=15;labelBackgroundColor=white;labelBorderColor=none" edge="1" parent="1" source="langchainTools" target="structuredThinking">
                  <mxGeometry relative="1" as="geometry"/>
                </mxCell>
<mxCell id="edge-L_langchainTools_branchAnalysis_8" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#808080;strokeWidth=2;jumpStyle=arc;jumpSize=10;spacing=15;labelBackgroundColor=white;labelBorderColor=none" edge="1" parent="1" source="langchainTools" target="branchAnalysis">
                  <mxGeometry relative="1" as="geometry"/>
                </mxCell>
<mxCell id="edge-L_langchainTools_researchAnalysis_9" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#808080;strokeWidth=2;jumpStyle=arc;jumpSize=10;spacing=15;labelBackgroundColor=white;labelBorderColor=none" edge="1" parent="1" source="langchainTools" target="researchAnalysis">
                  <mxGeometry relative="1" as="geometry"/>
                </mxCell>
<mxCell id="edge-L_customTools_formatterTools_10" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#808080;strokeWidth=2;jumpStyle=arc;jumpSize=10;spacing=15;labelBackgroundColor=white;labelBorderColor=none" edge="1" parent="1" source="customTools" target="formatterTools">
                  <mxGeometry relative="1" as="geometry"/>
                </mxCell>
<mxCell id="edge-L_customTools_searchTools_11" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#808080;strokeWidth=2;jumpStyle=arc;jumpSize=10;spacing=15;labelBackgroundColor=white;labelBorderColor=none" edge="1" parent="1" source="customTools" target="searchTools">
                  <mxGeometry relative="1" as="geometry"/>
                </mxCell>
<mxCell id="edge-L_ollamaCoord_mlflowDashboard_12" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#808080;strokeWidth=2;jumpStyle=arc;jumpSize=10;spacing=15;labelBackgroundColor=white;labelBorderColor=none" edge="1" parent="1" source="ollamaCoord" target="mlflowDashboard">
                  <mxGeometry relative="1" as="geometry"/>
                </mxCell>
<mxCell id="edge-L_mlflowDashboard_metricTracker_13" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#808080;strokeWidth=2;jumpStyle=arc;jumpSize=10;spacing=15;labelBackgroundColor=white;labelBorderColor=none" edge="1" parent="1" source="mlflowDashboard" target="metricTracker">
                  <mxGeometry relative="1" as="geometry"/>
                </mxCell>
<mxCell id="edge-L_ollamaCoord_knowledgeManager_14" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#808080;strokeWidth=2;jumpStyle=arc;jumpSize=10;spacing=15;labelBackgroundColor=white;labelBorderColor=none" edge="1" parent="1" source="ollamaCoord" target="knowledgeManager">
                  <mxGeometry relative="1" as="geometry"/>
                </mxCell>
<mxCell id="edge-L_knowledgeManager_indexStore_15" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#808080;strokeWidth=2;jumpStyle=arc;jumpSize=10;spacing=15;labelBackgroundColor=white;labelBorderColor=none" edge="1" parent="1" source="knowledgeManager" target="indexStore">
                  <mxGeometry relative="1" as="geometry"/>
                </mxCell>
<mxCell id="edge-L_crewInterface_langchainTools_16" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#808080;strokeWidth=2;jumpStyle=arc;jumpSize=10;spacing=15;labelBackgroundColor=white;labelBorderColor=none" edge="1" parent="1" source="crewInterface" target="langchainTools">
                  <mxGeometry relative="1" as="geometry"/>
                </mxCell>
<mxCell id="edge-L_crewInterface_customTools_17" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#808080;strokeWidth=2;jumpStyle=arc;jumpSize=10;spacing=15;labelBackgroundColor=white;labelBorderColor=none" edge="1" parent="1" source="crewInterface" target="customTools">
                  <mxGeometry relative="1" as="geometry"/>
                </mxCell>
            </root>
          </mxGraphModel>
        </diagram>
      </mxfile>
````

## File: New folder/current-2025-03-25T5-19pm.drawio

````
<?xml version="1.0" encoding="UTF-8"?>
      <mxfile host="codeviz.app" modified="2025-03-25T21:18:37.010Z" agent="CodeViz Exporter" version="14.6.5" type="device">
        <diagram id="codeviz-diagram" name="System Diagram">
          <mxGraphModel dx="1000" dy="1000" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1169" pageHeight="827" math="0" shadow="0">
            <root>
              <mxCell id="0"/>
              <mxCell id="1" parent="0"/>
              <mxCell id="subGraph2" value="" style="html=1;whiteSpace=wrap;container=1;fillColor=#dae8fc;strokeColor=#6c8ebf;dashed=1;fillOpacity=20;strokeWidth=2;containerType=none;recursiveResize=0;movable=1;resizable=1;autosize=0;dropTarget=0" vertex="1" parent="subGraph3">
                <mxGeometry x="441" y="525" width="520" height="220" as="geometry"/>
              </mxCell>
              <mxCell id="subGraph2_label" value="Knowledge Management" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;labelBackgroundColor=white;spacing=5" vertex="1" parent="subGraph3">
                <mxGeometry x="449" y="533" width="444" height="24" as="geometry"/>
              </mxCell>
<mxCell id="subGraph1" value="" style="html=1;whiteSpace=wrap;container=1;fillColor=#dae8fc;strokeColor=#6c8ebf;dashed=1;fillOpacity=20;strokeWidth=2;containerType=none;recursiveResize=0;movable=1;resizable=1;autosize=0;dropTarget=0" vertex="1" parent="subGraph3">
                <mxGeometry x="141" y="295" width="520" height="220" as="geometry"/>
              </mxCell>
              <mxCell id="subGraph1_label" value="Tools Layer" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;labelBackgroundColor=white;spacing=5" vertex="1" parent="subGraph3">
                <mxGeometry x="149" y="303" width="444" height="24" as="geometry"/>
              </mxCell>
<mxCell id="subGraph5" value="" style="html=1;whiteSpace=wrap;container=1;fillColor=#dae8fc;strokeColor=#6c8ebf;dashed=1;fillOpacity=20;strokeWidth=2;containerType=none;recursiveResize=0;movable=1;resizable=1;autosize=0;dropTarget=0" vertex="1" parent="subGraph6">
                <mxGeometry x="103" y="135" width="520" height="220" as="geometry"/>
              </mxCell>
              <mxCell id="subGraph5_label" value="Utility Components" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;labelBackgroundColor=white;spacing=5" vertex="1" parent="subGraph6">
                <mxGeometry x="111" y="143" width="444" height="24" as="geometry"/>
              </mxCell>
<mxCell id="subGraph4" value="" style="html=1;whiteSpace=wrap;container=1;fillColor=#dae8fc;strokeColor=#6c8ebf;dashed=1;fillOpacity=20;strokeWidth=2;containerType=none;recursiveResize=0;movable=1;resizable=1;autosize=0;dropTarget=0" vertex="1" parent="subGraph6">
                <mxGeometry x="591" y="1240" width="240" height="320" as="geometry"/>
              </mxCell>
              <mxCell id="subGraph4_label" value="Monitoring &amp; Analytics" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;labelBackgroundColor=white;spacing=5" vertex="1" parent="subGraph6">
                <mxGeometry x="599" y="1248" width="164" height="24" as="geometry"/>
              </mxCell>
<mxCell id="subGraph3" value="" style="html=1;whiteSpace=wrap;container=1;fillColor=#dae8fc;strokeColor=#6c8ebf;dashed=1;fillOpacity=20;strokeWidth=2;containerType=none;recursiveResize=0;movable=1;resizable=1;autosize=0;dropTarget=0" vertex="1" parent="subGraph6">
                <mxGeometry x="102" y="425" width="981" height="765" as="geometry"/>
              </mxCell>
              <mxCell id="subGraph3_label" value="Core System" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;labelBackgroundColor=white;spacing=5" vertex="1" parent="subGraph6">
                <mxGeometry x="110" y="433" width="905" height="24" as="geometry"/>
              </mxCell>
<mxCell id="subGraph0" value="" style="html=1;whiteSpace=wrap;container=1;fillColor=#dae8fc;strokeColor=#6c8ebf;dashed=1;fillOpacity=20;strokeWidth=2;containerType=none;recursiveResize=0;movable=1;resizable=1;autosize=0;dropTarget=0" vertex="1" parent="subGraph6">
                <mxGeometry x="91" y="1240" width="520" height="220" as="geometry"/>
              </mxCell>
              <mxCell id="subGraph0_label" value="Model Integration Layer" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;labelBackgroundColor=white;spacing=5" vertex="1" parent="subGraph6">
                <mxGeometry x="99" y="1248" width="444" height="24" as="geometry"/>
              </mxCell>
<mxCell id="subGraph7" value="" style="html=1;whiteSpace=wrap;container=1;fillColor=#dae8fc;strokeColor=#6c8ebf;dashed=1;fillOpacity=20;strokeWidth=2;containerType=none;recursiveResize=0;movable=1;resizable=1;autosize=0;dropTarget=0" vertex="1" parent="1">
                <mxGeometry x="996" y="1887" width="240" height="220" as="geometry"/>
              </mxCell>
              <mxCell id="subGraph7_label" value="External Services" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;labelBackgroundColor=white;spacing=5" vertex="1" parent="1">
                <mxGeometry x="1004" y="1895" width="164" height="24" as="geometry"/>
              </mxCell>
<mxCell id="subGraph6" value="" style="html=1;whiteSpace=wrap;container=1;fillColor=#dae8fc;strokeColor=#6c8ebf;dashed=1;fillOpacity=20;strokeWidth=2;containerType=none;recursiveResize=0;movable=1;resizable=1;autosize=0;dropTarget=0" vertex="1" parent="1">
                <mxGeometry x="73" y="242" width="1064" height="1525" as="geometry"/>
              </mxCell>
              <mxCell id="subGraph6_label" value="AI Analysis System" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;labelBackgroundColor=white;spacing=5" vertex="1" parent="1">
                <mxGeometry x="81" y="250" width="988" height="24" as="geometry"/>
              </mxCell>
              <mxCell id="User" value="External User" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f5f5f5" vertex="1" parent="1">
                    <mxGeometry x="34" y="12" width="120" height="60" as="geometry"/>
                  </mxCell>
<mxCell id="GeminiContainer" value="Gemini Integration&lt;br&gt;(Python/Google AI)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f5f5f5" vertex="1" parent="subGraph0">
                    <mxGeometry x="320" y="120" width="120" height="60" as="geometry"/>
                  </mxCell>
<mxCell id="OllamaContainer" value="Ollama Integration&lt;br&gt;(Python/Ollama)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f5f5f5" vertex="1" parent="subGraph0">
                    <mxGeometry x="40" y="120" width="120" height="60" as="geometry"/>
                  </mxCell>
<mxCell id="LMStudioContainer" value="LMStudio Integration&lt;br&gt;(Python/LMStudio)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f5f5f5" vertex="1" parent="subGraph0">
                    <mxGeometry x="180" y="120" width="120" height="60" as="geometry"/>
                  </mxCell>
<mxCell id="CrewManager" value="Crew Management&lt;br&gt;(CrewAI)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f5f5f5" vertex="1" parent="subGraph3">
                    <mxGeometry x="40" y="120" width="120" height="60" as="geometry"/>
                  </mxCell>
<mxCell id="TaskManager" value="Task Management&lt;br&gt;(YAML Config)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f5f5f5" vertex="1" parent="subGraph3">
                    <mxGeometry x="311" y="220" width="120" height="60" as="geometry"/>
                  </mxCell>
<mxCell id="CustomTools" value="Custom Tools&lt;br&gt;(Python)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f5f5f5" vertex="1" parent="subGraph1">
                    <mxGeometry x="320" y="120" width="120" height="60" as="geometry"/>
                  </mxCell>
<mxCell id="LangChainTools" value="LangChain Tools&lt;br&gt;(LangChain)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f5f5f5" vertex="1" parent="subGraph1">
                    <mxGeometry x="180" y="120" width="120" height="60" as="geometry"/>
                  </mxCell>
<mxCell id="LangGraphTools" value="LangGraph Tools&lt;br&gt;(LangGraph)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f5f5f5" vertex="1" parent="subGraph1">
                    <mxGeometry x="40" y="120" width="120" height="60" as="geometry"/>
                  </mxCell>
<mxCell id="KnowledgeBase" value="Knowledge Base&lt;br&gt;(YAML/JSON)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f5f5f5" vertex="1" parent="subGraph2">
                    <mxGeometry x="40" y="120" width="120" height="60" as="geometry"/>
                  </mxCell>
<mxCell id="PromptTemplates" value="Prompt Templates&lt;br&gt;(Markdown)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f5f5f5" vertex="1" parent="subGraph2">
                    <mxGeometry x="320" y="120" width="120" height="60" as="geometry"/>
                  </mxCell>
<mxCell id="Categories" value="Categories System&lt;br&gt;(YAML)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f5f5f5" vertex="1" parent="subGraph2">
                    <mxGeometry x="180" y="120" width="120" height="60" as="geometry"/>
                  </mxCell>
<mxCell id="MLFlow" value="MLFlow Tracking&lt;br&gt;(MLflow)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f5f5f5" vertex="1" parent="subGraph4">
                    <mxGeometry x="40" y="120" width="120" height="60" as="geometry"/>
                  </mxCell>
<mxCell id="Dashboard" value="MLFlow Dashboard&lt;br&gt;(Python/MLflow)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f5f5f5" vertex="1" parent="subGraph4">
                    <mxGeometry x="40" y="220" width="120" height="60" as="geometry"/>
                  </mxCell>
<mxCell id="ConfigManager" value="Configuration Manager&lt;br&gt;(YAML)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f5f5f5" vertex="1" parent="subGraph5">
                    <mxGeometry x="40" y="120" width="120" height="60" as="geometry"/>
                  </mxCell>
<mxCell id="KnowledgeManager" value="Knowledge Manager&lt;br&gt;(Python)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f5f5f5" vertex="1" parent="subGraph5">
                    <mxGeometry x="180" y="120" width="120" height="60" as="geometry"/>
                  </mxCell>
<mxCell id="PerformanceMonitor" value="Performance Monitor&lt;br&gt;(Python)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f5f5f5" vertex="1" parent="subGraph5">
                    <mxGeometry x="320" y="120" width="120" height="60" as="geometry"/>
                  </mxCell>
<mxCell id="SerperDev" value="Serper.dev API&lt;br&gt;(REST)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f5f5f5" vertex="1" parent="subGraph7">
                    <mxGeometry x="40" y="120" width="120" height="60" as="geometry"/>
                  </mxCell>
              <mxCell id="edge-L_User_CrewManager_0" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#808080;strokeWidth=2;jumpStyle=arc;jumpSize=10;spacing=15;labelBackgroundColor=white;labelBorderColor=none" edge="1" parent="1" source="User" target="CrewManager">
                  <mxGeometry relative="1" as="geometry"/>
                </mxCell>
                <mxCell id="edge-L_User_CrewManager_0_label" value="Interacts" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" vertex="1" connectable="0" parent="edge-L_User_CrewManager_0">
                  <mxGeometry x="-0.2" y="10" relative="1" as="geometry">
                    <mxPoint as="offset"/>
                  </mxGeometry>
                </mxCell>
<mxCell id="edge-L_CrewManager_GeminiContainer_1" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#808080;strokeWidth=2;jumpStyle=arc;jumpSize=10;spacing=15;labelBackgroundColor=white;labelBorderColor=none" edge="1" parent="1" source="CrewManager" target="GeminiContainer">
                  <mxGeometry relative="1" as="geometry"/>
                </mxCell>
                <mxCell id="edge-L_CrewManager_GeminiContainer_1_label" value="Manages" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" vertex="1" connectable="0" parent="edge-L_CrewManager_GeminiContainer_1">
                  <mxGeometry x="-0.2" y="10" relative="1" as="geometry">
                    <mxPoint as="offset"/>
                  </mxGeometry>
                </mxCell>
<mxCell id="edge-L_CrewManager_OllamaContainer_2" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#808080;strokeWidth=2;jumpStyle=arc;jumpSize=10;spacing=15;labelBackgroundColor=white;labelBorderColor=none" edge="1" parent="1" source="CrewManager" target="OllamaContainer">
                  <mxGeometry relative="1" as="geometry"/>
                </mxCell>
                <mxCell id="edge-L_CrewManager_OllamaContainer_2_label" value="Manages" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" vertex="1" connectable="0" parent="edge-L_CrewManager_OllamaContainer_2">
                  <mxGeometry x="-0.2" y="10" relative="1" as="geometry">
                    <mxPoint as="offset"/>
                  </mxGeometry>
                </mxCell>
<mxCell id="edge-L_CrewManager_LMStudioContainer_3" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#808080;strokeWidth=2;jumpStyle=arc;jumpSize=10;spacing=15;labelBackgroundColor=white;labelBorderColor=none" edge="1" parent="1" source="CrewManager" target="LMStudioContainer">
                  <mxGeometry relative="1" as="geometry"/>
                </mxCell>
                <mxCell id="edge-L_CrewManager_LMStudioContainer_3_label" value="Manages" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" vertex="1" connectable="0" parent="edge-L_CrewManager_LMStudioContainer_3">
                  <mxGeometry x="-0.2" y="10" relative="1" as="geometry">
                    <mxPoint as="offset"/>
                  </mxGeometry>
                </mxCell>
<mxCell id="edge-L_CrewManager_TaskManager_4" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#808080;strokeWidth=2;jumpStyle=arc;jumpSize=10;spacing=15;labelBackgroundColor=white;labelBorderColor=none" edge="1" parent="1" source="CrewManager" target="TaskManager">
                  <mxGeometry relative="1" as="geometry"/>
                </mxCell>
                <mxCell id="edge-L_CrewManager_TaskManager_4_label" value="Uses" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" vertex="1" connectable="0" parent="edge-L_CrewManager_TaskManager_4">
                  <mxGeometry x="-0.2" y="10" relative="1" as="geometry">
                    <mxPoint as="offset"/>
                  </mxGeometry>
                </mxCell>
<mxCell id="edge-L_TaskManager_CustomTools_5" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#808080;strokeWidth=2;jumpStyle=arc;jumpSize=10;spacing=15;labelBackgroundColor=white;labelBorderColor=none" edge="1" parent="1" source="TaskManager" target="CustomTools">
                  <mxGeometry relative="1" as="geometry"/>
                </mxCell>
                <mxCell id="edge-L_TaskManager_CustomTools_5_label" value="Configures" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" vertex="1" connectable="0" parent="edge-L_TaskManager_CustomTools_5">
                  <mxGeometry x="-0.2" y="10" relative="1" as="geometry">
                    <mxPoint as="offset"/>
                  </mxGeometry>
                </mxCell>
<mxCell id="edge-L_TaskManager_LangChainTools_6" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#808080;strokeWidth=2;jumpStyle=arc;jumpSize=10;spacing=15;labelBackgroundColor=white;labelBorderColor=none" edge="1" parent="1" source="TaskManager" target="LangChainTools">
                  <mxGeometry relative="1" as="geometry"/>
                </mxCell>
                <mxCell id="edge-L_TaskManager_LangChainTools_6_label" value="Configures" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" vertex="1" connectable="0" parent="edge-L_TaskManager_LangChainTools_6">
                  <mxGeometry x="-0.2" y="10" relative="1" as="geometry">
                    <mxPoint as="offset"/>
                  </mxGeometry>
                </mxCell>
<mxCell id="edge-L_TaskManager_LangGraphTools_7" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#808080;strokeWidth=2;jumpStyle=arc;jumpSize=10;spacing=15;labelBackgroundColor=white;labelBorderColor=none" edge="1" parent="1" source="TaskManager" target="LangGraphTools">
                  <mxGeometry relative="1" as="geometry"/>
                </mxCell>
                <mxCell id="edge-L_TaskManager_LangGraphTools_7_label" value="Configures" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" vertex="1" connectable="0" parent="edge-L_TaskManager_LangGraphTools_7">
                  <mxGeometry x="-0.2" y="10" relative="1" as="geometry">
                    <mxPoint as="offset"/>
                  </mxGeometry>
                </mxCell>
<mxCell id="edge-L_CustomTools_KnowledgeBase_8" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#808080;strokeWidth=2;jumpStyle=arc;jumpSize=10;spacing=15;labelBackgroundColor=white;labelBorderColor=none" edge="1" parent="1" source="CustomTools" target="KnowledgeBase">
                  <mxGeometry relative="1" as="geometry"/>
                </mxCell>
                <mxCell id="edge-L_CustomTools_KnowledgeBase_8_label" value="Accesses" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" vertex="1" connectable="0" parent="edge-L_CustomTools_KnowledgeBase_8">
                  <mxGeometry x="-0.2" y="10" relative="1" as="geometry">
                    <mxPoint as="offset"/>
                  </mxGeometry>
                </mxCell>
<mxCell id="edge-L_LangChainTools_SerperDev_9" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#808080;strokeWidth=2;jumpStyle=arc;jumpSize=10;spacing=15;labelBackgroundColor=white;labelBorderColor=none" edge="1" parent="1" source="LangChainTools" target="SerperDev">
                  <mxGeometry relative="1" as="geometry"/>
                </mxCell>
                <mxCell id="edge-L_LangChainTools_SerperDev_9_label" value="Uses" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" vertex="1" connectable="0" parent="edge-L_LangChainTools_SerperDev_9">
                  <mxGeometry x="-0.2" y="10" relative="1" as="geometry">
                    <mxPoint as="offset"/>
                  </mxGeometry>
                </mxCell>
<mxCell id="edge-L_KnowledgeManager_KnowledgeBase_10" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#808080;strokeWidth=2;jumpStyle=arc;jumpSize=10;spacing=15;labelBackgroundColor=white;labelBorderColor=none" edge="1" parent="1" source="KnowledgeManager" target="KnowledgeBase">
                  <mxGeometry relative="1" as="geometry"/>
                </mxCell>
                <mxCell id="edge-L_KnowledgeManager_KnowledgeBase_10_label" value="Manages" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" vertex="1" connectable="0" parent="edge-L_KnowledgeManager_KnowledgeBase_10">
                  <mxGeometry x="-0.2" y="10" relative="1" as="geometry">
                    <mxPoint as="offset"/>
                  </mxGeometry>
                </mxCell>
<mxCell id="edge-L_KnowledgeManager_PromptTemplates_11" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#808080;strokeWidth=2;jumpStyle=arc;jumpSize=10;spacing=15;labelBackgroundColor=white;labelBorderColor=none" edge="1" parent="1" source="KnowledgeManager" target="PromptTemplates">
                  <mxGeometry relative="1" as="geometry"/>
                </mxCell>
                <mxCell id="edge-L_KnowledgeManager_PromptTemplates_11_label" value="Manages" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" vertex="1" connectable="0" parent="edge-L_KnowledgeManager_PromptTemplates_11">
                  <mxGeometry x="-0.2" y="10" relative="1" as="geometry">
                    <mxPoint as="offset"/>
                  </mxGeometry>
                </mxCell>
<mxCell id="edge-L_KnowledgeManager_Categories_12" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#808080;strokeWidth=2;jumpStyle=arc;jumpSize=10;spacing=15;labelBackgroundColor=white;labelBorderColor=none" edge="1" parent="1" source="KnowledgeManager" target="Categories">
                  <mxGeometry relative="1" as="geometry"/>
                </mxCell>
                <mxCell id="edge-L_KnowledgeManager_Categories_12_label" value="Manages" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" vertex="1" connectable="0" parent="edge-L_KnowledgeManager_Categories_12">
                  <mxGeometry x="-0.2" y="10" relative="1" as="geometry">
                    <mxPoint as="offset"/>
                  </mxGeometry>
                </mxCell>
<mxCell id="edge-L_CrewManager_MLFlow_13" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#808080;strokeWidth=2;jumpStyle=arc;jumpSize=10;spacing=15;labelBackgroundColor=white;labelBorderColor=none" edge="1" parent="1" source="CrewManager" target="MLFlow">
                  <mxGeometry relative="1" as="geometry"/>
                </mxCell>
                <mxCell id="edge-L_CrewManager_MLFlow_13_label" value="Logs to" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" vertex="1" connectable="0" parent="edge-L_CrewManager_MLFlow_13">
                  <mxGeometry x="-0.2" y="10" relative="1" as="geometry">
                    <mxPoint as="offset"/>
                  </mxGeometry>
                </mxCell>
<mxCell id="edge-L_MLFlow_Dashboard_14" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#808080;strokeWidth=2;jumpStyle=arc;jumpSize=10;spacing=15;labelBackgroundColor=white;labelBorderColor=none" edge="1" parent="1" source="MLFlow" target="Dashboard">
                  <mxGeometry relative="1" as="geometry"/>
                </mxCell>
                <mxCell id="edge-L_MLFlow_Dashboard_14_label" value="Displays in" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" vertex="1" connectable="0" parent="edge-L_MLFlow_Dashboard_14">
                  <mxGeometry x="-0.2" y="10" relative="1" as="geometry">
                    <mxPoint as="offset"/>
                  </mxGeometry>
                </mxCell>
<mxCell id="edge-L_ConfigManager_CrewManager_15" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#808080;strokeWidth=2;jumpStyle=arc;jumpSize=10;spacing=15;labelBackgroundColor=white;labelBorderColor=none" edge="1" parent="1" source="ConfigManager" target="CrewManager">
                  <mxGeometry relative="1" as="geometry"/>
                </mxCell>
                <mxCell id="edge-L_ConfigManager_CrewManager_15_label" value="Configures" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" vertex="1" connectable="0" parent="edge-L_ConfigManager_CrewManager_15">
                  <mxGeometry x="-0.2" y="10" relative="1" as="geometry">
                    <mxPoint as="offset"/>
                  </mxGeometry>
                </mxCell>
<mxCell id="edge-L_ConfigManager_TaskManager_16" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#808080;strokeWidth=2;jumpStyle=arc;jumpSize=10;spacing=15;labelBackgroundColor=white;labelBorderColor=none" edge="1" parent="1" source="ConfigManager" target="TaskManager">
                  <mxGeometry relative="1" as="geometry"/>
                </mxCell>
                <mxCell id="edge-L_ConfigManager_TaskManager_16_label" value="Configures" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" vertex="1" connectable="0" parent="edge-L_ConfigManager_TaskManager_16">
                  <mxGeometry x="-0.2" y="10" relative="1" as="geometry">
                    <mxPoint as="offset"/>
                  </mxGeometry>
                </mxCell>
<mxCell id="edge-L_PerformanceMonitor_MLFlow_17" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#808080;strokeWidth=2;jumpStyle=arc;jumpSize=10;spacing=15;labelBackgroundColor=white;labelBorderColor=none" edge="1" parent="1" source="PerformanceMonitor" target="MLFlow">
                  <mxGeometry relative="1" as="geometry"/>
                </mxCell>
                <mxCell id="edge-L_PerformanceMonitor_MLFlow_17_label" value="Tracks" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" vertex="1" connectable="0" parent="edge-L_PerformanceMonitor_MLFlow_17">
                  <mxGeometry x="-0.2" y="10" relative="1" as="geometry">
                    <mxPoint as="offset"/>
                  </mxGeometry>
                </mxCell>
<mxCell id="edge-L_GeminiContainer_KnowledgeManager_18" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#808080;strokeWidth=2;jumpStyle=arc;jumpSize=10;spacing=15;labelBackgroundColor=white;labelBorderColor=none" edge="1" parent="1" source="GeminiContainer" target="KnowledgeManager">
                  <mxGeometry relative="1" as="geometry"/>
                </mxCell>
                <mxCell id="edge-L_GeminiContainer_KnowledgeManager_18_label" value="Uses" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" vertex="1" connectable="0" parent="edge-L_GeminiContainer_KnowledgeManager_18">
                  <mxGeometry x="-0.2" y="10" relative="1" as="geometry">
                    <mxPoint as="offset"/>
                  </mxGeometry>
                </mxCell>
<mxCell id="edge-L_OllamaContainer_KnowledgeManager_19" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#808080;strokeWidth=2;jumpStyle=arc;jumpSize=10;spacing=15;labelBackgroundColor=white;labelBorderColor=none" edge="1" parent="1" source="OllamaContainer" target="KnowledgeManager">
                  <mxGeometry relative="1" as="geometry"/>
                </mxCell>
                <mxCell id="edge-L_OllamaContainer_KnowledgeManager_19_label" value="Uses" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" vertex="1" connectable="0" parent="edge-L_OllamaContainer_KnowledgeManager_19">
                  <mxGeometry x="-0.2" y="10" relative="1" as="geometry">
                    <mxPoint as="offset"/>
                  </mxGeometry>
                </mxCell>
<mxCell id="edge-L_LMStudioContainer_KnowledgeManager_20" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#808080;strokeWidth=2;jumpStyle=arc;jumpSize=10;spacing=15;labelBackgroundColor=white;labelBorderColor=none" edge="1" parent="1" source="LMStudioContainer" target="KnowledgeManager">
                  <mxGeometry relative="1" as="geometry"/>
                </mxCell>
                <mxCell id="edge-L_LMStudioContainer_KnowledgeManager_20_label" value="Uses" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" vertex="1" connectable="0" parent="edge-L_LMStudioContainer_KnowledgeManager_20">
                  <mxGeometry x="-0.2" y="10" relative="1" as="geometry">
                    <mxPoint as="offset"/>
                  </mxGeometry>
                </mxCell>
            </root>
          </mxGraphModel>
        </diagram>
      </mxfile>
````

## File: New folder/current-2025-03-25T5-22pm.drawio

````
<?xml version="1.0" encoding="UTF-8"?>
      <mxfile host="codeviz.app" modified="2025-03-25T21:20:44.816Z" agent="CodeViz Exporter" version="14.6.5" type="device">
        <diagram id="codeviz-diagram" name="System Diagram">
          <mxGraphModel dx="1000" dy="1000" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1169" pageHeight="827" math="0" shadow="0">
            <root>
              <mxCell id="0"/>
              <mxCell id="1" parent="0"/>
              <mxCell id="subGraph2" value="" style="html=1;whiteSpace=wrap;container=1;fillColor=#dae8fc;strokeColor=#6c8ebf;dashed=1;fillOpacity=20;strokeWidth=2;containerType=none;recursiveResize=0;movable=1;resizable=1;autosize=0;dropTarget=0" vertex="1" parent="subGraph3">
                <mxGeometry x="441" y="525" width="520" height="220" as="geometry"/>
              </mxCell>
              <mxCell id="subGraph2_label" value="Knowledge Management" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;labelBackgroundColor=white;spacing=5" vertex="1" parent="subGraph3">
                <mxGeometry x="449" y="533" width="444" height="24" as="geometry"/>
              </mxCell>
<mxCell id="subGraph1" value="" style="html=1;whiteSpace=wrap;container=1;fillColor=#dae8fc;strokeColor=#6c8ebf;dashed=1;fillOpacity=20;strokeWidth=2;containerType=none;recursiveResize=0;movable=1;resizable=1;autosize=0;dropTarget=0" vertex="1" parent="subGraph3">
                <mxGeometry x="141" y="295" width="520" height="220" as="geometry"/>
              </mxCell>
              <mxCell id="subGraph1_label" value="Tools Layer" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;labelBackgroundColor=white;spacing=5" vertex="1" parent="subGraph3">
                <mxGeometry x="149" y="303" width="444" height="24" as="geometry"/>
              </mxCell>
<mxCell id="subGraph5" value="" style="html=1;whiteSpace=wrap;container=1;fillColor=#dae8fc;strokeColor=#6c8ebf;dashed=1;fillOpacity=20;strokeWidth=2;containerType=none;recursiveResize=0;movable=1;resizable=1;autosize=0;dropTarget=0" vertex="1" parent="subGraph6">
                <mxGeometry x="103" y="135" width="520" height="220" as="geometry"/>
              </mxCell>
              <mxCell id="subGraph5_label" value="Utility Components" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;labelBackgroundColor=white;spacing=5" vertex="1" parent="subGraph6">
                <mxGeometry x="111" y="143" width="444" height="24" as="geometry"/>
              </mxCell>
<mxCell id="subGraph4" value="" style="html=1;whiteSpace=wrap;container=1;fillColor=#dae8fc;strokeColor=#6c8ebf;dashed=1;fillOpacity=20;strokeWidth=2;containerType=none;recursiveResize=0;movable=1;resizable=1;autosize=0;dropTarget=0" vertex="1" parent="subGraph6">
                <mxGeometry x="591" y="1240" width="240" height="320" as="geometry"/>
              </mxCell>
              <mxCell id="subGraph4_label" value="Monitoring &amp; Analytics" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;labelBackgroundColor=white;spacing=5" vertex="1" parent="subGraph6">
                <mxGeometry x="599" y="1248" width="164" height="24" as="geometry"/>
              </mxCell>
<mxCell id="subGraph3" value="" style="html=1;whiteSpace=wrap;container=1;fillColor=#dae8fc;strokeColor=#6c8ebf;dashed=1;fillOpacity=20;strokeWidth=2;containerType=none;recursiveResize=0;movable=1;resizable=1;autosize=0;dropTarget=0" vertex="1" parent="subGraph6">
                <mxGeometry x="102" y="425" width="981" height="765" as="geometry"/>
              </mxCell>
              <mxCell id="subGraph3_label" value="Core System" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;labelBackgroundColor=white;spacing=5" vertex="1" parent="subGraph6">
                <mxGeometry x="110" y="433" width="905" height="24" as="geometry"/>
              </mxCell>
<mxCell id="subGraph0" value="" style="html=1;whiteSpace=wrap;container=1;fillColor=#dae8fc;strokeColor=#6c8ebf;dashed=1;fillOpacity=20;strokeWidth=2;containerType=none;recursiveResize=0;movable=1;resizable=1;autosize=0;dropTarget=0" vertex="1" parent="subGraph6">
                <mxGeometry x="91" y="1240" width="520" height="220" as="geometry"/>
              </mxCell>
              <mxCell id="subGraph0_label" value="Model Integration Layer" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;labelBackgroundColor=white;spacing=5" vertex="1" parent="subGraph6">
                <mxGeometry x="99" y="1248" width="444" height="24" as="geometry"/>
              </mxCell>
<mxCell id="subGraph7" value="" style="html=1;whiteSpace=wrap;container=1;fillColor=#dae8fc;strokeColor=#6c8ebf;dashed=1;fillOpacity=20;strokeWidth=2;containerType=none;recursiveResize=0;movable=1;resizable=1;autosize=0;dropTarget=0" vertex="1" parent="1">
                <mxGeometry x="996" y="1887" width="240" height="220" as="geometry"/>
              </mxCell>
              <mxCell id="subGraph7_label" value="External Services" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;labelBackgroundColor=white;spacing=5" vertex="1" parent="1">
                <mxGeometry x="1004" y="1895" width="164" height="24" as="geometry"/>
              </mxCell>
<mxCell id="subGraph6" value="" style="html=1;whiteSpace=wrap;container=1;fillColor=#dae8fc;strokeColor=#6c8ebf;dashed=1;fillOpacity=20;strokeWidth=2;containerType=none;recursiveResize=0;movable=1;resizable=1;autosize=0;dropTarget=0" vertex="1" parent="1">
                <mxGeometry x="73" y="242" width="1064" height="1525" as="geometry"/>
              </mxCell>
              <mxCell id="subGraph6_label" value="AI Analysis System" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;labelBackgroundColor=white;spacing=5" vertex="1" parent="1">
                <mxGeometry x="81" y="250" width="988" height="24" as="geometry"/>
              </mxCell>
              <mxCell id="User" value="External User" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f5f5f5" vertex="1" parent="1">
                    <mxGeometry x="34" y="12" width="120" height="60" as="geometry"/>
                  </mxCell>
<mxCell id="GeminiContainer" value="Gemini Integration&lt;br&gt;(Python/Google AI)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f5f5f5" vertex="1" parent="subGraph0">
                    <mxGeometry x="320" y="120" width="120" height="60" as="geometry"/>
                  </mxCell>
<mxCell id="OllamaContainer" value="Ollama Integration&lt;br&gt;(Python/Ollama)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f5f5f5" vertex="1" parent="subGraph0">
                    <mxGeometry x="40" y="120" width="120" height="60" as="geometry"/>
                  </mxCell>
<mxCell id="LMStudioContainer" value="LMStudio Integration&lt;br&gt;(Python/LMStudio)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f5f5f5" vertex="1" parent="subGraph0">
                    <mxGeometry x="180" y="120" width="120" height="60" as="geometry"/>
                  </mxCell>
<mxCell id="CrewManager" value="Crew Management&lt;br&gt;(CrewAI)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f5f5f5" vertex="1" parent="subGraph3">
                    <mxGeometry x="40" y="120" width="120" height="60" as="geometry"/>
                  </mxCell>
<mxCell id="TaskManager" value="Task Management&lt;br&gt;(YAML Config)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f5f5f5" vertex="1" parent="subGraph3">
                    <mxGeometry x="311" y="220" width="120" height="60" as="geometry"/>
                  </mxCell>
<mxCell id="CustomTools" value="Custom Tools&lt;br&gt;(Python)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f5f5f5" vertex="1" parent="subGraph1">
                    <mxGeometry x="320" y="120" width="120" height="60" as="geometry"/>
                  </mxCell>
<mxCell id="LangChainTools" value="LangChain Tools&lt;br&gt;(LangChain)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f5f5f5" vertex="1" parent="subGraph1">
                    <mxGeometry x="180" y="120" width="120" height="60" as="geometry"/>
                  </mxCell>
<mxCell id="LangGraphTools" value="LangGraph Tools&lt;br&gt;(LangGraph)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f5f5f5" vertex="1" parent="subGraph1">
                    <mxGeometry x="40" y="120" width="120" height="60" as="geometry"/>
                  </mxCell>
<mxCell id="KnowledgeBase" value="Knowledge Base&lt;br&gt;(YAML/JSON)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f5f5f5" vertex="1" parent="subGraph2">
                    <mxGeometry x="40" y="120" width="120" height="60" as="geometry"/>
                  </mxCell>
<mxCell id="PromptTemplates" value="Prompt Templates&lt;br&gt;(Markdown)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f5f5f5" vertex="1" parent="subGraph2">
                    <mxGeometry x="320" y="120" width="120" height="60" as="geometry"/>
                  </mxCell>
<mxCell id="Categories" value="Categories System&lt;br&gt;(YAML)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f5f5f5" vertex="1" parent="subGraph2">
                    <mxGeometry x="180" y="120" width="120" height="60" as="geometry"/>
                  </mxCell>
<mxCell id="MLFlow" value="MLFlow Tracking&lt;br&gt;(MLflow)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f5f5f5" vertex="1" parent="subGraph4">
                    <mxGeometry x="40" y="120" width="120" height="60" as="geometry"/>
                  </mxCell>
<mxCell id="Dashboard" value="MLFlow Dashboard&lt;br&gt;(Python/MLflow)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f5f5f5" vertex="1" parent="subGraph4">
                    <mxGeometry x="40" y="220" width="120" height="60" as="geometry"/>
                  </mxCell>
<mxCell id="ConfigManager" value="Configuration Manager&lt;br&gt;(YAML)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f5f5f5" vertex="1" parent="subGraph5">
                    <mxGeometry x="40" y="120" width="120" height="60" as="geometry"/>
                  </mxCell>
<mxCell id="KnowledgeManager" value="Knowledge Manager&lt;br&gt;(Python)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f5f5f5" vertex="1" parent="subGraph5">
                    <mxGeometry x="180" y="120" width="120" height="60" as="geometry"/>
                  </mxCell>
<mxCell id="PerformanceMonitor" value="Performance Monitor&lt;br&gt;(Python)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f5f5f5" vertex="1" parent="subGraph5">
                    <mxGeometry x="320" y="120" width="120" height="60" as="geometry"/>
                  </mxCell>
<mxCell id="SerperDev" value="Serper.dev API&lt;br&gt;(REST)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f5f5f5" vertex="1" parent="subGraph7">
                    <mxGeometry x="40" y="120" width="120" height="60" as="geometry"/>
                  </mxCell>
              <mxCell id="edge-L_User_CrewManager_0" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#808080;strokeWidth=2;jumpStyle=arc;jumpSize=10;spacing=15;labelBackgroundColor=white;labelBorderColor=none" edge="1" parent="1" source="User" target="CrewManager">
                  <mxGeometry relative="1" as="geometry"/>
                </mxCell>
                <mxCell id="edge-L_User_CrewManager_0_label" value="Interacts" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" vertex="1" connectable="0" parent="edge-L_User_CrewManager_0">
                  <mxGeometry x="-0.2" y="10" relative="1" as="geometry">
                    <mxPoint as="offset"/>
                  </mxGeometry>
                </mxCell>
<mxCell id="edge-L_CrewManager_GeminiContainer_1" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#808080;strokeWidth=2;jumpStyle=arc;jumpSize=10;spacing=15;labelBackgroundColor=white;labelBorderColor=none" edge="1" parent="1" source="CrewManager" target="GeminiContainer">
                  <mxGeometry relative="1" as="geometry"/>
                </mxCell>
                <mxCell id="edge-L_CrewManager_GeminiContainer_1_label" value="Manages" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" vertex="1" connectable="0" parent="edge-L_CrewManager_GeminiContainer_1">
                  <mxGeometry x="-0.2" y="10" relative="1" as="geometry">
                    <mxPoint as="offset"/>
                  </mxGeometry>
                </mxCell>
<mxCell id="edge-L_CrewManager_OllamaContainer_2" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#808080;strokeWidth=2;jumpStyle=arc;jumpSize=10;spacing=15;labelBackgroundColor=white;labelBorderColor=none" edge="1" parent="1" source="CrewManager" target="OllamaContainer">
                  <mxGeometry relative="1" as="geometry"/>
                </mxCell>
                <mxCell id="edge-L_CrewManager_OllamaContainer_2_label" value="Manages" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" vertex="1" connectable="0" parent="edge-L_CrewManager_OllamaContainer_2">
                  <mxGeometry x="-0.2" y="10" relative="1" as="geometry">
                    <mxPoint as="offset"/>
                  </mxGeometry>
                </mxCell>
<mxCell id="edge-L_CrewManager_LMStudioContainer_3" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#808080;strokeWidth=2;jumpStyle=arc;jumpSize=10;spacing=15;labelBackgroundColor=white;labelBorderColor=none" edge="1" parent="1" source="CrewManager" target="LMStudioContainer">
                  <mxGeometry relative="1" as="geometry"/>
                </mxCell>
                <mxCell id="edge-L_CrewManager_LMStudioContainer_3_label" value="Manages" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" vertex="1" connectable="0" parent="edge-L_CrewManager_LMStudioContainer_3">
                  <mxGeometry x="-0.2" y="10" relative="1" as="geometry">
                    <mxPoint as="offset"/>
                  </mxGeometry>
                </mxCell>
<mxCell id="edge-L_CrewManager_TaskManager_4" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#808080;strokeWidth=2;jumpStyle=arc;jumpSize=10;spacing=15;labelBackgroundColor=white;labelBorderColor=none" edge="1" parent="1" source="CrewManager" target="TaskManager">
                  <mxGeometry relative="1" as="geometry"/>
                </mxCell>
                <mxCell id="edge-L_CrewManager_TaskManager_4_label" value="Uses" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" vertex="1" connectable="0" parent="edge-L_CrewManager_TaskManager_4">
                  <mxGeometry x="-0.2" y="10" relative="1" as="geometry">
                    <mxPoint as="offset"/>
                  </mxGeometry>
                </mxCell>
<mxCell id="edge-L_TaskManager_CustomTools_5" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#808080;strokeWidth=2;jumpStyle=arc;jumpSize=10;spacing=15;labelBackgroundColor=white;labelBorderColor=none" edge="1" parent="1" source="TaskManager" target="CustomTools">
                  <mxGeometry relative="1" as="geometry"/>
                </mxCell>
                <mxCell id="edge-L_TaskManager_CustomTools_5_label" value="Configures" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" vertex="1" connectable="0" parent="edge-L_TaskManager_CustomTools_5">
                  <mxGeometry x="-0.2" y="10" relative="1" as="geometry">
                    <mxPoint as="offset"/>
                  </mxGeometry>
                </mxCell>
<mxCell id="edge-L_TaskManager_LangChainTools_6" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#808080;strokeWidth=2;jumpStyle=arc;jumpSize=10;spacing=15;labelBackgroundColor=white;labelBorderColor=none" edge="1" parent="1" source="TaskManager" target="LangChainTools">
                  <mxGeometry relative="1" as="geometry"/>
                </mxCell>
                <mxCell id="edge-L_TaskManager_LangChainTools_6_label" value="Configures" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" vertex="1" connectable="0" parent="edge-L_TaskManager_LangChainTools_6">
                  <mxGeometry x="-0.2" y="10" relative="1" as="geometry">
                    <mxPoint as="offset"/>
                  </mxGeometry>
                </mxCell>
<mxCell id="edge-L_TaskManager_LangGraphTools_7" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#808080;strokeWidth=2;jumpStyle=arc;jumpSize=10;spacing=15;labelBackgroundColor=white;labelBorderColor=none" edge="1" parent="1" source="TaskManager" target="LangGraphTools">
                  <mxGeometry relative="1" as="geometry"/>
                </mxCell>
                <mxCell id="edge-L_TaskManager_LangGraphTools_7_label" value="Configures" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" vertex="1" connectable="0" parent="edge-L_TaskManager_LangGraphTools_7">
                  <mxGeometry x="-0.2" y="10" relative="1" as="geometry">
                    <mxPoint as="offset"/>
                  </mxGeometry>
                </mxCell>
<mxCell id="edge-L_CustomTools_KnowledgeBase_8" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#808080;strokeWidth=2;jumpStyle=arc;jumpSize=10;spacing=15;labelBackgroundColor=white;labelBorderColor=none" edge="1" parent="1" source="CustomTools" target="KnowledgeBase">
                  <mxGeometry relative="1" as="geometry"/>
                </mxCell>
                <mxCell id="edge-L_CustomTools_KnowledgeBase_8_label" value="Accesses" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" vertex="1" connectable="0" parent="edge-L_CustomTools_KnowledgeBase_8">
                  <mxGeometry x="-0.2" y="10" relative="1" as="geometry">
                    <mxPoint as="offset"/>
                  </mxGeometry>
                </mxCell>
<mxCell id="edge-L_LangChainTools_SerperDev_9" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#808080;strokeWidth=2;jumpStyle=arc;jumpSize=10;spacing=15;labelBackgroundColor=white;labelBorderColor=none" edge="1" parent="1" source="LangChainTools" target="SerperDev">
                  <mxGeometry relative="1" as="geometry"/>
                </mxCell>
                <mxCell id="edge-L_LangChainTools_SerperDev_9_label" value="Uses" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" vertex="1" connectable="0" parent="edge-L_LangChainTools_SerperDev_9">
                  <mxGeometry x="-0.2" y="10" relative="1" as="geometry">
                    <mxPoint as="offset"/>
                  </mxGeometry>
                </mxCell>
<mxCell id="edge-L_KnowledgeManager_KnowledgeBase_10" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#808080;strokeWidth=2;jumpStyle=arc;jumpSize=10;spacing=15;labelBackgroundColor=white;labelBorderColor=none" edge="1" parent="1" source="KnowledgeManager" target="KnowledgeBase">
                  <mxGeometry relative="1" as="geometry"/>
                </mxCell>
                <mxCell id="edge-L_KnowledgeManager_KnowledgeBase_10_label" value="Manages" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" vertex="1" connectable="0" parent="edge-L_KnowledgeManager_KnowledgeBase_10">
                  <mxGeometry x="-0.2" y="10" relative="1" as="geometry">
                    <mxPoint as="offset"/>
                  </mxGeometry>
                </mxCell>
<mxCell id="edge-L_KnowledgeManager_PromptTemplates_11" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#808080;strokeWidth=2;jumpStyle=arc;jumpSize=10;spacing=15;labelBackgroundColor=white;labelBorderColor=none" edge="1" parent="1" source="KnowledgeManager" target="PromptTemplates">
                  <mxGeometry relative="1" as="geometry"/>
                </mxCell>
                <mxCell id="edge-L_KnowledgeManager_PromptTemplates_11_label" value="Manages" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" vertex="1" connectable="0" parent="edge-L_KnowledgeManager_PromptTemplates_11">
                  <mxGeometry x="-0.2" y="10" relative="1" as="geometry">
                    <mxPoint as="offset"/>
                  </mxGeometry>
                </mxCell>
<mxCell id="edge-L_KnowledgeManager_Categories_12" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#808080;strokeWidth=2;jumpStyle=arc;jumpSize=10;spacing=15;labelBackgroundColor=white;labelBorderColor=none" edge="1" parent="1" source="KnowledgeManager" target="Categories">
                  <mxGeometry relative="1" as="geometry"/>
                </mxCell>
                <mxCell id="edge-L_KnowledgeManager_Categories_12_label" value="Manages" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" vertex="1" connectable="0" parent="edge-L_KnowledgeManager_Categories_12">
                  <mxGeometry x="-0.2" y="10" relative="1" as="geometry">
                    <mxPoint as="offset"/>
                  </mxGeometry>
                </mxCell>
<mxCell id="edge-L_CrewManager_MLFlow_13" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#808080;strokeWidth=2;jumpStyle=arc;jumpSize=10;spacing=15;labelBackgroundColor=white;labelBorderColor=none" edge="1" parent="1" source="CrewManager" target="MLFlow">
                  <mxGeometry relative="1" as="geometry"/>
                </mxCell>
                <mxCell id="edge-L_CrewManager_MLFlow_13_label" value="Logs to" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" vertex="1" connectable="0" parent="edge-L_CrewManager_MLFlow_13">
                  <mxGeometry x="-0.2" y="10" relative="1" as="geometry">
                    <mxPoint as="offset"/>
                  </mxGeometry>
                </mxCell>
<mxCell id="edge-L_MLFlow_Dashboard_14" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#808080;strokeWidth=2;jumpStyle=arc;jumpSize=10;spacing=15;labelBackgroundColor=white;labelBorderColor=none" edge="1" parent="1" source="MLFlow" target="Dashboard">
                  <mxGeometry relative="1" as="geometry"/>
                </mxCell>
                <mxCell id="edge-L_MLFlow_Dashboard_14_label" value="Displays in" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" vertex="1" connectable="0" parent="edge-L_MLFlow_Dashboard_14">
                  <mxGeometry x="-0.2" y="10" relative="1" as="geometry">
                    <mxPoint as="offset"/>
                  </mxGeometry>
                </mxCell>
<mxCell id="edge-L_ConfigManager_CrewManager_15" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#808080;strokeWidth=2;jumpStyle=arc;jumpSize=10;spacing=15;labelBackgroundColor=white;labelBorderColor=none" edge="1" parent="1" source="ConfigManager" target="CrewManager">
                  <mxGeometry relative="1" as="geometry"/>
                </mxCell>
                <mxCell id="edge-L_ConfigManager_CrewManager_15_label" value="Configures" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" vertex="1" connectable="0" parent="edge-L_ConfigManager_CrewManager_15">
                  <mxGeometry x="-0.2" y="10" relative="1" as="geometry">
                    <mxPoint as="offset"/>
                  </mxGeometry>
                </mxCell>
<mxCell id="edge-L_ConfigManager_TaskManager_16" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#808080;strokeWidth=2;jumpStyle=arc;jumpSize=10;spacing=15;labelBackgroundColor=white;labelBorderColor=none" edge="1" parent="1" source="ConfigManager" target="TaskManager">
                  <mxGeometry relative="1" as="geometry"/>
                </mxCell>
                <mxCell id="edge-L_ConfigManager_TaskManager_16_label" value="Configures" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" vertex="1" connectable="0" parent="edge-L_ConfigManager_TaskManager_16">
                  <mxGeometry x="-0.2" y="10" relative="1" as="geometry">
                    <mxPoint as="offset"/>
                  </mxGeometry>
                </mxCell>
<mxCell id="edge-L_PerformanceMonitor_MLFlow_17" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#808080;strokeWidth=2;jumpStyle=arc;jumpSize=10;spacing=15;labelBackgroundColor=white;labelBorderColor=none" edge="1" parent="1" source="PerformanceMonitor" target="MLFlow">
                  <mxGeometry relative="1" as="geometry"/>
                </mxCell>
                <mxCell id="edge-L_PerformanceMonitor_MLFlow_17_label" value="Tracks" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" vertex="1" connectable="0" parent="edge-L_PerformanceMonitor_MLFlow_17">
                  <mxGeometry x="-0.2" y="10" relative="1" as="geometry">
                    <mxPoint as="offset"/>
                  </mxGeometry>
                </mxCell>
<mxCell id="edge-L_GeminiContainer_KnowledgeManager_18" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#808080;strokeWidth=2;jumpStyle=arc;jumpSize=10;spacing=15;labelBackgroundColor=white;labelBorderColor=none" edge="1" parent="1" source="GeminiContainer" target="KnowledgeManager">
                  <mxGeometry relative="1" as="geometry"/>
                </mxCell>
                <mxCell id="edge-L_GeminiContainer_KnowledgeManager_18_label" value="Uses" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" vertex="1" connectable="0" parent="edge-L_GeminiContainer_KnowledgeManager_18">
                  <mxGeometry x="-0.2" y="10" relative="1" as="geometry">
                    <mxPoint as="offset"/>
                  </mxGeometry>
                </mxCell>
<mxCell id="edge-L_OllamaContainer_KnowledgeManager_19" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#808080;strokeWidth=2;jumpStyle=arc;jumpSize=10;spacing=15;labelBackgroundColor=white;labelBorderColor=none" edge="1" parent="1" source="OllamaContainer" target="KnowledgeManager">
                  <mxGeometry relative="1" as="geometry"/>
                </mxCell>
                <mxCell id="edge-L_OllamaContainer_KnowledgeManager_19_label" value="Uses" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" vertex="1" connectable="0" parent="edge-L_OllamaContainer_KnowledgeManager_19">
                  <mxGeometry x="-0.2" y="10" relative="1" as="geometry">
                    <mxPoint as="offset"/>
                  </mxGeometry>
                </mxCell>
<mxCell id="edge-L_LMStudioContainer_KnowledgeManager_20" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#808080;strokeWidth=2;jumpStyle=arc;jumpSize=10;spacing=15;labelBackgroundColor=white;labelBorderColor=none" edge="1" parent="1" source="LMStudioContainer" target="KnowledgeManager">
                  <mxGeometry relative="1" as="geometry"/>
                </mxCell>
                <mxCell id="edge-L_LMStudioContainer_KnowledgeManager_20_label" value="Uses" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" vertex="1" connectable="0" parent="edge-L_LMStudioContainer_KnowledgeManager_20">
                  <mxGeometry x="-0.2" y="10" relative="1" as="geometry">
                    <mxPoint as="offset"/>
                  </mxGeometry>
                </mxCell>
            </root>
          </mxGraphModel>
        </diagram>
      </mxfile>
````

## File: Progress.md

````markdown
# Project Progress

## Completed Features
- ✅ Implemented Gemini crew with proper error handling and tools
- ✅ Implemented LM Studio crew with OpenAI-compatible endpoint
- ✅ Created shared tool infrastructure with ToolFactory
- ✅ Added MLflow integration for both models
- ✅ Implemented proper logging and error handling

## Current Status
- Both Gemini and LM Studio crews are ready for use
- Tools infrastructure is in place with web search, file analysis, and knowledge base tools
- MLflow tracking is configured for model performance comparison

## Next Steps
1. Complete knowledge base tool implementation for better information sharing
2. Enhance validation and testing tools
3. Implement advanced analysis and insight generation features
4. Add parallel execution support for model comparison
5. Implement proper MLflow metrics tracking with PostgreSQL backend correctly integrated
6. Enhance agent memory configuration with proper 1M token context window support
7. Implement efficient parallel processing between Gemini Flash and LM Studio models
8. Add selenium search tool integration with proper error handling and retries
9. Complete structured thinking implementation with new Gemini 2.0 experimental thinking mode
10. Update code execution capabilities to utilize Gemini Flash's native code execution
11. Create proper knowledge base structure for sharing context between models
12. Add proper model fallback logic between Flash and LM Studio
13. Implement config validation to ensure environment variables are properly set
14. Add performance monitoring dashboard for real-time model comparison

## Usage
To run analysis with either model:
```bash
python -m src.ollama.main --model gemini --topic "Your topic"
# or
python -m src.ollama.main --model lmstudio --topic "Your topic"
```

## Environment Setup
1. Copy .env.example to .env
2. Set GEMINI_API_KEY for Gemini usage
3. Configure LM Studio endpoint (default: http://localhost:1234)
4. Start MLflow server with PostgreSQL backend
5. Set required environment variables:
   - MLFLOW_TRACKING_URI
   - GEMINI_API_KEY
   - LANGCHAIN_API_KEY
6. Configure LM Studio (optional):
   - LMSTUDIO_API_URL
   - LMSTUDIO_MODEL

## Required Dependencies
```bash
# Core dependencies
pip install crewai langchain langgraph mlflow psycopg2-binary selenium
# Additional tools
pip install google-generativeai pillow python-dotenv pyyaml requests webdriver-manager
```
````

## File: pyproject.toml

````toml
[project]
name = "ollama"
version = "0.1.0"
description = "ollama using crewAI"
authors = [{ name = "Your Name", email = "you@example.com" }]
requires-python = ">=3.10,<3.13"
dependencies = [
    "crewai[tools]>=0.108.0,<1.0.0"
]

[project.scripts]
ollama = "ollama.main:run"
run_crew = "ollama.main:run"
train = "ollama.main:train"
replay = "ollama.main:replay"
test = "ollama.main:test"

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.crewai]
type = "crew"
````

## File: requirements.txt

````
selenium>=4.18.1
webdriver-manager>=4.0.1
requests>=2.31.0
google-generativeai>=0.3.2
python-dotenv>=1.0.1
mlflow>=2.10.2
crewai>=0.16.1
langchain>=0.1.9
pyyaml>=6.0.1
psycopg2-binary>=2.9.9
psutil>=5.9.8
````

## File: src/ollama/config/__init__.py

````python
def load_model_config() -> Dict
⋮----
config_path = Path(__file__).parent / "models.yaml"
⋮----
def load_mlflow_config() -> Dict
⋮----
config_path = Path(__file__).parent / "mlflow_config.yaml"
````

## File: src/ollama/config/models.yaml

````yaml
gemini:
  model_config:
    name: ${GEMINI_MODEL}
    temperature: 0.7
    top_p: 0.95
    max_tokens: 8192
  agents:
    researcher:
      model_name: "gemini-pro"
      temperature: 0.5
    analyzer:
      model_name: "gemini-pro"
      temperature: 0.3
    validator:
      model_name: "gemini-pro"
      temperature: 0.2

lmstudio:
  model_config:
    name: ${LMSTUDIO_MODEL}
    temperature: 0.7
    top_p: 0.95
    max_tokens: 2048
    api_base: ${LMSTUDIO_API_URL}
  agents:
    researcher:
      model_name: "gemma-3-4b-it"
      temperature: 0.5
    analyzer:
      model_name: "gemma-3-4b-it"
      temperature: 0.3
    validator:
      model_name: "gemma-3-4b-it"
      temperature: 0.2

ollama:
  model_config:
    name: ${OLLAMA_MODEL}
    temperature: 0.7
    top_p: 0.95
    max_tokens: 2048
  agents:
    researcher:
      model_name: "gemma:3b"
      temperature: 0.5
    analyzer:
      model_name: "gemma:3b"
      temperature: 0.3
    validator:
      model_name: "gemma:3b"
      temperature: 0.2

models:
  gemini_flash:
    name: "models/gemini-2.0-flash"
    context_window: 1048576
    max_tokens: 8192
    settings:
      temperature: 0.7
      top_p: 0.95
      presence_penalty: 0.0
      frequency_penalty: 0.0
    features:
      - structured_output
      - function_calling
      - code_execution
      - search
      - tool_use
      - thinking
    experimental:
      - image_generation
      - live_api
      - thinking

  gemini_flash_lite:
    name: "models/gemini-2.0-flash-lite"
    context_window: 1048576
    max_tokens: 8192
    settings:
      temperature: 0.6
      top_p: 0.9
      presence_penalty: 0.0
      frequency_penalty: 0.0
    features:
      - structured_output
      - function_calling
      - code_execution
      - search
      - tool_use
      - thinking
    experimental:
      - image_generation
      - live_api
      - thinking

  lmstudio:
    name: "${LMSTUDIO_MODEL}"
    context_window: 4096
    max_tokens: 2048
    settings:
      temperature: 0.7
      top_p: 0.95
      presence_penalty: 0.0
      frequency_penalty: 0.0
    api:
      base_url: "${LMSTUDIO_API_URL}"
      version: "v1"
      endpoints:
        chat: "/chat/completions"
        completion: "/completions"
        embedding: "/embeddings"

  lmstudio_emb:
    name: "text-embedding-nomic-embed-text-v1.5"
    context_window: 4096
    max_tokens: 2048
    api:
      base_url: "${LMSTUDIO_API_URL}"
      version: "v1"
      endpoint: "/embeddings"

model_assignments:
  default: "gemini_flash"
  research:
    primary: "gemini_flash"
    fallback: "gemini_flash_lite"
  analysis:
    primary: "gemini_flash_lite"
    fallback: "lmstudio"
  code:
    primary: "lmstudio"
    fallback: "gemini_flash"
  embedding:
    primary: "lmstudio_emb"
    fallback: null

validation:
  required_settings:
    - temperature
    - top_p
    - max_tokens
  required_features:
    gemini:
      - structured_output
      - function_calling
    lmstudio:
      - chat
      - completion
````

## File: src/ollama/config/search_tools.yaml

````yaml
selenium:
  default: true
  timeout: 10
  max_results: 5
  headless: true
  retry_attempts: 3
  retry_delay: 2
  user_agent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
  selectors:
    result_container: "div.g"
    title: "h3"
    link: "a"
    snippet: "div.VwiC3b"

serper:
  default: false
  max_results: 5
  timeout: 5
  retry_attempts: 2
  retry_delay: 1
  endpoints:
    search: "https://google.serper.dev/search"
    news: "https://google.serper.dev/news"
    places: "https://google.serper.dev/places"

mlflow:
  experiment_name: "search_performance_monitoring"
  metrics:
    - name: "search_time"
      unit: "seconds"
    - name: "results_count"
      unit: "count"
    - name: "success_rate"
      unit: "percentage"
  params:
    - "search_tool"
    - "query"
    - "max_results"
    - "timeout"

knowledge:
  storage:
    path: "search_results"
    format: "json"
    max_age_days: 7
  analysis:
    track_sources: true
    track_performance: true
    track_queries: true
````

## File: src/ollama/config/tools.yaml

````yaml
web_search:
  name: "web_search"
  description: "Search the web for information"
  args:
    api_key: ${SERPER_API_KEY}
    max_results: 5

file_analyzer:
  name: "file_analyzer"
  description: "Analyze file contents"
  args:
    supported_formats: ["txt", "md", "py", "json", "yaml"]
    max_file_size: 10485760  # 10MB

knowledge_base:
  name: "knowledge_base"
  description: "Access and query knowledge base"
  args:
    base_path: "./knowledge"
    index_type: "simple"

structured_analysis:
  name: "structured_analysis"
  description: "Perform structured analysis of information"
  args:
    formats: ["xml", "json", "yaml"]
    validation: true

validation_tool:
  name: "validation_tool"
  description: "Validate analysis results"
  args:
    criteria:
      - completeness
      - accuracy
      - relevance
    threshold: 0.8

insight_generator:
  name: "insight_generator"
  description: "Generate insights from analysis"
  args:
    formats: ["markdown", "json"]
    max_insights: 10
    min_confidence: 0.7

advanced_reasoning:
  name: "advanced_reasoning"
  description: "Enhanced reasoning and analysis capabilities"
  args:
    analysis_levels: ["basic", "detailed", "comprehensive"]
    thinking_patterns: ["system", "meta", "future"]
    validation: true

multimodal_analysis:
  name: "multimodal_analysis"
  description: "Advanced multimodal content analysis"
  args:
    supported_types: ["text", "image", "audio", "video"]
    max_input_size: 104857600  # 100MB
    parallel_processing: true

thinking_mode:
  name: "thinking_mode"
  description: "Control model's thinking approach"
  args:
    modes: ["standard", "enhanced", "experimental"]
    default_mode: "enhanced"
    features:
      - "context_understanding"
      - "pattern_recognition"
      - "hypothesis_generation"
      - "validation"

tool_use:
  name: "tool_use"
  description: "Native tool use capabilities"
  args:
    supported_tools: ["code", "search", "analysis", "generation"]
    max_tools_per_request: 5
    timeout: 30  # seconds

code_generation:
  name: "code_generation"
  description: "Advanced code generation and analysis"
  args:
    languages: ["python", "javascript", "typescript", "go", "java"]
    max_context_size: 32768
    include_tests: true
    optimization_levels: ["basic", "advanced"]

image_generation:
  name: "image_generation"
  description: "Experimental image generation capabilities"
  args:
    max_size: [2048, 2048]
    formats: ["pil", "jpeg", "png"]
    styles: ["natural", "artistic", "photographic"]
    experimental: true

audio_generation:
  name: "audio_generation"
  description: "Coming soon: Audio generation capabilities"
  args:
    formats: ["wav", "mp3"]
    voices: ["default"]
    max_duration: 300  # seconds
    status: "coming_soon"
````

## File: src/ollama/crews/model_crews.py

````python
logger = logging.getLogger(__name__)
⋮----
class BaseModelCrew
⋮----
def __init__(self, topic: str = "AI and machine learning")
⋮----
def _setup_llm(self) -> Optional[LLM]
⋮----
def _create_agents(self) -> Dict[str, Agent]
⋮----
def _create_tasks(self) -> List[Task]
⋮----
tasks = [
⋮----
def run(self) -> Dict[str, Any]
⋮----
agents = self._create_agents()
tasks = self._create_tasks()
⋮----
crew = Crew(
⋮----
result = crew.kickoff()
⋮----
error_result = {
⋮----
def _save_output(self, result: Dict[str, Any]) -> None
⋮----
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_file = self.output_dir / f"{self.__class__.__name__}_{timestamp}.json"
⋮----
def _get_tools_for_agent(self, tool_names: List[str])
⋮----
class GeminiCrew(BaseModelCrew)
⋮----
def __init__(self, *args, **kwargs)
⋮----
def _setup_llm(self) -> LLM
⋮----
api_key = os.getenv("GEMINI_API_KEY")
⋮----
# Configure model based on type
⋮----
max_tokens = int(os.getenv("GEMINI_2_5_MAX_TOKENS", "32768"))
context_window = int(os.getenv("GEMINI_2_5_CONTEXT_WINDOW", "1000000"))
⋮----
max_tokens = int(os.getenv("GEMINI_MAX_TOKENS", "8192"))
context_window = int(os.getenv("GEMINI_CONTEXT_WINDOW", "1000000"))
⋮----
# Set agent configurations based on model capabilities
researcher_config = {
analyzer_config = {
⋮----
# Add enhanced capabilities for 2.5 Pro
⋮----
class LMStudioCrew(BaseModelCrew)
⋮----
api_base = os.getenv("LMSTUDIO_API_URL", "http://localhost:1234")
model = os.getenv("LMSTUDIO_MODEL", "gemma-3-4b-it")
⋮----
model=f"openai/{model}",  # LM Studio uses OpenAI-compatible endpoint
````

## File: src/ollama/knowledge/integration.py

````python
logger = logging.getLogger(__name__)
⋮----
class KnowledgeIntegration
⋮----
def __init__(self, base_path: str = "./knowledge")
⋮----
def get_model_config(self, model_id: str) -> Optional[Dict]
⋮----
"""Get model-specific configuration and capabilities"""
capabilities = self.manager.get_model_capabilities(model_id)
⋮----
def _enrich_model_config(self, capabilities: Dict) -> Dict
⋮----
"""Enrich model config with best practices and optimization"""
model_id = capabilities.get("model_id")
⋮----
# Get related knowledge entries
best_practices = self.manager.search_entries(
⋮----
# Enrich with additional context
⋮----
def _get_recommended_templates(self, capabilities: Dict) -> List[str]
⋮----
"""Find templates that work well with model capabilities"""
templates = []
⋮----
def get_prompt_template(self, template_id: str) -> Optional[Dict]
⋮----
"""Get prompt template with enriched context"""
template = self.manager.get_entry("prompt-templates", template_id)
⋮----
# Add related entries and usage examples
related = self.manager.search_entries(
⋮----
def validate_model_compatibility(self, template_id: str, model_id: str) -> bool
⋮----
"""Check if template is compatible with model"""
⋮----
# Check compatibility based on features needed
model_features = capabilities.get("capabilities", {})
required_features = template.get("required_capabilities", [])
⋮----
def get_domain_knowledge(self, domain: str) -> List[Dict]
⋮----
"""Get domain-specific knowledge entries"""
⋮----
def update_model_performance(self, model_id: str, metrics: Dict) -> bool
⋮----
"""Update model performance metrics"""
⋮----
def get_optimization_tips(self, model_id: str) -> List[str]
⋮----
"""Get model-specific optimization tips"""
````

## File: src/ollama/knowledge/manager.py

````python
logger = logging.getLogger(__name__)
⋮----
class KnowledgeManager
⋮----
def __init__(self, base_path: str = "./knowledge")
⋮----
def _setup_mlflow(self)
⋮----
def _load_config(self) -> Dict
⋮----
def _load_categories(self) -> Dict
⋮----
def _load_schema(self) -> Dict
⋮----
def _validate_structure(self) -> None
⋮----
required_dirs = ["schemas", "templates", "model-specific", "prompt-templates"]
⋮----
def store_entry(self, category: str, entry_id: str, content: Dict) -> bool
⋮----
path = self._get_entry_path(category, entry_id)
⋮----
def get_entry(self, category: str, entry_id: str) -> Optional[Dict]
⋮----
def list_entries(self, category: str) -> List[str]
⋮----
path = self.base_path / category
⋮----
def get_category_info(self, category: str) -> Optional[Dict]
⋮----
def _get_entry_path(self, category: str, entry_id: str) -> Path
⋮----
def _validate_entry(self, content: Dict) -> bool
⋮----
# Basic validation - could be expanded with JSON Schema validation
required_fields = self.schema["required"]
⋮----
def search_entries(self, query: str, categories: Optional[List[str]] = None) -> List[Dict]
⋮----
results = []
search_categories = categories or list(self.categories.keys())
⋮----
entries = self.list_entries(category)
⋮----
entry = self.get_entry(category, entry_id)
⋮----
def _matches_query(self, entry: Dict, query: str) -> bool
⋮----
# Simple text matching - could be enhanced with better search
query = query.lower()
searchable_text = json.dumps(entry).lower()
⋮----
def update_model_capabilities(self, model_id: str, capabilities: Dict) -> bool
⋮----
template_path = self.base_path / "templates" / "model-capabilities.yaml"
⋮----
template = yaml.safe_load(f)
⋮----
# Validate capabilities against template
⋮----
def get_model_capabilities(self, model_id: str) -> Optional[Dict]
⋮----
def store_search_results(self, query: str, results: List[Dict], source: str) -> bool
⋮----
results_path = self.base_path / "search_results"
⋮----
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
file_path = results_path / f"search_{timestamp}.json"
⋮----
search_data = {
⋮----
"""Get recent search results with optional filtering"""
⋮----
files = sorted(
⋮----
history = []
⋮----
data = json.load(f)
⋮----
"""Analyze search performance metrics"""
⋮----
history = self.get_search_history(source=source, limit=1000)
⋮----
metrics = {
⋮----
source = entry["source"]
````

## File: src/ollama/knowledge/search.py

````python
logger = logging.getLogger(__name__)
⋮----
@dataclass
class SearchResult
⋮----
category: str
entry_id: str
title: str
relevance: float
content: Dict[str, Any]
metadata: Dict[str, Any]
⋮----
class KnowledgeSearch
⋮----
def __init__(self, base_path: str = "./knowledge")
⋮----
def _load_latest_index(self) -> Dict
⋮----
index_files = list(self.index_path.glob("index_*.json"))
⋮----
latest = max(index_files, key=lambda x: x.stat().st_mtime)
⋮----
def refresh_index(self) -> None
⋮----
"""Update the search index"""
new_index = {}
⋮----
category_path = self.base_path / category
⋮----
content = f.read()
entry_id = file.stem
⋮----
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
index_file = self.index_path / f"index_{timestamp}.json"
⋮----
"""Search the knowledge base"""
results = []
query = query.lower()
⋮----
content = entry["content"].lower()
⋮----
# Simple relevance score based on word frequency
relevance = content.count(query) / len(content.split())
⋮----
# Sort by relevance and limit results
⋮----
def get_related(self, entry_id: str, limit: int = 5) -> List[SearchResult]
⋮----
"""Find related knowledge entries"""
⋮----
entry = self.latest_index[entry_id]
content_words = set(entry["content"].lower().split())
⋮----
other_words = set(other_entry["content"].lower().split())
# Calculate similarity based on word overlap
similarity = len(content_words & other_words) / len(content_words | other_words)
⋮----
def get_recent_updates(self, days: int = 7) -> List[Dict]
⋮----
"""Get recently updated entries"""
cutoff = datetime.now().timestamp() - (days * 24 * 60 * 60)
recent = []
⋮----
updated = datetime.fromisoformat(entry["updated"]).timestamp()
````

## File: src/ollama/templates/code_templates.xml

````xml
<?xml version="1.0" encoding="UTF-8"?>
<templates>
    <code_execution>
        <template>
            <![CDATA[
            Execute and analyze the following code:
            {code}
            Consider these aspects:
            - Code correctness
            - Performance implications
            - Security considerations
            - Best practices
            ]]>
        </template>
        <validation>
            <criteria>
                <security>Check for security vulnerabilities</security>
                <performance>Analyze computational efficiency</performance>
                <quality>Evaluate code quality and style</quality>
            </criteria>
        </validation>
    </code_execution>

    <vision_analysis>
        <template>
            <![CDATA[
            Analyze the code or diagram in this image:
            {image_context}
            Focus on:
            - Code structure
            - Design patterns
            - Flow logic
            - Implementation details
            ]]>
        </template>
        <output_format>
            <structure>
                <code_elements>List of identified code elements</code_elements>
                <patterns>Detected design patterns</patterns>
                <flow>Control flow analysis</flow>
                <recommendations>Improvement suggestions</recommendations>
            </structure>
        </output_format>
    </vision_analysis>

    <code_generation>
        <template>
            <![CDATA[
            Generate code based on the following requirements:
            {requirements}
            Use these parameters:
            - Language: {language}
            - Style: {style}
            - Constraints: {constraints}
            ]]>
        </template>
        <parameters>
            <language type="choice">python,javascript,typescript,go</language>
            <style type="choice">functional,object-oriented,procedural</style>
            <constraints type="object">
                <max_complexity>specified maximum cyclomatic complexity</max_complexity>
                <patterns>required design patterns</patterns>
                <testing>testing requirements</testing>
            </constraints>
        </parameters>
    </code_generation>
</templates>
````

## File: src/ollama/templates/multimodal_templates.xml

````xml
<?xml version="1.0" encoding="UTF-8"?>
<templates>
    <multimodal_analysis>
        <image_analysis>
            <template><![CDATA[
                Analyze the following image content:
                {image_content}
                Provide analysis considering:
                - Visual elements
                - Technical patterns
                - Context interpretation
                - Related concepts
            ]]></template>
            <parameters>
                <format>image/*, video/*, application/pdf</format>
                <max_size>20971520</max_size>
                <supported_types>png,jpg,jpeg,gif,pdf,mp4</supported_types>
            </parameters>
        </image_analysis>

        <video_analysis>
            <template><![CDATA[
                Analyze video content frame by frame:
                {video_content}
                Focus on:
                - Temporal patterns
                - Motion analysis
                - Scene understanding
                - Technical details
            ]]></template>
            <parameters>
                <max_duration>300</max_duration>
                <frame_rate>30</frame_rate>
                <formats>mp4,mov,avi</formats>
            </parameters>
        </video_analysis>

        <audio_analysis>
            <template><![CDATA[
                Process audio input:
                {audio_content}
                Analyze:
                - Audio patterns
                - Signal characteristics
                - Content interpretation
            ]]></template>
            <parameters>
                <formats>mp3,wav,ogg</formats>
                <max_duration>600</max_duration>
                <sample_rate>44100</sample_rate>
            </parameters>
        </audio_analysis>

        <diagram_understanding>
            <template><![CDATA[
                Interpret diagram content:
                {diagram_content}
                Extract:
                - Structure relationships
                - Flow patterns
                - Technical components
                - Implementation insights
            ]]></template>
            <parameters>
                <diagram_types>flowchart,uml,er,sequence</diagram_types>
                <output_format>json,xml,markdown</output_format>
            </parameters>
        </diagram_understanding>
    </multimodal_analysis>
</templates>
````

## File: src/ollama/tools/advanced_tools.py

````python
class AdvancedReasoningTool(Tool)
⋮----
def __init__(self)
⋮----
def analyze(self, content: Dict[str, Any], depth: str = "comprehensive") -> Dict[str, Any]
⋮----
"""Implements Gemini 2.5's enhanced reasoning capabilities"""
⋮----
analysis_levels = {
⋮----
def _generate_insights(self, content: Dict[str, Any], depth: str) -> List[Dict]
⋮----
# Implementation for different analysis depths
⋮----
class MultimodalAnalysisTool(Tool)
⋮----
def process(self, inputs: Dict[str, Any]) -> Dict[str, Any]
⋮----
"""Process multiple types of inputs (text, images, audio, video)"""
supported_types = ["text", "image", "audio", "video"]
results = {}
⋮----
def _analyze_content(self, content_type: str, content: Any) -> Dict[str, Any]
⋮----
# Implementation for different content types
⋮----
class ThinkingModeTool(Tool)
⋮----
def __init__(self, mode: str = "enhanced")
⋮----
def apply_thinking(self, content: str) -> Dict[str, Any]
⋮----
"""Apply specific thinking patterns based on mode"""
modes = {
⋮----
think_func = modes.get(self.mode, self._enhanced_thinking)
⋮----
def _standard_thinking(self, content: str) -> Dict[str, Any]
⋮----
def _enhanced_thinking(self, content: str) -> Dict[str, Any]
⋮----
def _experimental_thinking(self, content: str) -> Dict[str, Any]
⋮----
class ToolUseTool(Tool)
⋮----
def use_tool(self, tool_request: Dict[str, Any]) -> Dict[str, Any]
⋮----
"""Handle dynamic tool usage requests"""
tool_type = tool_request.get("type")
parameters = tool_request.get("parameters", {})
⋮----
result = self._execute_tool(tool_type, parameters)
⋮----
def _execute_tool(self, tool_type: str, parameters: Dict[str, Any]) -> Any
⋮----
# Implementation for tool execution
````

## File: src/ollama/tools/agent_tools.py

````python
class WebSearchTool(Tool)
⋮----
def __init__(self, api_key: str, max_results: int = 5)
⋮----
def search(self, query: str) -> List[Dict]
⋮----
headers = {"X-API-KEY": self.api_key}
response = requests.get(
⋮----
class FileAnalyzerTool(Tool)
⋮----
def __init__(self, supported_formats: List[str], max_file_size: int)
⋮----
def analyze(self, file_path: str) -> Dict[str, Any]
⋮----
path = Path(file_path)
⋮----
content = f.read()
⋮----
class KnowledgeBaseTool(Tool)
⋮----
def __init__(self, base_path: str, index_type: str = "simple")
⋮----
def query(self, query: str) -> Dict[str, Any]
⋮----
# Implementation depends on knowledge base structure
⋮----
class StructuredAnalysisTool(Tool)
⋮----
def __init__(self, formats: List[str], validation: bool = True)
⋮----
def analyze(self, content: str, format: str = "json") -> Dict[str, Any]
⋮----
# Add format-specific analysis logic
⋮----
# Add other format handlers
⋮----
class ValidationTool(Tool)
⋮----
def __init__(self, criteria: List[str], threshold: float = 0.8)
⋮----
def validate(self, content: Dict[str, Any]) -> Dict[str, Any]
⋮----
results = {}
⋮----
# Add validation logic for each criterion
⋮----
def _check_criterion(self, content: Dict[str, Any], criterion: str) -> float
⋮----
# Add specific validation logic for each criterion
return 1.0  # Placeholder
⋮----
class InsightGeneratorTool(Tool)
⋮----
def __init__(self, formats: List[str], max_insights: int = 10, min_confidence: float = 0.7)
⋮----
def generate(self, content: Dict[str, Any], format: str = "markdown") -> Dict[str, Any]
⋮----
# Add insight generation logic
insights = self._extract_insights(content)
⋮----
def _extract_insights(self, content: Dict[str, Any]) -> List[Dict[str, Any]]
⋮----
# Add insight extraction logic
return []  # Placeholder
````

## File: src/ollama/tools/coding-tools.py

````python
logger = logging.getLogger(__name__)
⋮----
class CodeExecutor
⋮----
def __init__(self)
⋮----
api_key = os.getenv("GEMINI_API_KEY")
⋮----
@retry_with_backoff(retries=3)
    def execute_code(self, code: str, context: Optional[Dict] = None) -> Dict[str, Any]
⋮----
response = self.model.generate_content([
⋮----
@retry_with_backoff(retries=3)
    def generate_code(self, prompt: str, context: Optional[Dict] = None) -> Dict[str, Any]
⋮----
class CodeVisionAnalyzer
⋮----
def _encode_image(self, image_path: str) -> str
⋮----
@retry_with_backoff(retries=3)
    def analyze_code_image(self, image_path: str) -> Dict[str, Any]
⋮----
img = Image.open(image_path)
response = self.model.generate_content(["Analyze this code image:", img])
⋮----
@retry_with_backoff(retries=3)
    def generate_from_diagram(self, image_path: str, context: Optional[Dict] = None) -> Dict[str, Any]
````

## File: src/ollama/tools/generation_tools.py

````python
class CodeGenerationTool(Tool)
⋮----
def __init__(self)
⋮----
"""Generate code using Gemini's advanced coding capabilities"""
⋮----
# Configure code generation parameters
parameters = {
⋮----
class ImageGenerationTool(Tool)
⋮----
"""Generate images using Gemini's experimental image capabilities"""
⋮----
# Image generation parameters
⋮----
"image": None,  # PIL Image will be here
⋮----
class AudioGenerationTool(Tool)
⋮----
"""Generate audio using upcoming Gemini capabilities"""
````

## File: src/ollama/tools/model_tools.py

````python
class BaseModelTool(ABC)
⋮----
def __init__(self)
⋮----
@abstractmethod
    def execute(self, **kwargs) -> Dict[str, Any]
⋮----
def _get_model(self) -> Optional[Dict]
⋮----
def _handle_fallback(self) -> bool
⋮----
fallback = self.coordinator.get_fallback_model(self.current_model["type"])
⋮----
class TextCompletionTool(BaseModelTool)
⋮----
def execute(self, prompt: str, **kwargs) -> Dict[str, Any]
⋮----
model = self._get_model()
⋮----
response = model["model"].generate_text(prompt, **kwargs)
⋮----
# LM Studio API call implementation
⋮----
class StructuredOutputTool(BaseModelTool)
⋮----
def execute(self, prompt: str, format_schema: Dict, **kwargs) -> Dict[str, Any]
⋮----
response = model["model"].generate_text(
````

## File: src/ollama/tools/search_tools.py

````python
logger = logging.getLogger(__name__)
⋮----
class BaseSearchTool
⋮----
"""Base class for search implementations"""
def search(self, query: str, **kwargs) -> List[Dict]
⋮----
class SeleniumSearchTool(BaseSearchTool)
⋮----
"""Search tool using Selenium with automated WebDriver management"""
def __init__(self, headless: bool = True)
⋮----
def search(self, query: str, max_results: int = 5, timeout: int = 10) -> List[Dict]
⋮----
start_time = time.time()
driver = None
results = []
⋮----
driver = WebDriverManager.get_chrome_driver(headless=self.headless)
search_url = f"https://www.google.com/search?q={query}"
⋮----
search_results = driver.find_elements(By.CSS_SELECTOR, "div.g")
⋮----
title = result.find_element(By.CSS_SELECTOR, "h3").text
link = result.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
snippet = result.find_element(By.CSS_SELECTOR, "div.VwiC3b").text
⋮----
execution_time = time.time() - start_time
⋮----
class SerperSearchTool(BaseSearchTool)
⋮----
"""Search tool using Serper API"""
def __init__(self)
⋮----
def search(self, query: str, max_results: int = 5) -> List[Dict]
⋮----
headers = {
response = requests.get(
⋮----
results = response.json()["organic"]
⋮----
class SearchManager
⋮----
"""Manager for coordinating different search tools"""
⋮----
def _setup_mlflow(self)
⋮----
"""
        Perform search using specified tool
        Args:
            query: Search query
            tool: "selenium" or "serper"
            max_results: Maximum number of results
        """
⋮----
results = self.selenium_search.search(query, max_results=max_results)
⋮----
results = self.serper_search.search(query, max_results=max_results)
⋮----
"""Run searches in parallel using all available tools"""
⋮----
results = {}
⋮----
# Add Selenium results
⋮----
# Add Serper results if available
````

## File: src/ollama/tools/serperdevtool.py

````python
class SerperSearchInput(BaseModel)
⋮----
"""Input schema for Serper.dev search."""
query: str = Field(..., description="Search query")
search_type: str = Field(
num_results: int = Field(default=10, description="Number of results to return")
include_domains: Optional[List[str]] = Field(
exclude_domains: Optional[List[str]] = Field(
⋮----
class SerperDevTool(BaseTool)
⋮----
name: str = "serper_search_tool"
description: str = "Perform web searches using Serper.dev API"
args_schema: Type[BaseModel] = SerperSearchInput
⋮----
def __init__(self)
⋮----
"""
        Perform search using Serper.dev API with advanced filtering
        """
headers = {
⋮----
# Build search parameters
params = {
⋮----
# Add domain filters if specified
⋮----
# Determine endpoint based on search type
endpoint = f"/{search_type}"
⋮----
response = requests.post(
⋮----
results = response.json()
⋮----
# Add metadata to results
⋮----
class SerperNewsInput(BaseModel)
⋮----
"""Input schema for news search."""
query: str = Field(..., description="News search query")
time_range: str = Field(
sort_by: str = Field(
⋮----
class SerperNewsTool(SerperDevTool)
⋮----
name: str = "serper_news_tool"
description: str = "Search news articles using Serper.dev API"
args_schema: Type[BaseModel] = SerperNewsInput
⋮----
"""
        Perform news search with time range and sorting options
        """
````

## File: src/ollama/tools/tool_factory.py

````python
class ToolFactory
⋮----
def __init__(self)
⋮----
def _load_config(self) -> Dict
⋮----
config_path = Path(__file__).parent.parent / "config" / "tools.yaml"
⋮----
def get_tool(self, tool_name: str)
⋮----
config = self.config.get(tool_name)
⋮----
tool = self._create_tool(tool_name, config)
⋮----
def _create_tool(self, name: str, config: Dict)
⋮----
# Basic tools
⋮----
# Generation tools
⋮----
# Advanced Gemini 2.5 tools
⋮----
def get_tools_for_agent(self, tool_names: List[str])
````

## File: src/ollama/utils/knowledge_manager.py

````python
class KnowledgeManager
⋮----
def __init__(self, base_path: str = "./knowledge")
⋮----
def _initialize_structure(self)
⋮----
def store_knowledge(self, key: str, data: Any, model_type: Optional[str] = None)
⋮----
path = self.base_path / model_type / f"{key}.json"
⋮----
path = self.base_path / "shared" / f"{key}.json"
⋮----
def get_knowledge(self, key: str, model_type: Optional[str] = None) -> Optional[Any]
⋮----
data = json.load(f)
⋮----
def list_knowledge(self, model_type: Optional[str] = None) -> List[str]
⋮----
path = self.base_path / model_type
⋮----
path = self.base_path / "shared"
⋮----
def share_knowledge(self, key: str, source_model: str)
⋮----
data = self.get_knowledge(key, source_model)
````

## File: src/ollama/utils/lmstudio_client.py

````python
class LMStudioClient
⋮----
def __init__(self)
⋮----
def generate_text(self, prompt: str, **kwargs) -> Dict[str, Any]
⋮----
headers = {"Content-Type": "application/json"}
data = {
⋮----
response = requests.post(
⋮----
def chat_completion(self, messages: list, **kwargs) -> Dict[str, Any]
⋮----
def get_model_info(self) -> Optional[Dict[str, Any]]
⋮----
response = requests.get(f"{self.api_url}/v1/models")
````

## File: src/ollama/utils/model_analyzer.py

````python
class ModelAnalyzer
⋮----
def __init__(self)
⋮----
def get_model_metrics(self, model_type: str, days: int = 7) -> Dict[str, Any]
⋮----
experiment = mlflow.get_experiment_by_name(self.experiments[model_type])
⋮----
runs = mlflow.search_runs(
⋮----
metrics = {
⋮----
def compare_models(self, days: int = 7) -> Dict[str, Dict]
⋮----
results = {}
⋮----
metrics = self.get_model_metrics(model_type, days)
⋮----
def get_performance_trends(self, model_type: str, metric: str, days: int = 7) -> List[Dict]
⋮----
df = pd.DataFrame({
⋮----
df = df.sort_values("timestamp")
````

## File: src/ollama/utils/model_clients.py

````python
class GeminiClient
⋮----
def __init__(self)
⋮----
def generate_text(self, prompt: str, **kwargs) -> Dict[str, Any]
⋮----
response = self.model.generate_content(prompt)
⋮----
def chat_completion(self, messages: List[Dict[str, str]], **kwargs) -> Dict[str, Any]
⋮----
chat = self.model.start_chat(history=[])
response = chat.send_message(messages[-1]["content"])
⋮----
def search_and_generate(self, query: str, search_tool: str = "selenium") -> Dict[str, Any]
⋮----
# First perform web search
search_results = self.search_manager.search(query, tool=search_tool)
⋮----
# Format search results for model context
context = "Based on these search results:\n"
⋮----
# Generate response with search context
response = self.model.generate_content(f"{context}\n\nAnalyze and summarize the information about: {query}")
⋮----
class LMStudioClient
⋮----
response = requests.post(
⋮----
response = self.generate_text(f"{context}\n\nAnalyze and summarize the information about: {query}")
````

## File: src/ollama/utils/model_coordinator.py

````python
class ModelCoordinator
⋮----
def __init__(self)
⋮----
def get_available_models(self) -> List[str]
⋮----
available = []
⋮----
def get_primary_model(self) -> Optional[Dict]
⋮----
available = self.get_available_models()
⋮----
primary = available[0]
⋮----
def get_fallback_model(self, failed_type: str) -> Optional[Dict]
⋮----
current_index = available.index(failed_type)
⋮----
next_type = available[current_index + 1]
````

## File: src/ollama/utils/model_utils.py

````python
class ModelManager
⋮----
def __init__(self)
⋮----
def _initialize_clients(self)
⋮----
# Initialize Gemini
api_key = os.getenv("GEMINI_API_KEY")
⋮----
# Initialize LM Studio
⋮----
def get_gemini_model(self, model_name: Optional[str] = None) -> genai.GenerativeModel
⋮----
model = model_name or self.default_model
generation_config = {
⋮----
def get_lmstudio_model(self, model_name: Optional[str] = None) -> Dict
⋮----
model = model_name or os.getenv("LMSTUDIO_MODEL", "gemma-3-4b-it")
⋮----
def validate_model_config(self, model_type: str) -> bool
⋮----
response = requests.get(f"{self.lmstudio_url}/v1/models")
````

## File: src/ollama/utils/progress_tracker.py

````python
class ProgressTracker
⋮----
def __init__(self, model_type: str)
⋮----
def start_run(self)
⋮----
experiment = f"{self.model_type}_crew_monitoring"
⋮----
def log_metric(self, key: str, value: float, step: int = None)
⋮----
def log_execution(self, task_name: str, success: bool, **metrics)
⋮----
execution_time = time.time() - self.start_time
⋮----
def get_summary(self) -> Dict[str, Any]
````

## File: src/ollama/utils/retry_utils.py

````python
logger = logging.getLogger(__name__)
⋮----
def decorator(func: Callable)
⋮----
@wraps(func)
        def wrapper(*args, **kwargs)
⋮----
delay = initial_delay
last_exception = None
⋮----
last_exception = e
⋮----
sleep_time = delay * (backoff_factor ** attempt)
````

## File: src/ollama/utils/template_loader.py

````python
logger = logging.getLogger(__name__)
⋮----
class TemplateLoader
⋮----
def __init__(self, template_dir: str = "../templates")
⋮----
def load_templates(self, template_type: str) -> Dict[str, Any]
⋮----
"""Load templates by type (code or multimodal)"""
⋮----
template_path = self.template_dir / "code_templates.xml"
⋮----
template_path = self.template_dir / "multimodal_templates.xml"
⋮----
tree = ET.parse(template_path)
root = tree.getroot()
⋮----
templates = {}
⋮----
def _parse_template_section(self, element: ET.Element) -> Dict
⋮----
"""Parse XML template section"""
result = {}
⋮----
# Extract CDATA content
⋮----
def get_template(self, template_type: str, category: str, section: Optional[str] = None) -> Optional[Dict]
⋮----
"""Get specific template by type, category and section"""
templates = self.load_templates(template_type)
⋮----
def validate_parameters(self, template_type: str, category: str, parameters: Dict) -> bool
⋮----
"""Validate parameters against template requirements"""
template = self.get_template(template_type, category)
⋮----
required_params = template["parameters"]
````

## File: src/ollama/utils/webdriver_utils.py

````python
logger = logging.getLogger(__name__)
⋮----
class WebDriverManager
⋮----
@staticmethod
    def get_chrome_driver(headless: bool = True) -> webdriver.Chrome
⋮----
chrome_options = Options()
⋮----
# Auto-install/update ChromeDriver
service = Service(ChromeDriverManager().install())
````

## File: knowledge/categories.yaml

````yaml
# Knowledge Base Categories
model_specific:
  gemini:
    - gemini-pro
    - gemini-vision
    - gemini-ultra
    - gemini-embedding
    subcategories:
      - prompts
      - performance
      - limitations
      - use-cases
  ollama:
    - gemma-3:4b
    subcategories:
      - prompts
      - performance
      - limitations
      - use-cases
  lmstudio:
    - gemma-3-4b-it
    subcategories:
      - prompts
      - performance
      - limitations
      - use-cases

prompt_templates:
  reasoning:
    - system-prompts
    - chain-of-thought
    - structured-thinking
  research:
    - data-collection
    - analysis-patterns
    - synthesis
  creative:
    - generation
    - innovation
    - brainstorming
  technical:
    - code-generation
    - system-design
    - documentation

domain_knowledge:
  machine_learning:
    - architectures
    - training
    - deployment
    - optimization
  software_engineering:
    - patterns
    - practices
    - tools
    - frameworks
  data_science:
    - analysis
    - visualization
    - statistics
    - pipelines

relationships:
  - source: prompt_templates/reasoning
    target: model_specific/gemini/prompts
    type: implementation
  - source: domain_knowledge/machine_learning
    target: model_specific/gemini/performance
    type: reference
  - source: prompt_templates/technical
    target: domain_knowledge/software_engineering
    type: application
````

## File: src/ollama/__init__.py

````python
__version__ = "2.0.0"
__all__ = ["GeminiCrew", "LMStudioCrew", "ToolFactory"]
````

## File: src/ollama/config/agents.yaml

````yaml
# This file defines the agents used in the Ollama system.

# Base prompt master configuration - used as template for specialized agents
prompt_master_base:
  base_config: true  # Flag to identify this as a base template
  role_template: >
    Expert {specialization} Engineer with systematic XML-based thinking patterns and {domain_expertise}
  goal_template: >
    Apply structured thinking frameworks using XML tags and CDATA sections to {objective}
  backstory_template: >
    Expert in cognitive frameworks and systematic problem-solving with {experience_years}+ years
    developing structured analysis patterns that improve solution quality by {percentage}%

# Specialized Prompt Engineering Agents
prompt_engineer:
  inherits: prompt_master_base
  role: >
    {specialization|Strategic} Prompt {seniority|Architect} with expertise in {domain_expertise|system design}
  goal: >
    Leverage advanced {technique|meta-prompting} techniques to create highly effective prompts
    for {model_type|generative} models that {objective|maximize coherence and relevance}
  backstory: >
    With {experience_years|8}+ years crafting prompts across {industry_count|12}+ industries,
    you've become renowned for your {specialty|structured} approach to prompt engineering.
    Your methodology consistently {achievement|improves output quality} by {percentage|40}% compared to standard approaches.
  temperature: {temperature|0.7}
  tools:
    - prompt_testing_tool
    - prompt_template_library

prompt_researcher:
  inherits: prompt_master_base
  role: >
    {specialization|Analytical} Prompt {seniority|Researcher} with expertise in {domain_expertise|academic literature}
  goal: >
    Conduct systematic analysis of {research_scope|prompt patterns} across {model_category|various LLM architectures}
    to identify {objective|optimal prompting strategies}
  backstory: >
    Your research in prompt engineering has been cited in {citation_count|15}+ academic papers.
    You've developed methodologies that {achievement|extract 30% more pertinent information}
    from language models through {specialty|contextual framing techniques}.
  temperature: {temperature|0.5}
  tools:
    - semantic_search_tool
    - literature_analyzer
    - pattern_extraction_tool

prompt_documentor:
  inherits: prompt_master_base
  role: >
    {specialization|Technical} Prompt {seniority|Documentation Specialist} with expertise in {domain_expertise|knowledge management}
  goal: >
    Create comprehensive {documentation_type|technical reference guides} for prompt libraries
    with {documentation_focus|implementation examples} and {measurement_metrics|effectiveness metrics}
  backstory: >
    You've documented prompt systems for {company_count|50}+ enterprise organizations,
    creating {documentation_style|accessible yet comprehensive} guides that reduce prompt engineering
    onboarding time by {time_reduction|65}%. Your documentation system is {adoption_status|widely adopted}
    in the {industry_focus|AI development} community.
  temperature: {temperature|0.3}
  tools:
    - file_output_tool
    - markdown_formatter
    - taxonomy_builder

prompt_tester:
  inherits: prompt_master_base
  role: >
    {specialization|Empirical} Prompt {seniority|Quality Assurance Specialist} with expertise in {domain_expertise|performance evaluation}
  goal: >
    Develop and implement {testing_methodology|rigorous testing frameworks} for prompt evaluation
    across {evaluation_dimensions|robustness, coherence, and relevance} dimensions
  backstory: >
    You've pioneered {testing_approach|systematic prompt testing methodologies} that have been
    implemented by {organization_type|leading AI labs}. Your evaluation metrics have become
    {standard_status|industry standards} for measuring prompt effectiveness across {model_count|dozens} of models.
  temperature: {temperature|0.4}
  tools:
    - prompt_benchmark_tool
    - statistical_analyzer
    - regression_testing_tool

structured_thinking_expert:
  inherits: prompt_master_base
  role: >
    {specialization|Analytical} Thinking Architect with expertise in {domain_expertise|systematic problem decomposition}
  goal: >
    Generate well-organized thought processes using XML-based structure for {objective|complex problem analysis}
  backstory: >
    Pioneer in developing XML-based thinking patterns that enhance analytical clarity by {percentage|45}%
  temperature: 0.7
  tools:
    - template_validation
    - structure_check
    - pattern_recognition
    - logic_verification

analysis_expert:
  inherits: prompt_master_base
  role: >
    {specialization|Strategic} Analysis Expert with focus on {domain_expertise|branching logic}
  goal: >
    Apply systematic thinking patterns to break down complex problems using structured XML frameworks
  backstory: >
    Developed branched analysis methodologies that improve decision quality by {percentage|50}%
  temperature: 0.6
  tools:
    - branch_analysis
    - decision_mapping
    - impact_assessment
    - pattern_matching

# Add new agent type
xml_thinking_specialist:
  inherits: prompt_master_base
  role: >
    Structured Thinking Specialist with expertise in XML-based cognitive patterns
  goal: >
    Apply systematic XML-structured analysis to break down complex problems
  tools:
    - structured_thinking_tool
    - branch_analysis_tool
    - pattern_recognition_tool

# Agent Configurations with Memory and Advanced Settings
base_config:
  memory:
    enabled: true
    type: "conversation_buffer"
    max_tokens: 1048576  # Flash model context limit
    memory_key: "chat_history"
    return_messages: true
    output_key: "output"
    input_key: "input"
  llm_settings:
    temperature: 0.7
    top_p: 0.95
    presence_penalty: 0.0
    frequency_penalty: 0.0
    max_tokens: 8192  # Output token limit
  validation:
    validate_outputs: true
    validate_inputs: true
    structured_output: true
  model_settings:
    default_model: "${GEMINI_MODEL:-models/gemini-2.0-flash}"
    available_models:
      gemini_flash:
        name: "models/gemini-2.0-flash"
        context_window: 1048576
        max_tokens: 8192
      gemini_flash_lite:
        name: "models/gemini-2.0-flash-lite"
        context_window: 1048576
        max_tokens: 8192
      gemini_pro:
        name: "models/gemini-2.0-pro-exp-02-05"
        context_window: 32768
        max_tokens: 8192
      lmstudio:
        name: "${LMSTUDIO_MODEL}"
        context_window: 4096
        max_tokens: 2048
      lmstudio_emb:
        name: "text-embedding-nomic-embed-text-v1.5"
        context_window: 4096
        max_tokens: 2048

# Research Expert Agent
researcher:
  role: "Research Expert"
  goal: "Conduct comprehensive research and gather accurate information"
  backstory: "Expert researcher with advanced analytical capabilities and information synthesis skills"
  allow_delegation: true
  model:
    type: "gemini_flash"
    settings:
      temperature: 0.7
      top_p: 0.95
  memory:
    inherit: true  # Inherit base memory config
    context_window: 1048576  # Full Flash model context
    memory_type: "vectorstore"  # Enhanced memory type
  tools:
    - web_search
    - file_analyzer
    - knowledge_base
  verbose: true
  max_iter: 5
  max_rpm: 100  # Rate limit for API calls
  async_execution: true

# Analysis Expert Agent
analyzer:
  role: "Analysis Expert"
  goal: "Process and analyze information with advanced reasoning"
  backstory: "Expert analyst specializing in pattern recognition and data interpretation"
  allow_delegation: true
  model:
    type: "gemini_flash_lite"
    settings:
      temperature: 0.6
      top_p: 0.9
  memory:
    inherit: true
    selective_memory: true  # Only store important information
    context_window: 1048576
    memory_priority: "high"
    contextual_recall: true
  tools:
    - structured_analysis
    - validation_tool
    - insight_generator
  verbose: true
  max_iter: 3
  parallel_processing: true

# Code Expert Agent
code_expert:
  role: "Code Analysis Expert"
  goal: "Analyze and generate code with best practices"
  backstory: "Expert software engineer with deep knowledge of code analysis and generation"
  allow_delegation: true
  model:
    type: "lmstudio"
    settings:
      temperature: 0.8
      top_p: 0.95
  memory:
    inherit: true
    code_context: true  # Special memory for code
    context_window: 4096
    memory_type: "code_aware"
  tools:
    - code_execution
    - code_analysis
    - code_generation
  verbose: true
  execution_mode: "safe"
  sandbox_environment: true

# Integration Expert Agent
integrator:
  role: "Integration Expert"
  goal: "Coordinate between different agents and systems"
  backstory: "Expert system integrator with experience in complex system coordination"
  allow_delegation: true
  model:
    primary: "gemini_flash"
    embedding: "lmstudio_emb"
    settings:
      temperature: 0.7
      top_p: 0.95
  memory:
    inherit: true
    shared_memory: true  # Share memory across agents
    global_context: true
    context_window: 1048576
    embedding_model: "lmstudio_emb"
  tools:
    - agent_coordinator
    - workflow_manager
    - resource_allocator
  verbose: true
  coordination_mode: "active"

# Advanced Agent Settings
agent_settings:
  execution:
    async_enabled: true
    parallel_tasks: 3
    timeout: 300  # seconds
    retry_attempts: 3
  monitoring:
    log_level: "INFO"
    track_performance: true
    track_memory_usage: true
    track_tool_usage: true
  optimization:
    batch_processing: true
    resource_aware: true
    adaptive_execution: true
  validation:
    input_validation: true
    output_validation: true
    context_validation: true
  security:
    sandbox_mode: true
    rate_limiting: true
    credential_check: true

# Memory Configuration Details
memory_settings:
  conversation_buffer:
    max_history: 50
    priority_based: true
    cleanup_frequency: "auto"
  vectorstore:
    engine: "faiss"
    dimension: 1536
    similarity_threshold: 0.8
  selective:
    importance_threshold: 0.7
    max_tokens_per_entry: 1000
    pruning_strategy: "importance"
  code_aware:
    language_support: ["python", "javascript", "go"]
    context_window: 1048576
    token_limit: 8192
  model_specific:
    gemini_flash:
      max_history: 100
      cleanup_threshold: 900000  # 90% of context window
    gemini_flash_lite:
      max_history: 80
      cleanup_threshold: 900000
    lmstudio:
      max_history: 40
      cleanup_threshold: 3500  # ~85% of context window
    lmstudio_emb:
      max_history: 40
      cleanup_threshold: 3500

# Tool Access Configuration
tool_access:
  web_search:
    allowed_agents: ["researcher"]
    rate_limit: 10
  code_execution:
    allowed_agents: ["code_expert"]
    sandbox_required: true
  agent_coordinator:
    allowed_agents: ["integrator"]
    coordination_level: "full"

# Agent Communication
communication:
  protocol: "async"
  message_format: "structured"
  broadcast_enabled: true
  coordination_method: "consensus"
  delegation_rules:
    max_depth: 3
    approval_required: false
    priority_override: true
````

## File: src/ollama/config/tasks.yaml

````yaml
# Core Research Tasks
research_task:
  description: >
    Research {topic} focusing on key information and insights.
    Consider current context from {current_year}.
  expected_output: >
    Structured findings with clear sections:
    - Key discoveries
    - Supporting evidence
    - Relevance assessment
  agent: researcher
  context_requirements:
    - topic_relevance
    - time_sensitivity
    - source_quality
  model:
    primary: "gemini_flash"
    fallback: "gemini_flash_lite"
  variables:
    context_window: 1048576
    token_limit: 8192
    thinking_mode: "experimental"

reporting_task:
  description: >
    Create a detailed report based on research findings.
    Format: Structured markdown with clear sections.
  expected_output: >
    Comprehensive report with:
    - Executive summary
    - Detailed analysis
    - Key recommendations
  agent: reporting_analyst
  validation_rules:
    - completeness
    - accuracy
    - clarity

# Analysis Tasks with proper task isolation
analysis_task:
  template: structured_analysis
  description: >
    Analyze {topic} using systematic approach with defined metrics
  variables:
    depth: "comprehensive"
    format: "structured"
    validation: true
  agent: analytical_expert
  expected_output: >
    Analysis results with:
    - Quantitative metrics
    - Qualitative insights
    - Action recommendations
  model:
    primary: "gemini_flash_lite"
    fallback: "lmstudio"

processing_task:
  template: data_processing
  description: >
    Process and structure information using defined patterns
  variables:
    format: "json"
    validation: true
  agent: processing_expert
  expected_output: >
    Structured data with:
    - Processed results
    - Validation metrics
    - Quality indicators
  model:
    primary: "gemini_flash_lite"
    fallback: "lmstudio"

# Task Chains with Clear Dependencies
task_chain:
  research:
    order: 1
    next: analysis
    validation: true
  analysis:
    order: 2
    next: reporting
    requires: ["research"]
  reporting:
    order: 3
    requires: ["analysis"]
    final: true

# Optional Vision Analysis Task (only used when needed)
vision_analysis_task:
  enabled: false  # Default disabled, enable when needed
  template: vision
  description: >
    Analyze visual content when explicitly requested
  variables:
    vision_type: "auto"
    depth: "standard"
  agent: vision_expert
  expected_output: >
    Visual analysis with:
    - Content description
    - Pattern recognition
    - Context interpretation

# Prompt Mastery Tasks
research_prompt_techniques:
  description: >
    Research current best practices and techniques in prompt engineering
  expected_output: >
    A comprehensive summary of modern prompt engineering techniques,
    including examples and use cases across different domains
  agent: prompt_researcher

generate_prompt_templates:
  description: >
    Design a set of prompt templates for common use cases based on research findings
  expected_output: >
    A collection of prompt templates with explanations of their structure,
    intended use cases, and examples of expected outputs
  agent: prompt_engineer
  depends_on:
    - research_prompt_techniques

document_prompts:
  description: >
    Create comprehensive documentation for the prompt templates
  expected_output: >
    Documentation files containing detailed descriptions, usage guidelines,
    examples, and best practices for each prompt template
  agent: prompt_documentor
  depends_on:
    - generate_prompt_templates

# Task templates with variable placeholders
task_templates:
  research_template:
    description_template: >
      Research {research_topic} with focus on {research_focus}, examining at least
      {source_count} different {source_type} from the past {timeframe}.
    output_template: >
      A comprehensive {output_format} containing {detail_level} analysis of
      {analysis_topic} with supporting evidence from {evidence_sources}.

  creation_template:
    description_template: >
      Create {creation_type} for {target_audience} with {creation_purpose},
      ensuring {quality_criteria} and adherence to {standards}.
    output_template: >
      A collection of {output_count} {output_type} with {organization_method}
      and {metadata_inclusion} for each {item_type}.

  documentation_template:
    description_template: >
      Document {documentation_subject} using {documentation_format} with
      {documentation_structure}, ensuring {documentation_standards}.
    output_template: >
      {output_type} documentation in {file_format} format containing
      {section_types} with {reference_inclusion} and {example_count} examples.

# Concrete tasks with inheritance from templates
analyze_prompt_landscape:
  inherits: task_templates.research_template
  description: >
    Research {research_topic|current prompt engineering methodologies} with focus on {research_focus|emerging techniques},     examining at least {source_count|15} different {source_type|academic papers and industry reports}     from the past {timeframe|12 months}.
  expected_output: >
    A comprehensive {output_format|research report} containing {detail_level|in-depth} analysis of
    {analysis_topic|prompt engineering patterns and their effectiveness} with supporting evidence     from {evidence_sources|peer-reviewed research and industry benchmarks}.
  agent: prompt_researcher
  context: >
    Focus particularly on techniques applicable to {model_type|large language models}     with {model_architecture|transformer-based architectures}.

map_prompt_patterns:
  inherits: task_templates.research_template
  description: >
    Identify and categorize {research_focus|common patterns in effective prompts}     across {domain_count|5+} domains, analyzing how {analysis_subject|structural elements}     affect {performance_metric|response quality}.
  expected_output: >
    A {output_format|taxonomic breakdown} of {classification_subject|prompt patterns}     with {analysis_type|comparative analysis} of their effectiveness in {context_types|different contexts}.
  agent: prompt_researcher
  depends_on:
    - analyze_prompt_landscape
  context: >
    Consider how patterns vary across {model_size_range|different model sizes} and     {specialization_types|specialized vs. general models}.

design_prompt_templates:
  inherits: task_templates.creation_template
  description: >
    Create {creation_type|modular prompt templates} for {target_audience|technical and non-technical users}     with {creation_purpose|variable placeholders for customization}, ensuring {quality_criteria|consistency in output format}     and adherence to {standards|established best practices from research}.
  expected_output: >
    A collection of {output_count|10+} {output_type|prompt templates} with {organization_method|categorical organization by use case}
    and {metadata_inclusion|performance characteristics} for each {item_type|template}.
  agent: prompt_engineer
  depends_on:
    - map_prompt_patterns
  context: >
    Templates should support {variable_types|text, numerical, and categorical} variables and include
    {guidance_type|usage notes} for optimal implementation.

build_prompt_library:
  inherits: task_templates.creation_template
  description: >
    Develop a {creation_type|comprehensive prompt library} organized by {organization_method|domain and complexity},
    with {feature_inclusion|built-in evaluation metrics} for each prompt template.
  expected_output: >
    A structured {output_type|prompt collection} with {metadata_count|5+} metadata fields per template,
    including {metadata_fields|effectiveness score, ideal use cases, limitations, and example outputs}.
  agent: prompt_engineer
  depends_on:
    - design_prompt_templates
  context: >
    Include prompts specifically optimized for {model_list|gemma, llama, mistral} models     running in {deployment_context|Ollama local environments}.

test_prompt_effectiveness:
  inherits: task_templates.creation_template
  description: >
    Evaluate {evaluation_subject|each prompt template} using {methodology|systematic testing approach}
    across {dimension_count|multiple} dimensions including {dimensions|coherence, relevance, and factuality}.
  expected_output: >
    A {output_format|detailed test report} with {metric_type|quantitative and qualitative} assessments
    for each template, including {improvement_suggestions|specific recommendations for refinement}.
  agent: prompt_tester
  depends_on:
    - build_prompt_library
  context: >
    Apply more rigorous testing to {priority_templates|high-impact templates} like those for
    {use_case_examples|code generation, reasoning tasks, and creative content}.

document_prompt_library:
  inherits: task_templates.documentation_template
  description: >
    Document {documentation_subject|the complete prompt library} using {documentation_format|markdown and YAML frontmatter}
    with {documentation_structure|hierarchical organization}, ensuring {documentation_standards|comprehensive metadata and examples}.
  expected_output: >
    {output_type|Comprehensive} documentation in {file_format|markdown} format containing
    {section_types|sections} with {reference_inclusion|references} and {example_count|multiple} examples.
  agent: prompt_documentor
  depends_on:
    - test_prompt_effectiveness

reasoning_task:
  template: reasoning
  description: >
    Analyze problem using analytical reasoning framework
  variables:
    problem_domain: "{domain}"
    analysis_depth: "detailed"
    structured_output: "json"
    task_context: "{context}"
    chain_results: "{previous_results}"
  agent:
    role: analytical_expert
    goal: "Provide comprehensive problem analysis"
    tools: ["research", "analyze", "summarize"]
    allowed_chains: ["research_task", "reporting_task"]

# Add new structured thinking tasks

structured_analysis_task:
  template: tags
  description: >
    Apply XML-based structured thinking to analyze {topic} using systematic branching patterns
  variables:
    context: "{analysis_context}"
    objective: "{analysis_goal}"
    depth: "comprehensive"
    reasoning_style: "analytical"
  agent: structured_thinking_expert
  expected_output: >
    A structured analysis following the XML template pattern with clear branches for:
    - Plan section with execution details
    - Thoughts section with strategic elements
    - Analysis section with component breakdown
    - Execution section with implementation steps

branching_analysis_task:
  template: tags
  description: >
    Develop comprehensive branch analysis for {topic} with multiple decision paths
  variables:
    context: "{decision_context}"
    objective: "Map decision tree with alternatives"
    format: "structured"
    depth: "detailed"
  agent: analysis_expert
  expected_output: >
    A detailed branch analysis using XML tags and CDATA sections covering:
    - Multiple decision paths
    - Alternative scenarios
    - Impact assessment
    - Risk evaluation

task_chain_template:
  description_template: >
    Apply {analysis_type} thinking pattern to {subject} using XML-structured approach
    with {branch_depth} levels of analysis and {validation_criteria} validation
  output_template: >
    XML-structured analysis with CDATA sections containing:
    - {component_count} main components
    - {branch_count} decision branches
    - {metric_count} evaluation metrics
    - {validation_count} quality checks

advanced_reasoning_task:
  inherits: task_chain_template
  template: tags
  description: >
    Conduct systematic analysis of {topic} using XML-structured thinking patterns
    with focus on {focus_areas} and consideration of {constraint_set}
  variables:
    context: "{problem_context}"
    depth: "comprehensive"
    format: "structured"
    reasoning_style: "analytical"
  agent:
    role: structured_thinking_expert
    goal: "Generate comprehensive structured analysis"
    tools: ["template_validation", "pattern_recognition", "logic_verification"]
    allowed_chains: ["research_task", "branching_analysis_task"]

structured_thinking_pipeline:
  template: tags
  description: >
    Apply structured thinking to {topic} using:
    - XML-based thought organization
    - Branching analysis patterns
    - CDATA sections for content
  steps:
    - initial_analysis
    - branch_development
    - pattern_recognition
    - validation_check

code_execution_task:
  template: code
  description: >
    Execute and analyze code with proper sandboxing
  model:
    primary: "lmstudio"
    fallback: "gemini_flash"
  variables:
    sandbox: true
    max_execution_time: 30
    memory_limit: 1000

embedding_task:
  template: embedding
  description: >
    Generate embeddings for knowledge base entries
  model:
    primary: "lmstudio_emb"
    fallback: null
  variables:
    batch_size: 32
    normalize: true
````

## File: src/ollama/crew.py

````python
# Load configuration
config_dir = Path(__file__).parent / "config"
⋮----
agents_config = yaml.safe_load(f)
⋮----
tasks_config = yaml.safe_load(f)
⋮----
class BaseCrew
⋮----
def _initialize_tools(self) -> Dict
⋮----
"""Initialize all available tools"""
⋮----
def _format_agent_variables(self, config: Dict) -> Dict
⋮----
"""Format agent configuration variables"""
formatted = {}
⋮----
def get_agents(self) -> Dict[str, Agent]
⋮----
"""Create agents based on the configuration"""
⋮----
# Format configuration variables
formatted_config = self._format_agent_variables(config)
⋮----
# Initialize tools based on the agent
tools = self._get_agent_tools(formatted_config)
⋮----
def _get_agent_tools(self, config: Dict) -> List
⋮----
"""Get tools for an agent based on configuration"""
tools = []
⋮----
def _format_task_variables(self, config: Dict) -> Dict
⋮----
"""Format task configuration variables"""
⋮----
def get_tasks(self) -> List[Task]
⋮----
"""Create tasks based on the configuration"""
⋮----
# Format task configuration
formatted_config = self._format_task_variables(config)
⋮----
# Get the agent for this task
agent = self.agents[formatted_config["agent"]]
⋮----
# Set up task dependencies
depends_on = []
⋮----
# Create task with additional context
⋮----
def add_context(self, context: Dict) -> None
⋮----
"""Add additional context for variable formatting"""
⋮----
def run(self, process_type: Process = Process.sequential) -> Dict
⋮----
"""Run the crew with specified process type"""
crew = Crew(
⋮----
result = crew.kickoff()
⋮----
# Save results using FileOutputTool
output_tool = self.tools["file_output_tool"]
⋮----
class OllamaCrew(BaseCrew)
⋮----
def __init__(self, *args, **kwargs)
⋮----
# Ollama-specific initialization here
⋮----
class GeminiCrew(BaseCrew)
⋮----
tools = super()._initialize_tools()
# Add Gemini-specific tools here if needed
⋮----
class LMStudioCrew(BaseCrew)
⋮----
# Add LMStudio-specific tools here if needed
````

## File: src/ollama/tools/custom_tool.py

````python
logger = logging.getLogger(__name__)
⋮----
class XMLValidationError(Exception)
⋮----
"""Custom exception for XML validation errors."""
⋮----
class StructureError(Exception)
⋮----
"""Custom exception for structure-related errors."""
⋮----
@dataclass
class ValidationResult
⋮----
"""Structured validation result."""
valid: bool
score: float
issues: List[str]
details: Dict[str, Any]
⋮----
class ValidationLevel(Enum)
⋮----
"""Validation severity levels."""
STRICT = "strict"
NORMAL = "normal"
RELAXED = "relaxed"
⋮----
class XMLStructureInput(BaseModel)
⋮----
"""Input schema for XML structure validation."""
content: str = Field(..., description="XML content to validate")
required_tags: List[str] = Field(
check_cdata: bool = Field(
⋮----
class BranchAnalysisInput(BaseModel)
⋮----
"""Input schema for branch analysis."""
scenario: str = Field(..., description="Initial scenario to analyze")
depth: int = Field(default=3, description="Branch depth")
width: int = Field(default=3, description="Maximum alternatives per node")
⋮----
class SmartRecoveryMixin
⋮----
"""Add to tools for intelligent error recovery."""
⋮----
def recover_from_error(self, error: Exception, context: Dict) -> Dict
⋮----
"""Attempt to recover from various error types."""
⋮----
def _fix_xml_structure(self, context: Dict) -> Dict
⋮----
"""Fix common XML structure issues."""
# Implementation here
⋮----
def _reorganize_structure(self, context: Dict) -> Dict
⋮----
"""Reorganize malformed structure."""
⋮----
def _general_recovery(self, context: Dict) -> Dict
⋮----
"""General error recovery strategy."""
⋮----
class MyCustomToolInput(BaseModel)
⋮----
"""Input schema for MyCustomTool."""
argument: str = Field(..., description="Description of the argument.")
⋮----
class PatternRecognitionInput(BaseModel)
⋮----
"""Input schema for pattern recognition in thinking structures."""
content: str = Field(..., description="Content to analyze")
pattern_types: List[str] = Field(
⋮----
class StructuredThinkingTool(BaseTool, SmartRecoveryMixin)
⋮----
"""Tool for structured thinking pattern validation and analysis."""
name: str = "structured_thinking_tool"
description: str = "Validate and analyze XML-structured thinking patterns"
args_schema: Type[BaseModel] = XMLStructureInput
⋮----
def __init__(self)
⋮----
def _validate_cdata(self, elem: ET.Element) -> List[str]
⋮----
"""Validate CDATA sections in an element."""
issues = []
⋮----
"""Calculate weighted structure score."""
⋮----
weighted_deductions = (missing * weights["missing"]) + (issues * weights["issues"])
score = max(0.0, min(1.0, 1.0 - (weighted_deductions / total)))
⋮----
"""Run validation with enhanced error handling."""
⋮----
result = ValidationResult(
⋮----
root = ET.fromstring(content)
⋮----
"""Validate content structure and requirements."""
⋮----
elem = root.find(tag)
⋮----
"""Process CDATA validation issues."""
cdata_issues = self._validate_cdata(elem)
⋮----
class MyCustomTool(BaseTool)
⋮----
name: str = "Name of my tool"
description: str = (
args_schema: Type[BaseModel] = MyCustomToolInput
⋮----
def _run(self, argument: str) -> str
⋮----
# Implementation goes here
⋮----
class BranchAnalysisTool(BaseTool)
⋮----
name: str = "branch_analysis_tool"
description: str = "Analyze decision trees and branching patterns"
args_schema: Type[BaseModel] = BranchAnalysisInput
⋮----
def _run(self, scenario: str, depth: int, width: int) -> Dict
⋮----
analysis = {
⋮----
def generate_branches(node: str, current_depth: int) -> List[Dict]
⋮----
branches = []
⋮----
branch = {
⋮----
class FileOutputTool(Tool)
⋮----
name: str = "file_output_tool"
description: str = "Write structured content to files with various formats"
⋮----
def __init__(self, output_dir="./outputs")
⋮----
"""Write content to file with metadata and formatting."""
file_path = os.path.join(self.output_dir, file_name)
⋮----
# Add metadata if provided
⋮----
content = f"---\n{json.dumps(metadata, indent=2)}\n---\n\n{content}"
⋮----
content = f"<!-- metadata: {json.dumps(metadata)} -->\n{content}"
⋮----
class PromptTestingTool(Tool)
⋮----
name: str = "prompt_testing_tool"
description: str = "Comprehensive prompt testing and validation"
⋮----
results = {
⋮----
# Implement testing logic here
⋮----
class PromptTemplateLibrary
⋮----
name: str = "prompt_template_library"
description: str = "Manage prompt templates"
⋮----
def _execute(self, action: str, template_id=None, category=None, template=None)
⋮----
# Implement template management
⋮----
class MarkdownFormatter
⋮----
name: str = "markdown_formatter"
description: str = "Format content as markdown"
⋮----
def _execute(self, content: dict, template_type="documentation")
⋮----
# Implement markdown formatting
⋮----
class DocumentationGenerator
⋮----
"""Generate comprehensive documentation"""
def generate_docs(self, analysis_results: Dict) -> str
⋮----
template = """
⋮----
class AdvancedValidator
⋮----
"""Enhanced validation with pattern matching"""
def validate_structure(self, content: str) -> ValidationResult
⋮----
patterns = {
⋮----
class PerformanceMonitor
⋮----
"""Monitor and optimize system performance"""
⋮----
def track_execution(self, func)
⋮----
@wraps(func)
        def wrapper(*args, **kwargs)
⋮----
start_time = time.time()
memory_start = util.Process().memory_info().rss
⋮----
result = func(*args, **kwargs)
⋮----
execution_time = time.time() - start_time
memory_used = (util.Process().memory_info().rss - memory_start) / (1024 * 1024)
⋮----
def get_performance_summary(self) -> Dict
⋮----
"""Get summary of performance metrics"""
⋮----
# Add to template files
current_date = datetime.now().strftime("%Y-%m-%d")
template = f"""
````

## File: src/ollama/tools/langchain.py

````python
logger = logging.getLogger(__name__)
⋮----
class XMLThinkingOutputParser(BaseOutputParser)
⋮----
"""Parser for XML-structured thinking patterns"""
⋮----
def parse(self, text: str) -> Dict
⋮----
# Clean and normalize XML
text = text.replace("```xml", "").replace("```", "").strip()
root = ET.fromstring(text)
⋮----
def _parse_section(self, element: ET.Element) -> Dict
⋮----
"""Parse XML section recursively"""
result = {}
⋮----
# Handle CDATA sections
⋮----
# Parse children
⋮----
class StructuredThinkingChain(LLMChain)
⋮----
"""Chain for structured thinking using XML patterns"""
⋮----
template_content = f.read()
⋮----
prompt = PromptTemplate(
⋮----
class BranchAnalysisChain(LLMChain)
⋮----
"""Chain for branching analysis patterns"""
⋮----
template = """
⋮----
class ResearchAnalysisChain(AnalyzeDocumentChain)
⋮----
"""Chain for research analysis with XML structure"""
⋮----
class CodeExecutionChain(LLMChain)
⋮----
"""Chain for code execution and analysis"""
⋮----
def execute_with_vision(self, code: str, image_path: Optional[str] = None) -> Dict[str, Any]
⋮----
"""Execute code with optional vision analysis"""
⋮----
start_time = time.time()
⋮----
# Log parameters
⋮----
vision_context = {}
⋮----
vision_context = self.vision_analyzer.analyze_code_image(image_path)
⋮----
result = self.code_executor.execute_code(
⋮----
# Log execution metrics
execution_time = time.time() - start_time
⋮----
class ModelManager
⋮----
"""Manages model initialization and configuration"""
def __init__(self, model_config: Dict)
⋮----
def get_model(self, model_type: str) -> Any
⋮----
model_config = self.config["available_models"].get(model_type)
⋮----
def _init_gemini_model(self, config: Dict) -> Any
⋮----
def _init_lmstudio_model(self, config: Dict) -> Any
⋮----
class AgentFactory
⋮----
"""Creates agents with appropriate model configurations"""
def __init__(self, base_config: Dict)
⋮----
def create_agent(self, agent_config: Dict) -> Agent
⋮----
model_type = agent_config["model"]["type"]
model = self.model_manager.get_model(model_type)
⋮----
# LMStudio model configuration
llm = LLM(
⋮----
# Gemini model configuration
llm = LLM(model=model)
⋮----
# Update the create_structured_thinking_agent function
⋮----
"""Create an agent specialized in structured thinking with specific model configuration"""
# Initialize factory with base config
factory = AgentFactory(agent_config.get("base_config", {}))
⋮----
# Create agent with specified model
agent = factory.create_agent(agent_config)
⋮----
# Add tools and memory
⋮----
# Update create_analysis_pipeline function to use model-specific configurations
⋮----
"""Create a complete analysis pipeline with model-specific configurations"""
⋮----
factory = AgentFactory(base_config)
⋮----
# Create chains with appropriate models
structured_chain = StructuredThinkingChain(
⋮----
branch_chain = BranchAnalysisChain(
⋮----
research_chain = ResearchAnalysisChain(
⋮----
code_chain = CodeExecutionChain(
````

## File: src/ollama/tools/langgraph.py

````python
logger = logging.getLogger(__name__)
⋮----
class ThinkingState(BaseModel)
⋮----
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
⋮----
class AnalysisPhase(str, Enum)
⋮----
"""Phases of structured thinking process"""
PLAN = "plan"
THOUGHTS = "thoughts"
ANALYSIS = "analysis"
EXECUTION = "execution"
REVIEW = "review"
COMPLETE = "complete"
CODE_EXECUTION = "code_execution"
VISION_ANALYSIS = "vision_analysis"
⋮----
"""Create a graph for structured thinking process"""
⋮----
# Initialize tools
tool_executor = ToolExecutor(tools)
⋮----
# Load template
⋮----
template_content = f.read()
⋮----
# Create prompts for different phases
planning_prompt = ChatPromptTemplate.from_template("""
⋮----
analysis_prompt = ChatPromptTemplate.from_template("""
⋮----
# Add code execution prompt
code_execution_prompt = ChatPromptTemplate.from_template("""
⋮----
def should_continue(state: ThinkingState) -> Tuple[bool, str]
⋮----
"""Determine if thinking process should continue"""
⋮----
def track_state_transition(state: ThinkingState, phase: str) -> None
⋮----
"""Track state transition metrics in MLflow"""
⋮----
# Track phase-specific metrics
metrics = {
⋮----
"""Process current thinking phase with MLflow tracking"""
⋮----
# Update state with new messages
⋮----
# Process based on phase
⋮----
# Planning phase logic
⋮----
# Thought process logic
⋮----
"branches": []  # Add actual branches here
⋮----
# Analysis logic
⋮----
# Execution logic
⋮----
# Update metadata
⋮----
def process_code_execution(state: ThinkingState) -> ThinkingState
⋮----
"""Process code execution phase with MLflow tracking"""
⋮----
# Execute code and store results
⋮----
execution_result = tools["code_executor"].execute_code(
⋮----
def process_vision_analysis(state: ThinkingState) -> ThinkingState
⋮----
"""Process vision analysis phase with MLflow tracking"""
⋮----
# Analyze code images if present
⋮----
vision_result = tools["vision_analyzer"].analyze_code_image(
⋮----
# Create the graph
workflow = StateGraph(ThinkingState)
⋮----
# Add nodes for each phase including new code and vision nodes
⋮----
# Add edges including new nodes
⋮----
# Add conditional branching
⋮----
"""Create a complete analysis workflow"""
⋮----
# Ensure code and vision tools are available
required_tools = ["code_executor", "vision_analyzer"]
⋮----
graph = create_thinking_graph(
⋮----
# Initialize state with code and vision support
state = ThinkingState(
````

## File: src/ollama/utils/mlflow_dashboard.py

````python
logger = logging.getLogger(__name__)
⋮----
class MLflowDashboard
⋮----
"""MLflow dashboard for monitoring and tracking Ollama Crew performance."""
⋮----
"""Initialize MLflow dashboard with configuration."""
⋮----
def _load_config(self, config_path: Optional[str]) -> Dict
⋮----
"""Load dashboard configuration"""
⋮----
def _get_default_config(self) -> Dict
⋮----
"""Get default configuration"""
⋮----
def _initialize_mlflow(self) -> None
⋮----
"""Initialize MLflow experiment"""
⋮----
"""Start a new MLflow run with enhanced tracking"""
⋮----
run_name = run_name or f"run_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
⋮----
# Add system info to tags
system_tags = {
⋮----
# Initialize run metrics
⋮----
def log_metrics(self, metrics: Dict[str, float], step: Optional[int] = None) -> None
⋮----
"""Log metrics with validation and alerting"""
⋮----
# Update current metrics
⋮----
# Log to MLflow
⋮----
# Check thresholds and send alerts
⋮----
# Store for historical tracking
⋮----
def log_multimodal_metrics(self, metrics: Dict[str, Any]) -> None
⋮----
"""Log metrics specific to multimodal operations"""
multimodal_metrics = {
⋮----
def log_model_metrics(self, model_type: str, metrics: Dict[str, Any]) -> None
⋮----
"""Log metrics specific to model type"""
⋮----
model_config = self.config["metrics"]["models"].get(model_type, {})
⋮----
# Calculate performance ratio based on model-specific thresholds
performance_ratio = metrics.get("success_rate", 0) / model_config.get("performance_threshold", 1)
⋮----
model_metrics = {
⋮----
def _check_metric_thresholds(self, metrics: Dict[str, float]) -> None
⋮----
"""Check metrics against thresholds and trigger alerts"""
⋮----
threshold = self.config["metrics"]["validation"][f"{metric_name}_threshold"]
⋮----
threshold = self.config["metrics"]["performance"][f"{metric_name}_threshold"]
⋮----
def _trigger_alert(self, message: str, level: str = "WARNING") -> None
⋮----
"""Trigger alerts based on configuration"""
⋮----
def create_performance_visualizations(self) -> None
⋮----
"""Generate comprehensive performance visualizations"""
⋮----
# Create main dashboard
dashboard = self._create_dashboard()
⋮----
# Create individual metric plots
⋮----
# Save visualizations
⋮----
def _create_dashboard(self) -> go.Figure
⋮----
"""Create main performance dashboard"""
df = pd.DataFrame([
⋮----
fig = make_subplots(
⋮----
# Add traces for each metric
metrics_config = [
⋮----
def _create_multimodal_dashboard(self) -> go.Figure
⋮----
"""Create dashboard for multimodal metrics"""
df = pd.DataFrame([{
⋮----
# Add multimodal-specific traces
⋮----
def _create_model_performance_dashboard(self) -> go.Figure
⋮----
"""Create dashboard for model-specific performance metrics"""
⋮----
# Add model comparison
⋮----
def end_run(self, status: str = "FINISHED") -> None
⋮----
"""End the current MLflow run with final metrics and visualizations"""
⋮----
# Create final visualizations
⋮----
# Calculate and log final metrics
final_metrics = self._calculate_final_metrics()
⋮----
# End the run
⋮----
def _calculate_final_metrics(self) -> Dict[str, float]
⋮----
"""Calculate final aggregate metrics"""
metrics_df = pd.DataFrame([m["metrics"] for m in self.historical_metrics])
⋮----
def _save_visualizations(self) -> None
⋮----
"""Save all visualizations as artifacts"""
⋮----
path = self.artifacts_path / f"{fig_name}.html"
````

## File: .env.example

````
# Ollama Crew Configuration
#OLLAMA_HOST="http://localhost:11434"
#OLLAMA_MODEL="gemma-3:4b"

# Gemini Configuration
# MODEL="gemini/gemini-2.0-flash"
#GEMINI_API_KEY="<API_KEY>"
#LANGTRACE_API_KEY="<API_KEY>"

# Gemini Configuration
GEMINI_MODEL="models/gemini-2.0-flash"
GEMINI_API_KEY=""
GEMINI_MAX_TOKENS=8192
GEMINI_INPUT_TOKENS=1048576
GEMINI_CONTEXT_SIZE=1048576
GEMINI_MODEL_URL="https://api.gemini.com/v1/models/${GEMINI_MODEL}"
GEMINI_CHAT_API_URL="https://api.gemini.com/v1/chat/completions"
GEMINI_COMPLETIONS_URL="https://api.gemini.com/v1/completions"
GEMINI_EMBEDDINGS_URL="https://api.gemini.com/v1/embeddings"
GEMINI_TEMPERATURE=0.7
GEMINI_TOP_P=0.95
GEMINI_STRUCTURED_MODE=true
GEMINI_THINKING_MODE=experimental
GEMINI_FEATURES="structured_output,function_calling,code_execution,search,tool_use,thinking"
GEMINI_EXPERIMENTAL="image_generation,live_api,thinking"
GEMINI_COMING_SOON="audio_generation,caching"

# LM Studio Configuration
#LMSTUDIO_API_URL="http://10.26.112.79:1234"
#LMSTUDIO_API_VERSION="v1"
#LMSTUDIO_CHAT_API_URL="${LMSTUDIO_API_URL}/${LMSTUDIO_API_VERSION}/chat/completions"
#LMSTUDIO_MODEL_URL="${LMSTUDIO_API_URL}/${LMSTUDIO_API_VERSION}/models/${LMSTUDIO_MODEL}"
#LMSTUDIO_COMPLETIONS_URL="${LMSTUDIO_API_URL}/${LMSTUDIO_API_VERSION}/completions"
#LMSTUDIO_EMBEDDINGS_URL="${LMSTUDIO_API_URL}/${LMSTUDIO_API_VERSION}/embeddings"
#LMSTUDIO_MODEL_EMB="text-embedding-nomic-embed-text-v1.5"
#LMSTUDIO_MODEL="gemma-3-4b-it"

# LM Studio Configuration
LMSTUDIO_API_URL="http://localhost:1234"
LMSTUDIO_MODEL="gemma-3-4b-it"
LMSTUDIO_CONTEXT_SIZE=4096
LMSTUDIO_MAX_TOKENS=2048
LMSTUDIO_TEMPERATURE=0.7
LMSTUDIO_TOP_P=0.95
LMSTUDIO_RESPONSE_FORMAT="json"

# Langchain Configuration
#LANGCHAIN_API_KEY="API_KEY"

# MLflow Configuration
MLFLOW_TRACKING_URI=postgresql://postgres:7285@localhost:5432/mlflow_tracking

# Performance Monitoring
MONITOR_LOG_LEVEL=INFO
PERFORMANCE_THRESHOLD_CPU=80
PERFORMANCE_THRESHOLD_MEMORY=1000
EXECUTION_TIMEOUT=300

# API Keys and External Services
SERPER_API_KEY=your_serper_api_key_here
OPENAI_API_KEY=your_openai_api_key_here  # Optional: for comparison testing

# Logging Configuration
LOG_LEVEL=INFO
LOG_FILE=ollama.log
LOG_FORMAT=%(asctime)s - %(name)s - %(levelname)s - %(message)s

# System Configuration
MAX_PARALLEL_TASKS=3
DEFAULT_ANALYSIS_DEPTH=detailed
DEFAULT_BRANCH_DEPTH=3
VALIDATION_LEVEL=normal

# Model Selection and Coordination
MODEL_PRIORITY=["gemini", "lmstudio", "ollama"]
ENABLE_MODEL_FALLBACK=true
PARALLEL_MODEL_EXECUTION=false

# Output Configuration
OUTPUT_DIR=./outputs
TEMPLATE_DIR=./templates
CONFIG_DIR=./config

# Alert Configuration
ALERT_EMAIL=admin@example.com
ALERT_THRESHOLD_CRITICAL=5
ALERT_THRESHOLD_WARNING=3

# Cache Configuration
CACHE_ENABLED=true
CACHE_DIR=./cache
CACHE_RETENTION_DAYS=7

# Development Settings
DEBUG=false
DEVELOPMENT_MODE=false
PROFILE_CODE=false

# Security Settings
ENABLE_SSL=false
SSL_CERT_PATH=
SSL_KEY_PATH=

# Documentation
DOCS_AUTO_GENERATE=true
DOCS_OUTPUT_DIR=./docs
````

## File: .gitignore

````
.env
__pycache__/
.DS_Store
.env
*.pyc
````

## File: src/ollama/config/mlflow_config.yaml

````yaml
dashboard:
  experiment_name: "ollama_crew_monitoring"
  experiment_id: "628510843323994625"  # From your URL
  tracking_uri: "sqlite:///mlflow.db"
  artifacts_path: "./mlflow-artifacts"
  ui:
    port: 5000
    host: "127.0.0.1"
    default_view: "TABLE"
  auto_log: true
  log_system_metrics: true
  compare_runs:
    enabled: true
    default_metrics:
      - "execution_time"
      - "memory_usage"
      - "validation_score"
      - "success_rate"
    view_state_key: "3894e7dac091113a949e1a0b144bdfbf23f857b1cfb2b6251e919052fe25b155"  # From your URL
  model_tracking:
    gemini:
      experiment_name: "gemini_crew_monitoring"
      model_name: ${GEMINI_MODEL}
    lmstudio:
      experiment_name: "lmstudio_crew_monitoring"
      model_name: ${LMSTUDIO_MODEL}
    ollama:
      experiment_name: "ollama_crew_monitoring"
      model_name: ${OLLAMA_MODEL}

  compare_models:
    enabled: true
    metrics:
      - "execution_time"
      - "memory_usage"
      - "validation_score"
      - "success_rate"
    grouping: "model_name"

metrics:
  validation:
    - name: "validation_score"
      threshold: 0.8
      warning_threshold: 0.6
      critical_threshold: 0.4
      plot_type: "line"
      compare_runs: true
    - name: "error_count"
      threshold: 5
      warning_threshold: 10
      critical_threshold: 20
      plot_type: "bar"
      compare_runs: true
    - name: "structure_violations"
      threshold: 2
      warning_threshold: 5
      critical_threshold: 10
      plot_type: "bar"
      compare_runs: true

  performance:
    - name: "execution_time"
      unit: "seconds"
      warning_threshold: 10.0
      error_threshold: 30.0
      plot_type: "line"
      compare_runs: true
    - name: "memory_usage"
      unit: "MB"
      warning_threshold: 500
      error_threshold: 1000
      plot_type: "line"
      compare_runs: true
    - name: "success_rate"
      unit: "percentage"
      minimum_threshold: 0.95
      warning_threshold: 0.90
      critical_threshold: 0.85
      plot_type: "line"
      compare_runs: true
  model_specific:
    - name: "model_latency"
      unit: "milliseconds"
      warning_threshold: 1000
      critical_threshold: 5000
      plot_type: "line"
      compare_runs: true
    - name: "token_usage"
      unit: "count"
      warning_threshold: 8000
      critical_threshold: 15000
      plot_type: "bar"
      compare_runs: true

visualization:
  default_theme: "plotly_dark"
  refresh_interval: 60  # seconds
  retention_period: 30  # days
  default_view: "TABLE"  # Matches your URL
  charts:
    - type: "timeline"
      metrics: ["execution_time", "memory_usage", "success_rate"]
      layout:
        height: 400
        title: "Performance Timeline"
    - type: "comparison"
      metrics: ["validation_score", "error_count", "structure_violations"]
      layout:
        height: 400
        title: "Validation Metrics Comparison"
    - type: "distribution"
      metrics: ["execution_time", "memory_usage"]
      layout:
        height: 400
        title: "Resource Usage Distribution"

alerts:
  enabled: true
  channels:
    - type: "logging"
      level: "WARNING"
      format: "%(asctime)s - %(levelname)s - %(message)s"
    - type: "email"
      recipients: ["admin@example.com"]
      on_critical: true
      on_warning: false
  thresholds:
    critical_error_count: 5
    performance_degradation: 0.2
    memory_spike: 1.5  # ratio to average
  aggregation_window: "1h"
  cooldown_period: "15m"

runs:
  compare:
    enabled: true
    max_runs: 10
    default_metrics:
      - "execution_time"
      - "memory_usage"
      - "validation_score"
    sort_key: "start_time"
    sort_order: "desc"
  artifacts:
    save_plots: true
    save_metrics: true
    retention_days: 30

api:
  base_url: "http://127.0.0.1:5000"
  endpoints:
    experiments: "/api/2.0/mlflow/experiments"
    runs: "/api/2.0/mlflow/runs"
    metrics: "/api/2.0/mlflow/metrics"
  headers:
    Content-Type: "application/json"
````

## File: src/ollama/main.py

````python
#!/usr/bin/env python
⋮----
import psutil  # Add missing import for memory monitoring
⋮----
from concurrent.futures import ThreadPoolExecutor  # Add for parallel processing
⋮----
from src.ollama.tools.custom_tool import ValidationLevel  # Add for validation
⋮----
# Configure logging
⋮----
logger = logging.getLogger(__name__)
⋮----
# Ignore specific warnings
⋮----
# Load environment variables
⋮----
class PerformanceMonitor
⋮----
"""Monitor and optimize system performance"""
def __init__(self)
⋮----
def track_execution(self, func)
⋮----
@wraps(func)
        def wrapper(*args, **kwargs)
⋮----
start_time = time.time()
⋮----
result = func(*args, **kwargs)
⋮----
execution_time = time.time() - start_time
⋮----
class OllamaRunner
⋮----
# Initialize MLflow dashboard
⋮----
mlflow_config = yaml.safe_load(f)
⋮----
def setup_environment(self) -> None
⋮----
"""Setup necessary directories and configurations"""
⋮----
def get_default_inputs(self) -> Dict
⋮----
"""Get default input parameters"""
⋮----
def initialize_crew(self, custom_inputs: Optional[Dict] = None) -> None
⋮----
"""Initialize the crew with inputs"""
inputs = self.get_default_inputs()
⋮----
def validate_configuration(self) -> bool
⋮----
"""Validate runner configuration"""
⋮----
@PerformanceMonitor().track_execution
    def run(self, custom_inputs: Optional[Dict] = None) -> Dict
⋮----
"""Run the crew with structured thinking patterns and performance monitoring"""
⋮----
result = self.crew.run()
⋮----
# Log enhanced metrics
⋮----
def train(self, n_iterations: int, filename: str, custom_inputs: Optional[Dict] = None, max_workers: int = 3) -> Dict
⋮----
"""Train the crew with parallel iterations"""
⋮----
results = []
⋮----
future_to_iteration = {
⋮----
result = future.result()
⋮----
# Save and analyze results
⋮----
analysis = self._analyze_training_results(results)
⋮----
def _run_training_iteration(self, iteration: int) -> Dict
⋮----
"""Run a single training iteration"""
⋮----
def _analyze_training_results(self, results: List[Dict]) -> Dict
⋮----
"""Analyze training results"""
successful = [r for r in results if r.get("metrics", {}).get("success", False)]
⋮----
"""Test crew performance"""
⋮----
test_results = {
⋮----
def _save_execution_metadata(self, result: Dict) -> None
⋮----
"""Save execution metadata"""
metadata_path = self.output_dir / "execution_metadata.json"
metadata = {
⋮----
def _save_training_results(self, results: List[Dict], filename: str) -> None
⋮----
"""Save training results"""
training_path = self.output_dir / filename
⋮----
def _save_test_results(self, results: Dict) -> None
⋮----
"""Save test results"""
test_path = self.output_dir / f"test_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
⋮----
def _calculate_test_metrics(self, test_results: Dict) -> None
⋮----
"""Calculate test metrics"""
successful = sum(1 for r in test_results["results"] if r.get("valid", False))
⋮----
def setup_mlflow()
⋮----
tracking_uri = os.getenv("MLFLOW_TRACKING_URI", "postgresql://postgres:password@localhost:5432/mlflow_tracking")
⋮----
def run_crew(model_type: str, topic: str)
⋮----
# Set up MLflow tracking
⋮----
experiment_name = f"{model_type}_crew_monitoring"
⋮----
# Initialize appropriate crew
⋮----
crew = GeminiCrew(topic=topic)
⋮----
crew = LMStudioCrew(topic=topic)
⋮----
# Run analysis with MLflow tracking
⋮----
result = crew.run()
⋮----
# Log metrics
⋮----
def main()
⋮----
parser = argparse.ArgumentParser(description="Run AI analysis with different models")
⋮----
args = parser.parse_args()
⋮----
result = run_crew(args.model, args.topic)
````

## File: README.md

````markdown
<div align="center">

# Cognitive Crew AI Framework

> Next-Generation Enterprise AI System with Advanced Model Integration and MLflow Analytics

[Features](#-core-features) •
[Installation](#-quick-start) •
[Documentation](#-documentation) •
[Contributing](#-contributing)

[![Python](https://img.shields.io/badge/Python-3.10%20|%203.11%20|%203.12-blue?logo=python)](https://www.python.org/)
[![MLflow](https://img.shields.io/badge/MLflow-Latest-blue?logo=mlflow)](https://mlflow.org)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Latest-blue?logo=postgresql)](https://www.postgresql.org/)
[![Gemini](https://img.shields.io/badge/Gemini%202.0-Flash-purple?logo=google)](https://ai.google.dev/)
[![LangChain](https://img.shields.io/badge/LangChain-Latest-green?logo=chainlink)](https://langchain.com)
[![LangGraph](https://img.shields.io/badge/LangGraph-Latest-yellow)](https://python.langchain.com/docs/langgraph)
[![CrewAI](https://img.shields.io/badge/CrewAI-Latest-red)](https://www.crewai.com/)
[![Selenium](https://img.shields.io/badge/Selenium-Latest-green?logo=selenium)](https://www.selenium.dev/)
[![Docker](https://img.shields.io/badge/Docker-Latest-blue?logo=docker)](https://www.docker.com/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Latest-teal?logo=fastapi)](https://fastapi.tiangolo.com/)
[![UV](https://img.shields.io/badge/UV-Latest-purple?logo=python)](https://docs.astral.sh/uv/)
[![Pytest](https://img.shields.io/badge/Pytest-Latest-blue?logo=pytest)](https://docs.pytest.org/)
[![Black](https://img.shields.io/badge/Black-Latest-black?logo=python)](https://black.readthedocs.io/)
[![Ruff](https://img.shields.io/badge/Ruff-Latest-yellow?logo=python)](https://beta.ruff.rs/docs/)
[![Documentation](https://img.shields.io/badge/Docs-MkDocs-blue?logo=markdown)](https://www.mkdocs.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

</div>

## Table of Contents

- [Overview](#-overview)
- [Core Features](#-core-features)
- [System Architecture](#-system-architecture)
  - [Model Integration](#-model-integration)
  - [Tool Integration](#-tools-integration)
  - [Analytics Pipeline](#-performance-monitoring)
- [Installation](#-quick-start)
  - [Prerequisites](#-quick-start)
  - [Quick Start](#-quick-start)
  - [Docker Deployment](#-quick-start)
- [Usage](#-usage)
  - [Basic Usage](#-usage)
  - [Advanced Configuration](#-configuration)
  - [Model Selection](#-model-integration)
- [Configuration](#-configuration)
  - [Environment Variables](#-configuration)
  - [Model Settings](#-configuration)
  - [MLflow Setup](#-configuration)
- [Development](#-contributing)
  - [Code Quality](#-contributing)
  - [Testing](#-contributing)
  - [Documentation](#-documentation)
- [Monitoring](#-performance-monitoring)
  - [MLflow Dashboard](#-performance-monitoring)
  - [Performance Metrics](#-performance-monitoring)
  - [Alerting](#-performance-monitoring)
- [Contributing](#-contributing)
  - [Development Setup](#-contributing)
  - [Pull Request Process](#-contributing)
- [Support](#-support)
  - [Documentation](#-documentation)
  - [Community](#-support)
  - [Professional Support](#-support)
- [License](#-license)
- [Acknowledgments](#-acknowledgments)

## Overview

Cognitive Crew AI is an enterprise-grade framework for orchestrating multiple AI models with advanced analytics and monitoring capabilities. It supports Gemini Flash (1M context), LM Studio, and provides extensive tooling for development and deployment.

## Core Features

```mermaid
mindmap
  root((Cognitive Crew))
    Models
      Gemini Flash
        1M Context Window
        8K Output Tokens
      LM Studio
        Local Deployment
        Embedding Support
    Analytics
      MLflow Integration
      Real-time Monitoring
      Performance Tracking
    Tools
      Web Search
      Code Execution
      Knowledge Base
    Development
      UV Package Manager
      Docker Support
      FastAPI Integration
```

## Quick Start

```bash
# Install using UV
uv venv
uv pip install -r requirements.txt

# Configure Environment
cp .env.example .env

# Start MLflow Server
docker-compose up -d mlflow

# Run System
python -m src.ollama.main run
```

## Model Integration

| Model | Context | Output | Features |
|-------|----------|---------|-----------|
| Gemini Flash | 1M tokens | 8K tokens | Code, Search, Tools |
| LM Studio | 4K tokens | 2K tokens | Local, Embeddings |

## System Architecture

```mermaid
graph TD
    A[Client] --> B[OllamaCrew]
    B --> C[Agent Manager]
    B --> D[Task Manager]
    C --> E[Structured Thinking Expert]
    C --> F[Analysis Expert]
    C --> G[Research Expert]
    D --> H[Task Pipeline]
    E --> I[XML Processing]
    F --> J[Branch Analysis]
    G --> K[Data Collection]
    I --> L[Validation]
    J --> L
    K --> L
    L --> M[Output Generator]
    M --> N[Results]
```

## 📅 Project Timeline

```mermaid
gantt
    title Ollama Crew Development Roadmap
    dateFormat  YYYY-MM-DD
    section Core Development
    System Architecture       :done,    arch,   2024-03-01, 2024-03-15
    XML Framework            :done,    xml,    2024-03-15, 2024-03-30
    Agent System            :active,  agent,  2024-03-30, 2024-04-15
    section Features
    Basic Templates         :done,    temp,   2024-03-15, 2024-03-30
    Advanced Analysis      :active,  anal,   2024-03-30, 2024-04-30
    Integration Tools      :         tools,  2024-04-15, 2024-05-15
    section Testing & Deployment
    Unit Testing           :active,  test,   2024-04-01, 2024-05-01
    Documentation         :         docs,   2024-04-15, 2024-05-15
    Beta Release          :         beta,   2024-05-15, 2024-06-01
```

## 📊 Project Progress

Current Status: Beta Development (v2.0.0)

```mermaid
pie title Development Progress
    "Completed" : 45
    "In Progress" : 35
    "Planned" : 20
```

### Milestone Progress

- [x] Core Architecture (100%)
- [x] XML Framework (100%)
- [x] Basic Templates (100%)
- [ ] Advanced Analysis (75%)
- [ ] Integration Tools (45%)
- [ ] Testing Suite (60%)
- [ ] Documentation (40%)

## 🔮 Future Roadmap

```mermaid
graph LR
    A[Current: v2.0.0] --> B[v2.1.0: Enhanced Analysis]
    B --> C[v2.2.0: Advanced Integration]
    C --> D[v3.0.0: Enterprise Features]

    subgraph "Q2 2024"
    B
    end

    subgraph "Q3 2024"
    C
    end

    subgraph "Q4 2024"
    D
    end
```

### Upcoming Features

1. **Q2 2024 (v2.1.0)**
   - Advanced pattern recognition
   - Enhanced error recovery
   - Performance optimization

2. **Q3 2024 (v2.2.0)**
   - Custom model integration
   - Distributed processing
   - Real-time analytics

3. **Q4 2024 (v3.0.0)**
   - Enterprise security features
   - Advanced monitoring
   - Cloud deployment options

## 📊 Performance Monitoring

```mermaid
graph TD
    A[System Metrics] --> B[MLflow Dashboard]
    B --> C[Performance Data]
    B --> D[Validation Metrics]
    B --> E[Resource Usage]
    C --> F[Visualization]
    D --> F
    E --> F
    F --> G[Analysis Reports]
```

### Key Metrics

- Execution Performance
- Memory Utilization
- Success Rates
- Validation Scores
- Resource Efficiency

### Dashboard Features

- Real-time Monitoring
- Custom Metric Tracking
- Performance Alerts
- Resource Optimization
- Trend Analysis

## 🛠 Configuration

### Agent Configuration

```yaml
structured_thinking_expert:
  role: "Analytical Thinking Architect"
  goal: "Generate well-organized thought processes"
  tools: ["template_validation", "branch_analysis"]
```

### Task Configuration

```yaml
analysis_task:
  template: tags
  description: "Apply structured thinking to {topic}"
  agent: structured_thinking_expert
```

## 📚 Documentation

- [Configuration Guide](docs/configuration.md)
- [Template Reference](docs/templates.md)
- [API Documentation](docs/api.md)
- [Best Practices](docs/best-practices.md)

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 💬 Support

- 📚 [Documentation](https://docs.crewai.com)
- 💬 [Discord Community](https://discord.gg/X4JWnZnxPb)
- 🤝 [GitHub Issues](https://github.com/joaomdmoura/crewai/issues)
- 💡 [Documentation Chat](https://chatg.pt/DWjSBZn)

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [crewAI](https://crewai.com) for the core framework
- The open-source community for valuable tools and libraries
- Contributors who have helped shape this project

## 📋 Changelog

See [CHANGELOG.md](CHANGELOG.md) for version history and updates.

```mermaid
graph TB
    User((External User))

    subgraph "AI Analysis System"
        subgraph "Model Integration Layer"
            GeminiContainer["Gemini Integration<br>(Python/Google AI)"]
            OllamaContainer["Ollama Integration<br>(Python/Ollama)"]
            LMStudioContainer["LMStudio Integration<br>(Python/LMStudio)"]
        end

        subgraph "Core System"
            CrewManager["Crew Management<br>(CrewAI)"]
            TaskManager["Task Management<br>(YAML Config)"]

            subgraph "Tools Layer"
                CustomTools["Custom Tools<br>(Python)"]
                LangChainTools["LangChain Tools<br>(LangChain)"]
                LangGraphTools["LangGraph Tools<br>(LangGraph)"]
            end

            subgraph "Knowledge Management"
                KnowledgeBase["Knowledge Base<br>(YAML/JSON)"]
                PromptTemplates["Prompt Templates<br>(Markdown)"]
                Categories["Categories System<br>(YAML)"]
            end
        end

        subgraph "Monitoring & Analytics"
            MLFlow["MLFlow Tracking<br>(MLflow)"]
            Dashboard["MLFlow Dashboard<br>(Python/MLflow)"]
        end

        subgraph "Utility Components"
            ConfigManager["Configuration Manager<br>(YAML)"]
            KnowledgeManager["Knowledge Manager<br>(Python)"]
            PerformanceMonitor["Performance Monitor<br>(Python)"]
        end
    end

    subgraph "External Services"
        SerperDev["Serper.dev API<br>(REST)"]
    end

    User -->|Interacts| CrewManager

    CrewManager -->|Manages| GeminiContainer
    CrewManager -->|Manages| OllamaContainer
    CrewManager -->|Manages| LMStudioContainer

    CrewManager -->|Uses| TaskManager
    TaskManager -->|Configures| CustomTools
    TaskManager -->|Configures| LangChainTools
    TaskManager -->|Configures| LangGraphTools

    CustomTools -->|Accesses| KnowledgeBase
    LangChainTools -->|Uses| SerperDev

    KnowledgeManager -->|Manages| KnowledgeBase
    KnowledgeManager -->|Manages| PromptTemplates
    KnowledgeManager -->|Manages| Categories

    CrewManager -->|Logs to| MLFlow
    MLFlow -->|Displays in| Dashboard

    ConfigManager -->|Configures| CrewManager
    ConfigManager -->|Configures| TaskManager

    PerformanceMonitor -->|Tracks| MLFlow

    GeminiContainer -->|Uses| KnowledgeManager
    OllamaContainer -->|Uses| KnowledgeManager
    LMStudioContainer -->|Uses| KnowledgeManager
```
````
