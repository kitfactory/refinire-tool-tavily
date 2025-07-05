"""Example demonstrating RefinireAgent with Tavily search tools."""

from refinire import Agent
from refinire_tool_tavily import (
    refinire_web_search,
    refinire_web_search_context, 
    refinire_web_search_news,
    refinire_web_search_research
)


def main():
    """Demonstrate RefinireAgent with Tavily search tools."""
    
    print("RefinireAgent with Tavily Search Tools Demo")
    print("=" * 45)
    print()
    
    # Create agent with web search tools
    agent = Agent(
        name="WebSearchAgent",
        instructions="""You are a helpful assistant with access to web search capabilities.
        Use the web search tools to find current information, news, and research when needed.
        Always provide sources and be accurate with the information you find.""",
        tools=[
            refinire_web_search,
            refinire_web_search_context,
            refinire_web_search_news,
            refinire_web_search_research
        ]
    )
    
    print("Available tools:")
    for tool in agent.tools:
        print(f"  - {tool.name}: {tool.description}")
    print()
    
    # Example queries
    queries = [
        "What are the latest developments in Python 3.12?",
        "Find recent news about artificial intelligence regulations",
        "Search for research papers on transformer architectures"
    ]
    
    for i, query in enumerate(queries, 1):
        print(f"{i}. Query: {query}")
        print("-" * 50)
        
        try:
            # Run the agent with the query
            result = agent.run(query)
            print(f"Response: {result}")
        except Exception as e:
            print(f"Error: {e}")
        
        print()
        print("=" * 45)
        print()


if __name__ == "__main__":
    main()