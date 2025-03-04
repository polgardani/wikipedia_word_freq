# app/routes.py
from flask import Blueprint, request, jsonify
from .utils import get_word_frequency, get_filtered_keywords

api_bp = Blueprint('api', __name__)

@api_bp.route('/word-frequency', methods=['GET'])
def word_frequency():
    return get_word_frequency(request)

@api_bp.route('/keywords', methods=['POST'])
def keywords():
    return get_filtered_keywords(request)