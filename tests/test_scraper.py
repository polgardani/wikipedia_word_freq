# tests/test_scraper.py (Tests for Wikipedia scraper)
import pytest
from app.scraper import scrape_wikipedia

def test_scrape_wikipedia():
    content = scrape_wikipedia("Python_(programming_language)", 1)
    assert isinstance(content, str)
    assert len(content) > 0

def test_scrape_wikipedia_non_existent():
    content = scrape_wikipedia("ThisArticleDoesNotExist12345", 1)
    assert content is None  # Expect None when article doesn't exist