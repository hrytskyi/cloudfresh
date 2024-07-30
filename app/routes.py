from flask import Blueprint, render_template, request, redirect, url_for
from app.models import create_board, get_boards, get_board, add_task

main = Blueprint('main', __name__)

@main.route('/')
def index():
    boards = get_boards()
    return render_template('index.html', boards=boards)

@main.route('/board/<board_id>')
def board(board_id):
    board = get_board(board_id)
    return render_template('board.html', board=board)

@main.route('/create_board', methods=['POST'])
def create_board_route():
    board_name = request.form.get('board_name')
    create_board(board_name)
    return redirect(url_for('main.index'))

@main.route('/board/<board_id>/add_task', methods=['POST'])
def add_task_route(board_id):
    task_name = request.form.get('task_name')
    task_status = request.form.get('task_status', 'Backlog')
    add_task(board_id, task_name, task_status)
    return redirect(url_for('main.board', board_id=board_id))
