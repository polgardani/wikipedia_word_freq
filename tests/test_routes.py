# tests/test_routes.py (Tests for API routes)
import pytest
from app import create_app

def test_word_frequency():
    app = create_app()
    client = app.test_client()
    response = client.get("/word-frequency?article=Python_(programming_language)&depth=1")
    assert response.status_code == 200
    assert isinstance(response.json, dict)