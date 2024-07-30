from flask import current_app as app
from bson.objectid import ObjectId

def create_board(board_name):
    app.db.boards.insert_one({"name": board_name, "tasks": []})

def get_boards():
    return list(app.db.boards.find())

def get_board(board_id):
    return app.db.boards.find_one({"_id": ObjectId(board_id)})

def add_task(board_id, task_name):
    app.db.boards.update_one(
        {"_id": ObjectId(board_id)},
        {"$push": {"tasks": {"name": task_name, "status": "To Do"}}}
    )
