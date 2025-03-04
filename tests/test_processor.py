# tests/test_processor.py (Tests for word frequency processor)
import pytest
from app.processor import calculate_word_frequencies

def test_calculate_word_frequencies():
    text = "Python is great. Python is popular."
    result = calculate_word_frequencies(text)
    assert "python" in result
    assert result["python"]["count"] == 2