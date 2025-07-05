"""Basic usage example for refinire-tool-tavily."""

import os
from dotenv import load_dotenv
from refinire_tool_tavily import search_web, get_search_context

# Load environment variables from .env file
load_dotenv()


def main():
    """Demonstrate basic usage of the Tavily search tool."""
    
    # Check if API key is set
    if not os.getenv("TAVILY_API_KEY"):
        print("Error: TAVILY_API_KEY environment variable is not set")
        print("Please set your Tavily API key: export TAVILY_API_KEY=your_api_key_here")
        return
    
    # Basic search example
    print("=== Basic Search Example ===")
    query = "Python programming best practices"
    
    try:
        result = search_web(query, max_results=3)
        
        if result["success"]:
            print(f"Search Query: {result['query']}")
            print(f"Total Results: {result['total_results']}")
            print(f"Search Time: {result.get('search_time', 'N/A')}s")
            print()
            
            for i, search_result in enumerate(result["results"], 1):
                print(f"{i}. {search_result['title']}")
                print(f"   URL: {search_result['url']}")
                print(f"   Content: {search_result['content'][:200]}...")
                if "score" in search_result:
                    print(f"   Score: {search_result['score']}")
                print()
        else:
            print(f"Search failed: {result['error']}")
    
    except Exception as e:
        print(f"Error: {str(e)}")
    
    # Search with answer example
    print("\n=== Search with AI Answer Example ===")
    
    try:
        result = search_web(
            query="What is machine learning?",
            max_results=2,
            include_answer=True
        )
        
        if result["success"]:
            if "answer" in result:
                print(f"AI Answer: {result['answer']}")
                print()
            
            if "follow_up_questions" in result:
                print("Follow-up Questions:")
                for q in result["follow_up_questions"]:
                    print(f"  - {q}")
                print()
        else:
            print(f"Search failed: {result['error']}")
    
    except Exception as e:
        print(f"Error: {str(e)}")
    
    # Context retrieval example
    print("\n=== Search Context Example ===")
    
    try:
        context = get_search_context("Python web frameworks", max_results=2)
        print("Search Context:")
        print(context)
    
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()