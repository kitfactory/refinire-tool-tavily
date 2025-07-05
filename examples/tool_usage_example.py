"""Example demonstrating individual Refinire tools usage."""

import os
from dotenv import load_dotenv
from refinire_tool_tavily import (
    refinire_web_search,
    refinire_web_search_context,
    refinire_web_search_news, 
    refinire_web_search_research
)

# Load environment variables
load_dotenv()


def main():
    """Demonstrate individual tool usage."""
    
    print("Refinire Tavily Tools Usage Examples")
    print("=" * 40)
    print()
    
    # 1. Basic web search
    print("1. Basic Web Search")
    print("-" * 20)
    try:
        result = refinire_web_search("Python programming best practices", max_results=3)
        if result["success"]:
            print(f"Found {result['total_results']} results:")
            for i, item in enumerate(result["results"], 1):
                print(f"  {i}. {item['title']}")
                print(f"     URL: {item['url']}")
                print(f"     Content: {item['content'][:100]}...")
                print()
        else:
            print(f"Search failed: {result['error']}")
    except Exception as e:
        print(f"Error: {e}")
    
    print("=" * 40)
    print()
    
    # 2. Web search context (formatted for LLM)
    print("2. Web Search Context (for LLM)")
    print("-" * 30)
    try:
        context = refinire_web_search_context("machine learning trends", max_results=2)
        print("Context for language model:")
        print(context[:500] + "..." if len(context) > 500 else context)
    except Exception as e:
        print(f"Error: {e}")
    
    print("=" * 40)
    print()
    
    # 3. News search
    print("3. News Search")
    print("-" * 15)
    try:
        news = refinire_web_search_news("artificial intelligence", max_results=2)
        if news["success"]:
            if "answer" in news:
                print("AI News Summary:")
                print(news["answer"])
                print()
            print("News Articles:")
            for i, item in enumerate(news["results"], 1):
                print(f"  {i}. {item['title']}")
                print(f"     URL: {item['url']}")
                print()
        else:
            print(f"News search failed: {news['error']}")
    except Exception as e:
        print(f"Error: {e}")
    
    print("=" * 40)
    print()
    
    # 4. Research search
    print("4. Research Search")
    print("-" * 18)
    try:
        research = refinire_web_search_research("neural networks", max_results=2)
        if research["success"]:
            print("Research Results:")
            for i, item in enumerate(research["results"], 1):
                print(f"  {i}. {item['title']}")
                print(f"     URL: {item['url']}")
                if item.get("raw_content"):
                    print(f"     Raw content available: {len(item['raw_content'])} chars")
                print()
        else:
            print(f"Research search failed: {research['error']}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()