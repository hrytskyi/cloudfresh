import pytest
from app import create_app, db
from models import Board, Task

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Kanban Boards" in response.data

def test_create_board(client):
    response = client.post('/create_board', data={'name': 'Test Board'}, follow_redirects=True)
    assert response.status_code == 200
    assert b"Test Board" in response.data

def test_view_board(client):
    client.post('/create_board', data={'name': 'Test Board'}, follow_redirects=True)
    response = client.get('/board/1')
    assert response.status_code == 200
    assert b"Test Board" in response.data

def test_create_task(client):
    client.post('/create_board', data={'name': 'Test Board'}, follow_redirects=True)
    response = client.post('/create_task/1', data={'title': 'Test Task', 'description': 'This is a test task', 'status': 'Backlog'}, follow_redirects=True)
    assert response.status_code == 200
    assert b"Test Task" in response.data
    assert b"This is a test task" in response.data
    assert b"Backlog" in response.data

def test_delete_task(client):
    client.post('/create_board', data={'name': 'Test Board'}, follow_redirects=True)
    client.post('/create_task/1', data={'title': 'Test Task', 'description': 'This is a test task', 'status': 'Backlog'}, follow_redirects=True)
    response = client.post('/delete_task/1', follow_redirects=True)
    assert response.status_code == 200
    assert b"Test Task" not in response.data

def test_delete_board(client):
    client.post('/create_board', data={'name': 'Test Board'}, follow_redirects=True)
    response = client.post('/delete_board/1', follow_redirects=True)
    assert response.status_code == 200
    assert b"Test Board" not in response.data
