from flask import Blueprint, render_template, request, redirect, url_for
from app.models import create_board, get_boards

main = Blueprint('main', __name__)

@main.route('/')
def index():
    boards = get_boards()
    return render_template('index.html', boards=boards)

@main.route('/create_board', methods=['POST'])
def create_board_route():
    board_name = request.form.get('board_name')
    create_board(board_name)
    return redirect(url_for('main.index'))
