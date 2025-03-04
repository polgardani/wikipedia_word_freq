# tests/test_routes.py (Tests for API routes)
import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    return app.test_client()

def test_word_frequency(client):
    response = client.get("/word-frequency?article=Python_(programming_language)&depth=1")
    assert response.status_code == 200
    assert isinstance(response.json, dict)


def test_word_frequency_non_existent_article(client):
    response = client.get("/word-frequency?article=ThisArticleDoesNotExist12345&depth=1")
    assert response.status_code == 404  # Should return 404 Not Found
    assert response.json == {"error": "This article does not exist."}  # Error message must match