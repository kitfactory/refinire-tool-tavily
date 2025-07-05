"""Example demonstrating the new tech and API search functionality."""

import os
from dotenv import load_dotenv
from refinire_tool_tavily import refinire_web_search_programming_api

# Load environment variables
load_dotenv()


def main():
    """Demonstrate tech and API search functionality."""
    
    print("Refinire Programming & API Search Examples")
    print("=" * 40)
    print()
    
    # Check if API key is set
    if not os.getenv("TAVILY_API_KEY"):
        print("Error: TAVILY_API_KEY environment variable is not set")
        print("Please set your Tavily API key")
        return
    
    # Example 1: API Documentation Search
    print("1. API Documentation Search")
    print("-" * 30)
    try:
        result = refinire_web_search_programming_api("REST API authentication methods", max_results=3)
        if result["success"]:
            print(f"Found {result['total_results']} API documentation results:")
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
    
    # Example 2: Python Library Documentation
    print("2. Python Library Documentation")
    print("-" * 35)
    try:
        result = refinire_web_search_programming_api("Python requests library tutorial", max_results=3)
        if result["success"]:
            if "answer" in result:
                print("AI Summary:")
                print(result["answer"])
                print()
            
            print("Documentation Results:")
            for i, item in enumerate(result["results"], 1):
                print(f"  {i}. {item['title']}")
                print(f"     URL: {item['url']}")
                print()
        else:
            print(f"Search failed: {result['error']}")
    except Exception as e:
        print(f"Error: {e}")
    
    print("=" * 40)
    print()
    
    # Example 3: Framework Documentation
    print("3. Framework Documentation")
    print("-" * 27)
    try:
        result = refinire_web_search_programming_api("FastAPI async database", max_results=3)
        if result["success"]:
            print("Framework Documentation:")
            for i, item in enumerate(result["results"], 1):
                print(f"  {i}. {item['title']}")
                print(f"     URL: {item['url']}")
                if item.get("raw_content"):
                    print(f"     Raw content available: {len(item['raw_content'])} chars")
                print()
        else:
            print(f"Search failed: {result['error']}")
    except Exception as e:
        print(f"Error: {e}")
    
    print("=" * 40)
    print()
    
    # Example 4: Japanese Tech Content
    print("4. Japanese Tech Content")
    print("-" * 25)
    try:
        result = refinire_web_search_programming_api("Python 非同期処理 async await", max_results=3)
        if result["success"]:
            print("Japanese Tech Results:")
            for i, item in enumerate(result["results"], 1):
                print(f"  {i}. {item['title']}")
                print(f"     URL: {item['url']}")
                print()
        else:
            print(f"Search failed: {result['error']}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()