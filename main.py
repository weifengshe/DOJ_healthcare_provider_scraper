
from scraping.parser import fetch_article_content
from services.llm import summarize_content, analyze_healthcare_providers
from utils.formatter import format_results
from typing import Dict, List
import asyncio
from scraping.page_fetcher import fetch_pages
from scraping.article_extractor import extract_articles
from services.utils.async_utils import run_in_threadpool
from utils.date_utils import get_monday_of_last_week, get_sunday_of_last_week

async def process_article(article: Dict) -> Dict:
    """Process a single article with content fetching and analysis."""
    content = await run_in_threadpool(fetch_article_content, article['link'])
    # print(len(content))
    if not content:
        article['summary'] = 'Content not available'
        article['providers'] = []
        return article
    
    # Get LLM analysis
    summary = await run_in_threadpool(summarize_content, content)
    providers_result = await run_in_threadpool(analyze_healthcare_providers, content)
    
    return {
        **article,
        'summary': summary or 'No summary available',
        'providers': providers_result.get('providers', [])
    }

async def main():
    monday = get_monday_of_last_week()
    sunday = get_sunday_of_last_week()
    try:
        # Fetch main page
        base_url = 'https://www.justice.gov/'
        search_by_date = f'news?search_api_fulltext=%20&start_date={monday}&end_date={sunday}' 
        search_by_topic = '&sort_by=search_api_relevance&f%5B0%5D=facet_topics%'
        topics = ['3A32601', '3A3936', '3A34671']
        page_urls = [base_url + search_by_date + search_by_topic + topic for topic in topics]


        
        # Fetch all pages concurrently
        html_contents = await fetch_pages(page_urls)
        
        # Extract and deduplicate articles
        articles = extract_articles(html_contents)

        # Process articles concurrently
        processed_articles = await asyncio.gather(
            *[process_article(article) for article in articles]
        )
        
        # Format and display results
        format_results(processed_articles)

    except Exception as e:
        print(f"Error in main process: {str(e)}")

if __name__ == "__main__":
    asyncio.run(main())