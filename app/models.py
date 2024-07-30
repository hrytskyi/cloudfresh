from flask import current_app as app

def create_board(board_name):
    app.db.boards.insert_one({"name": board_name, "tasks": []})

def get_boards():
    return list(app.db.boards.find())
