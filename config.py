import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    DB_NAME = os.getenv('DB_NAME')
    MONGODB_URI = os.getenv('MONGODB_URI')