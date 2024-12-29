from scraping.fetcher import fetch_page
from scraping.parser import parse_articles
from utils.logger import log_results

def main():
    try:
        html_content = fetch_page('https://www.justice.gov/news/press-releases')
        articles = parse_articles(html_content)
        log_results(articles)
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()