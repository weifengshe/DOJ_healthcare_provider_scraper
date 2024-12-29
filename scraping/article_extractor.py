"""Module for extracting and deduplicating articles."""
from typing import List, Dict, Set, Optional
from bs4 import BeautifulSoup
from dataclasses import dataclass
from datetime import datetime
import logging 

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class Article:
    """Article data structure."""
    title: str
    link: str
    date: str
    teaser: str

    def __hash__(self) -> int:
        """Hash based on link to ensure uniqueness."""
        return hash(self.link)

    def __eq__(self, other) -> bool:
        """Compare articles based on link."""
        if not isinstance(other, Article):
            return False
        return self.link == other.link

def extract_articles(html_contents: List[str]) -> List[Dict]:
    """Extract and deduplicate articles from multiple HTML pages."""
    unique_articles: Set[Article] = set()
    
    for html in html_contents:
        if not html:
            continue
            
        soup = BeautifulSoup(html, 'html.parser')
        for article_div in soup.select('.views-row'):
            article = extract_single_article(article_div)
            if article:
                unique_articles.add(article)
    
    # Convert to list and sort by date (newest first)
    sorted_articles = sorted(
        unique_articles,
        key=lambda x: datetime.strptime(x.date, '%Y-%m-%d'),
        reverse=True
    )
    
    logger.info(f"Extracted {len(sorted_articles)} unique articles")
    return [article_to_dict(article) for article in sorted_articles]

def extract_single_article(article_div) -> Optional[Article]:
    """Extract data from a single article div."""
    try:
        article = article_div.select_one('article.news-content-listing.node-press-release .node-content')
        if not article:
            return None
            
        title_elem = article.select_one('.news-title a')
        if not title_elem:
            return None
            
        title = title_elem.select_one('.field-formatter--string')
        title = title.text.strip() if title else title_elem.text.strip()
        link = f"https://www.justice.gov{title_elem['href']}"
        
        date_elem = article.select_one('.node-date time')
        date = date_elem['datetime'].split('T')[0] if date_elem else ''
        
        teaser = article.select_one('.field-formatter--smart-trim')
        teaser = teaser.text.strip() if teaser else ''
        
        return Article(title=title, link=link, date=date, teaser=teaser)
    except Exception as e:
        logger.error(f"Error extracting article: {str(e)}")
        return None

def article_to_dict(article: Article) -> Dict:
    """Convert Article object to dictionary."""
    return {
        'title': article.title,
        'link': article.link,
        'date': article.date,
        'teaser': article.teaser
    }