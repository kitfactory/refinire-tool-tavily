"""Refinire tool decorators for Tavily search functionality."""

import os
from typing import List, Optional
from dotenv import load_dotenv
from refinire import tool
from .api import search_web, get_search_context

# Load environment variables
load_dotenv()


@tool(
    name="web_search",
    description="Search the web using Tavily API for current information, news, and research"
)
def refinire_web_search(
    query: str,
    max_results: int = 5,
    include_domains: Optional[List[str]] = None,
    exclude_domains: Optional[List[str]] = None,
    include_answer: bool = False,
    include_raw_content: bool = False
) -> dict:
    """Search the web using Tavily API.
    
    This tool provides access to current web information, news, and research
    by searching the internet using the Tavily search API.
    
    Args:
        query: Search query string (required)
        max_results: Maximum number of results to return (1-20, default: 5)
        include_domains: List of domains to include in search (optional)
        exclude_domains: List of domains to exclude from search (optional) 
        include_answer: Include AI-generated answer in response (default: False)
        include_raw_content: Include raw content of web pages (default: False)
    
    Returns:
        Dictionary containing search results with titles, URLs, content snippets,
        and optionally AI-generated answers and follow-up questions.
        
    Example:
        result = web_search("latest Python 3.12 features")
        if result["success"]:
            for item in result["results"]:
                print(f"{item['title']}: {item['url']}")
    """
    return search_web(
        query=query,
        max_results=max_results,
        include_domains=include_domains,
        exclude_domains=exclude_domains,
        include_answer=include_answer,
        include_raw_content=include_raw_content
    )


@tool(
    name="web_search_context",
    description="Get formatted web search context for language model consumption"
)
def refinire_web_search_context(
    query: str,
    max_results: int = 5
) -> str:
    """Get web search results formatted as context for language models.
    
    This tool performs a web search and returns the results in a format
    optimized for providing context to language models and AI agents.
    
    Args:
        query: Search query string
        max_results: Maximum number of results to include (default: 5)
    
    Returns:
        Formatted string containing search results with AI answer,
        titles, URLs, and content snippets ready for LM consumption.
        
    Example:
        context = web_search_context("machine learning trends 2024")
        # Returns formatted text with search results and AI summary
    """
    return get_search_context(query, max_results)


@tool(
    name="web_search_news",
    description="Search for recent news and current events using web search"
)
def refinire_web_search_news(
    query: str,
    max_results: int = 5
) -> dict:
    """Search for recent news and current events.
    
    This tool searches for recent news articles and current events
    by including news-focused domains and requesting AI-generated summaries.
    
    Args:
        query: News search query
        max_results: Maximum number of news results (default: 5)
    
    Returns:
        Dictionary containing news search results with AI-generated summary.
        
    Example:
        news = web_search_news("artificial intelligence regulations 2024")
        print(news["answer"])  # AI summary of recent news
    """
    # Focus on news domains and include AI answer for news summary
    news_domains = [
        "reuters.com", "bbc.com", "cnn.com", "apnews.com",
        "nytimes.com", "wsj.com", "bloomberg.com", "techcrunch.com"
    ]
    
    return search_web(
        query=f"{query} news recent",
        max_results=max_results,
        include_domains=news_domains,
        include_answer=True
    )


@tool(
    name="web_search_research",
    description="Search for research papers, academic content, and technical documentation"
)
def refinire_web_search_research(
    query: str,
    max_results: int = 5
) -> dict:
    """Search for research papers, academic content, and technical documentation.
    
    This tool searches for academic and technical content by focusing on
    research-oriented domains and requesting raw content for detailed analysis.
    
    Args:
        query: Research search query
        max_results: Maximum number of research results (default: 5)
    
    Returns:
        Dictionary containing research-focused search results with raw content.
        
    Example:
        research = web_search_research("transformer architecture attention mechanism")
        for result in research["results"]:
            if result.get("raw_content"):
                # Analyze detailed content
                pass
    """
    # Focus on academic and technical domains
    research_domains = [
        # Academic & Research
        "arxiv.org", "ar5iv.labs.arxiv.org", "scholar.google.com", "ieee.org", "acm.org",
        "nature.com", "science.org", "researchgate.net", "semanticscholar.org",
        "pubmed.ncbi.nlm.nih.gov", "doi.org",
        
        # Technical Documentation & API References
        "docs.python.org", "github.com", "stackoverflow.com", "developer.mozilla.org",
        "docs.microsoft.com", "cloud.google.com", "aws.amazon.com",
        
    ]
    
    return search_web(
        query=f"{query} research paper academic",
        max_results=max_results,
        include_domains=research_domains,
        include_answer=True,
        include_raw_content=True
    )


@tool(
    name="web_search_programming",
    description="Search for programming documentation, API references, and developer resources"
)
def refinire_web_search_programming(
    query: str,
    max_results: int = 5
) -> dict:
    """Search for programming documentation, API references, and developer resources.
    
    This tool searches for programming content, API documentation, and developer resources
    by focusing on programming sites, API documentation platforms, and development communities.
    
    Args:
        query: Programming or API search query
        max_results: Maximum number of results (default: 5)
    
    Returns:
        Dictionary containing programming and API-focused search results.
        
    Example:
        api_results = web_search_programming("REST API authentication methods")
        doc_results = web_search_programming("Python requests library documentation")
    """
    # Focus on programming and API documentation domains
    programming_api_domains = [
        # API Documentation & Tools
        "postman.com", "swagger.io", "openapi.org", "restfulapi.net",
        "apidog.com", "insomnia.rest", "rapidapi.com", "apidocs.io",
        
        # Major Platform APIs
        "developers.google.com", "developer.apple.com", "developer.twitter.com",
        "docs.github.com", "developer.spotify.com", "developers.facebook.com",
        "developer.mozilla.org", "docs.microsoft.com", "cloud.google.com", "aws.amazon.com",
        
        # Technical Documentation
        "docs.python.org", "nodejs.org", "reactjs.org", "vuejs.org", "angular.io",
        "django-rest-framework.org", "flask.palletsprojects.com", "fastapi.tiangolo.com",
        "kubernetes.io", "docker.com", "redis.io", "mongodb.com", "postgresql.org",
        
        # Development Communities & Resources
        "github.com", "stackoverflow.com", "dev.to", "hashnode.com",
        "freecodecamp.org", "codecademy.com", "tutorialspoint.com", "w3schools.com",
        
        # US Tech Sites & Blogs
        "techcrunch.com", "venturebeat.com", "arstechnica.com", "wired.com",
        "medium.com", "hackernoon.com", "smashingmagazine.com", "css-tricks.com",
        
        # Japanese Tech Sites
        "qiita.com", "zenn.dev", "speakerdeck.com", "slideshare.net",
        "tech.recruit-mp.co.jp", "engineering.mercari.com", "techblog.yahoo.co.jp",
        
        # Open Source & Package Repositories
        "pypi.org", "npmjs.com", "packagist.org", "rubygems.org", "crates.io"
    ]
    
    return search_web(
        query=f"{query} documentation API guide tutorial",
        max_results=max_results,
        include_domains=programming_api_domains,
        include_answer=True,
        include_raw_content=True
    )