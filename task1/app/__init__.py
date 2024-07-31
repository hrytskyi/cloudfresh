from flask import Flask
from app.routes import main
from pymongo import MongoClient
import os

def create_app():
    app = Flask(__name__, template_folder='../templates')
    app.config.from_object('config.Config')
    
    # Ініціалізація MongoDB
    client = MongoClient(os.getenv('MONGODB_URI'))
    db_name = os.getenv('DB_NAME')
    if not db_name:
        raise ValueError("DB_NAME environment variable not set")
    app.db = client[db_name]
    
    app.register_blueprint(main)
    
    return app
