def log_results(articles):
    """Log scraped articles to console."""
    print(f"Found {len(articles)} articles\n")
    
    for i, article in enumerate(articles, 1):
        print(f"Article {i}:")
        print(f"Title: {article['title']}")
        print(f"Date: {article['date']}")
        print(f"Link: {article['link']}")
        print(f"Summary: {article['summary']}")
        
        if article['healthcare_providers']:
            print("Healthcare Providers Found:")
            for provider in article['healthcare_providers']:
                print(f"  - {provider}")
        
        print("\n")