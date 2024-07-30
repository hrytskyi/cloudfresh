from flask import current_app as app
from bson.objectid import ObjectId

def create_board(board_name):
    app.db.boards.insert_one({"name": board_name, "tasks": []})

def get_boards():
    return list(app.db.boards.find())

def get_board(board_id):
    return app.db.boards.find_one({"_id": ObjectId(board_id)})

def add_task(board_id, task_name, task_status='Backlog'):
    task = {"_id": ObjectId(), "name": task_name, "status": task_status}
    app.db.boards.update_one(
        {"_id": ObjectId(board_id)},
        {"$push": {"tasks": task}}
    )

def delete_board(board_id):
    app.db.boards.delete_one({"_id": ObjectId(board_id)})

def delete_task(board_id, task_id):
    app.db.boards.update_one(
        {"_id": ObjectId(board_id)},
        {"$pull": {"tasks": {"_id": ObjectId(task_id)}}}
    )
