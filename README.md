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

    subgraph "Ollama System"
        subgraph "Core Services"
            OllamaRunner["Ollama Runner<br>(Python)"]
            MLflowDashboard["MLflow Dashboard<br>(MLflow)"]
            KnowledgeManager["Knowledge Manager<br>(Python)"]
        end

        subgraph "Model Services"
            subgraph "Gemini Container"
                GeminiClient["Gemini Client<br>(Google AI)"]
                GeminiCrew["Gemini Crew<br>(Python)"]
            end

            subgraph "LMStudio Container"
                LMStudioClient["LMStudio Client<br>(REST API)"]
                LMStudioCrew["LMStudio Crew<br>(Python)"]
            end

            ModelCoordinator["Model Coordinator<br>(Python)"]
        end

        subgraph "Agent System"
            subgraph "Agent Components"
                ResearchAgent["Research Agent<br>(CrewAI)"]
                AnalysisAgent["Analysis Agent<br>(CrewAI)"]
                CodeExpertAgent["Code Expert Agent<br>(CrewAI)"]
                IntegratorAgent["Integrator Agent<br>(CrewAI)"]
            end

            subgraph "Tool Components"
                ToolFactory["Tool Factory<br>(Python)"]
                SearchTools["Search Tools<br>(Python)"]
                CustomTools["Custom Tools<br>(Python)"]
            end
        end

        subgraph "Knowledge Base"
            KnowledgeBase[("Knowledge Base<br>(YAML/JSON)")]
            ConfigStore[("Configuration Store<br>(YAML)")]
            PromptTemplates["Prompt Templates<br>(Markdown/YAML)"]
        end

        subgraph "Monitoring"
            MLflowTracking["MLflow Tracking<br>(SQLite)"]
            Logging["Logging System<br>(Python)"]
        end
    end

    subgraph "External Services"
        SerperDev["SerperDev API<br>(REST API)"]
        GeminiAPI["Google Gemini API<br>(REST API)"]
    end

    %% Relationships
    User -->|"Interacts with"| OllamaRunner
    OllamaRunner -->|"Manages"| ModelCoordinator
    OllamaRunner -->|"Uses"| MLflowDashboard
    OllamaRunner -->|"Uses"| KnowledgeManager

    ModelCoordinator -->|"Coordinates"| GeminiClient
    ModelCoordinator -->|"Coordinates"| LMStudioClient

    GeminiClient -->|"Calls"| GeminiAPI
    GeminiClient -->|"Uses"| SearchTools
    LMStudioClient -->|"Uses"| SearchTools

    GeminiCrew -->|"Uses"| GeminiClient
    LMStudioCrew -->|"Uses"| LMStudioClient

    ResearchAgent -->|"Uses"| ToolFactory
    AnalysisAgent -->|"Uses"| ToolFactory
    CodeExpertAgent -->|"Uses"| ToolFactory
    IntegratorAgent -->|"Uses"| ToolFactory

    ToolFactory -->|"Creates"| SearchTools
    ToolFactory -->|"Creates"| CustomTools
    SearchTools -->|"Calls"| SerperDev

    KnowledgeManager -->|"Manages"| KnowledgeBase
    KnowledgeManager -->|"Reads"| ConfigStore
    KnowledgeManager -->|"Uses"| PromptTemplates

    MLflowDashboard -->|"Tracks"| MLflowTracking
    OllamaRunner -->|"Logs to"| Logging
```
