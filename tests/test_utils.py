# tests/test_utils.py
import pytest
from flask import Flask
from app.utils import get_word_frequency, get_filtered_keywords

@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    app = Flask(__name__)
    return app

@pytest.fixture
def app_context(app):
    """Create an application context for the test."""
    with app.app_context():
        yield

@pytest.fixture
def mock_request_get():
    class MockRequest:
        args = {"article": "Python (programming language)", "depth": "1"}
    return MockRequest()

@pytest.fixture
def mock_request_post():
    class MockRequest:
        def get_json(self):
            return {
                "article": "Python (programming language)",
                "depth": 1,
                "ignore_list": ["the", "and", "is"],
                "percentile": 80
            }
    return MockRequest()

def test_get_word_frequency(mock_request_get, monkeypatch, app_context):
    monkeypatch.setattr("app.utils.scrape_wikipedia", lambda article, depth: "Python is a programming language.")
    monkeypatch.setattr("app.utils.calculate_word_frequencies", lambda content: {"python": 1, "is": 1, "a": 1, "programming": 1, "language": 1})
    response = get_word_frequency(mock_request_get)
    assert response.json == {"python": 1, "is": 1, "a": 1, "programming": 1, "language": 1}

def test_get_filtered_keywords(mock_request_post, monkeypatch, app_context):
    monkeypatch.setattr("app.utils.scrape_wikipedia", lambda article, depth: "Python is a programming language.")
    monkeypatch.setattr("app.utils.calculate_word_frequencies", lambda content, ignore_list, percentile: {"python": 1, "programming": 1, "language": 1})
    response = get_filtered_keywords(mock_request_post)
    assert response.json == {"python": 1, "programming": 1, "language": 1}
