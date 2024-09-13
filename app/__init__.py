from flask import Flask
from app.routes import main
from pymongo import MongoClient
import os

def create_app():
    app = Flask(__name__, template_folder='../templates')
    
    # Ініціалізація MongoDB
    mongodb_uri = os.getenv('MONGODB_URI')
    if not mongodb_uri:
        raise ValueError("MONGODB_URI environment variable not set")
    client = MongoClient(mongodb_uri)

    db_name = os.getenv('DB_NAME')
    if not db_name:
        raise ValueError("DB_NAME environment variable not set")
    app.db = client[db_name]
    
    # Реєстрація blueprint
    app.register_blueprint(main)

    return app
