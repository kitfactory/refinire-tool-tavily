# Refinire Tool Tavily

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A comprehensive web search tool for RefinireAgent using the Tavily API. This package provides seamless integration between Refinire agents and Tavily's powerful web search capabilities.

[�,�H README](README_ja.md)

## Features

- = **Web Search Integration**: Complete Tavily API integration for RefinireAgent
- > **Refinire Tool Decorators**: Ready-to-use tools for agent integration
- =� **Multiple Search Types**: General, news, research, and context-optimized searches
- =� **Security & Validation**: Input validation and prompt injection protection
- =' **Environment Management**: OneEnv integration for easy configuration
-  **Comprehensive Testing**: 68% test coverage with robust error handling
- =� **Rich Documentation**: Examples and guides for all use cases

## Quick Start

### Installation

```bash
pip install refinire-tool-tavily
```

### Environment Setup

1. Generate environment template:
```bash
oneenv template
```

2. Copy and configure:
```bash
cp .env.example .env
# Edit .env and add your Tavily API key
```

3. Get your Tavily API key from [https://tavily.com/](https://tavily.com/)

### Basic Usage

```python
from refinire_tool_tavily import search_web

# Simple web search
result = search_web("Python programming best practices", max_results=5)

if result["success"]:
    for item in result["results"]:
        print(f"{item['title']}: {item['url']}")
```

### RefinireAgent Integration

```python
from refinire import Agent
from refinire_tool_tavily import refinire_web_search

# Create agent with web search capability
agent = Agent(
    name="WebSearchAgent",
    instructions="Use web search to find current information when needed.",
    tools=[refinire_web_search]
)

# Use the agent
response = agent.run("What are the latest developments in AI?")
```

## Available Tools

### Core Functions

- **`search_web()`**: Basic web search with full customization
- **`get_search_context()`**: Formatted search results for LLM consumption

### Refinire Tools

- **`refinire_web_search`**: General web search tool for agents
- **`refinire_web_search_context`**: Context-optimized search for LLMs
- **`refinire_web_search_news`**: News-focused search with AI summaries
- **`refinire_web_search_research`**: Academic and research-focused search

## Search Types

### General Web Search
```python
result = search_web(
    query="machine learning trends 2024",
    max_results=10,
    include_answer=True
)
```

### News Search
```python
from refinire_tool_tavily import refinire_web_search_news

news = refinire_web_search_news("AI regulations", max_results=5)
print(news["answer"])  # AI-generated news summary
```

### Research Search
```python
from refinire_tool_tavily import refinire_web_search_research

research = refinire_web_search_research("neural networks", max_results=3)
# Includes raw content for detailed analysis
```

## Configuration

### Environment Variables

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `TAVILY_API_KEY` | Tavily API key | Yes | - |
| `REFINIRE_TOOL_TAVILY_MAX_RESULTS` | Default max results | No | 5 |
| `REFINIRE_TOOL_TAVILY_INCLUDE_ANSWER` | Include AI answers | No | false |
| `REFINIRE_TOOL_TAVILY_INCLUDE_RAW_CONTENT` | Include raw content | No | false |

### Advanced Configuration

```python
from refinire_tool_tavily import ConfigManager

config = ConfigManager()
config.print_config_status()  # Check configuration
config.show_env_help()        # Show environment help
```

## Examples

### Basic Search with Filtering
```python
result = search_web(
    query="Python web frameworks",
    max_results=5,
    include_domains=["python.org", "docs.python.org"],
    exclude_domains=["spam.com"],
    include_answer=True
)
```

### Context for Language Models
```python
from refinire_tool_tavily import get_search_context

context = get_search_context("climate change solutions", max_results=3)
# Returns formatted text ready for LLM consumption
```

### Error Handling
```python
result = search_web("test query")

if result["success"]:
    # Process results
    for item in result["results"]:
        print(item["title"])
else:
    print(f"Search failed: {result['error']}")
```

## Development

### Setup Development Environment

```bash
# Clone repository
git clone https://github.com/kitfactory/refinire-tool-tavily.git
cd refinire-tool-tavily

# Install in development mode
source .venv/bin/activate
uv pip install -e .

# Run tests
python -m pytest tests/ -v
```

### Project Structure

```
refinire-tool-tavily/
   src/refinire_tool_tavily/
      __init__.py          # Package exports
      api.py               # Public API functions
      models.py            # Pydantic data models
      service.py           # Tavily service implementation
      tools.py             # Refinire tool decorators
      config.py            # Configuration management
      oneenv_template.py   # OneEnv template
   tests/                   # Test suite
   examples/                # Usage examples
   docs/                    # Documentation
```

## Dependencies

- **refinire**: RefinireAgent integration
- **tavily-python**: Tavily API client
- **pydantic**: Data validation
- **oneenv**: Environment management
- **python-dotenv**: Environment file loading

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

- =� **Documentation**: [Examples and guides](examples/)
- = **Issues**: [GitHub Issues](https://github.com/kitfactory/refinire-tool-tavily/issues)
- =� **Discussions**: [GitHub Discussions](https://github.com/kitfactory/refinire-tool-tavily/discussions)

## Related Projects

- [Refinire](https://github.com/kitfactory/refinire) - AI Agent framework
- [Tavily](https://tavily.com/) - Web search API service
- [OneEnv](https://github.com/kitfactory/oneenv) - Environment variable management