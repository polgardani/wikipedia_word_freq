# app/scraper.py (Handles Wikipedia scraping)
import requests
from bs4 import BeautifulSoup

def scrape_wikipedia(article, depth, visited=None):
    if visited is None:
        visited = set()
    if article in visited or depth == 0:
        return ""
    visited.add(article)
    url = f"https://en.wikipedia.org/wiki/{article}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    content = ' '.join(p.text for p in soup.find_all('p'))
    links = [a['href'].split('/')[-1] for a in soup.select('p a[href^="/wiki/"]') if ':' not in a['href']]
    for link in links[:5]:  # Limit the number of links followed
        content += scrape_wikipedia(link, depth - 1, visited)
    return content