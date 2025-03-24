# Ollama Crew - Advanced AI Agent Framework

> A sophisticated multi-agent AI system powered by [crewAI](https://crewai.com), featuring XML-structured thinking patterns and advanced branching analysis capabilities.

[![Python Version](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Documentation](https://img.shields.io/badge/docs-latest-brightgreen.svg)](docs/)
[![Discord](https://img.shields.io/discord/1234567890)](https://discord.gg/X4JWnZnxPb)

## 🌟 Features

- 🤖 **XML-Structured Thinking**: Systematic approach to problem-solving using XML patterns
- 🌳 **Advanced Branching Analysis**: Comprehensive decision tree exploration
- 🔍 **Smart Validation**: Robust error checking and recovery mechanisms
- 📊 **Performance Monitoring**: Built-in metrics and optimization tools
- 🔄 **Flexible Integration**: Easy integration with various LLM models
- 📝 **Template System**: Extensive template library for various use cases

## 📋 Requirements

- Python >=3.10 <3.13
- [UV](https://docs.astral.sh/uv/) for dependency management
- Ollama compatible system

## 🚀 Quick Start

1. **Install UV**:

```bash
pip install uv
```

2. **Install Dependencies**:

```bash
uv venv
uv pip install -r requirements.txt
```

3. **Configure Environment**:

```bash
cp .env.example .env
# Edit .env with your settings
```

4. **Run the System**:

```bash
python -m src.ollama.main run --topic "Your Analysis Topic"
```

## 🏗 System Architecture

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
