from bs4 import BeautifulSoup
from typing import List, Dict, Optional
from .fetcher import fetch_page

def extract_article_urls(html: str) -> List[Dict[str, str]]:
    """Extract article URLs and metadata from the main page."""
    soup = BeautifulSoup(html, 'html.parser')
    articles = []
    
    for article_div in soup.select('.views-row'):
        # Find the article content within the views-row
        article = article_div.select_one('.node-press-release .node-content')
        if not article:
            continue
            
        # Extract title and link
        title_elem = article.select_one('.news-title a')
        if not title_elem:
            continue
            
        title = title_elem.select_one('.field-formatter--string')
        title = title.text.strip() if title else title_elem.text.strip()
        link = f"https://www.justice.gov{title_elem['href']}"
        
        # Extract teaser
        teaser = article.select_one('.field-formatter--smart-trim')
        teaser = teaser.text.strip() if teaser else ''
        
        # Extract date
        date_elem = article.select_one('.node-date time')
        date = date_elem['datetime'] if date_elem else ''
        
        articles.append({
            'title': title,
            'link': link,
            'date': date,
            'teaser': teaser
        })
    print(articles)
    return articles

def fetch_article_content(url: str) -> Optional[str]:
    """Fetch and extract the content of a single article."""
    html = fetch_page(url)
    if not html:
        return None
        
    soup = BeautifulSoup(html, 'html.parser')
    content = soup.select_one('.node-body .field-formatter--text-default')
    print(len(content.get_text(strip=True) ))
    return content.get_text(strip=True) if content else None