# app/utils.py
from flask import jsonify
from .scraper import scrape_wikipedia
from .processor import calculate_word_frequencies

def get_word_frequency(request):
    article = request.args.get('article')
    depth = int(request.args.get('depth', 1))
    content = scrape_wikipedia(article, depth)
    
    if content is None:
        return jsonify({"error": "This article does not exist."}), 404
    
    word_freq = calculate_word_frequencies(content)
    return jsonify(word_freq)

def get_filtered_keywords(request):
    data = request.get_json()
    article = data['article']
    depth = data['depth']
    ignore_list = set(data['ignore_list'])
    percentile = data['percentile']
    content = scrape_wikipedia(article, depth)
    
    if content is None:
        return jsonify({"error": "This article does not exist."}), 404
    
    word_freq = calculate_word_frequencies(content, ignore_list, percentile)
    return jsonify(word_freq)