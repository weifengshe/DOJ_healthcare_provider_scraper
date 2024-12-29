"""Module for formatting and displaying results."""
from typing import List, Dict

def format_results(articles: List[Dict]) -> None:
    """Format and display the processed articles."""
    print(f"Found {len(articles)} articles\n")
    
    for i, article in enumerate(articles, 1):
        print(f"Article {i}:")
        print(f"Title: {article['title']}")
        print(f"Date: {article['date']}")
        print(f"Link: {article['link']}")
        print(f"Summary: {article.get('summary', 'No summary available')}")
        
        providers = article.get('providers', [])
        if providers:
            print("\nHealthcare Providers:")
            for provider in providers:
                org = f" of {provider['facility']}" if 'facility' in provider else ""
                print(f"  - {provider['title']} {provider['name']}{org}")
        else:
            print("\nNo healthcare providers found.")
        
        print("\n---\n")