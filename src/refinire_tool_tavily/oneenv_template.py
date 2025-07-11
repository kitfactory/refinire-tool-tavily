"""OneEnv template for refinire-tool-tavily environment variables."""


def tavily_template():
    """OneEnv template function for Tavily search tool configuration.
    
    Returns:
        Dictionary containing environment variable groups and specifications
    """
    return {
        "groups": {
            "Tavily API Configuration": {
                "TAVILY_API_KEY": {
                    "description": "Tavily API key for web search functionality. Get your API key from https://tavily.com/",
                    "default": "your_tavily_api_key_here",
                    "required": True,
                    "importance": "critical"
                }
            },
            "Search Defaults": {
                "REFINIRE_TOOL_TAVILY_MAX_RESULTS": {
                    "description": "Default maximum number of search results to return",
                    "default": "5",
                    "required": False,
                    "importance": "optional"
                },
                "REFINIRE_TOOL_TAVILY_INCLUDE_ANSWER": {
                    "description": "Include AI-generated answer by default",
                    "default": "false",
                    "required": False,
                    "importance": "optional"
                },
                "REFINIRE_TOOL_TAVILY_INCLUDE_RAW_CONTENT": {
                    "description": "Include raw content of web pages by default",
                    "default": "false",
                    "required": False,
                    "importance": "optional"
                }
            }
        }
    }