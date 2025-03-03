# app/__init__.py
from flask import Flask

def create_app():
    app = Flask(__name__)
    from .routes import api_bp
    app.register_blueprint(api_bp)
    return app