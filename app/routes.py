# app/routes.py
from flask import Blueprint, request, jsonify
from .scraper import scrape_wikipedia
from .processor import calculate_word_frequencies

api_bp = Blueprint('api', __name__)

@api_bp.route('/word-frequency', methods=['GET'])
def word_frequency():
    article = request.args.get('article')
    depth = int(request.args.get('depth', 1))
    content = scrape_wikipedia(article, depth)
    word_freq = calculate_word_frequencies(content)
    return jsonify(word_freq)

@api_bp.route('/keywords', methods=['POST'])
def keywords():
    data = request.get_json()
    article = data['article']
    depth = data['depth']
    ignore_list = set(data['ignore_list'])
    percentile = data['percentile']
    content = scrape_wikipedia(article, depth)
    word_freq = calculate_word_frequencies(content, ignore_list, percentile)
    return jsonify(word_freq)