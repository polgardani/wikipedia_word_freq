# app/processor.py (Processes text and calculates word frequency)
import re
from collections import Counter

def calculate_word_frequencies(text, ignore_list=None, percentile=None):
    words = re.findall(r'\b\w+\b', text.lower())
    word_count = Counter(words)
    if ignore_list:
        word_count = {word: count for word, count in word_count.items() if word not in ignore_list}
    total_words = sum(word_count.values())
    word_freq = {word: {"count": count, "percentage": (count / total_words) * 100} for word, count in word_count.items()}
    if percentile:
        threshold = sorted(word_freq.values(), key=lambda x: x["count"])[int(len(word_freq) * (percentile / 100))]["count"]
        word_freq = {word: freq for word, freq in word_freq.items() if freq["count"] >= threshold}
    return word_freq