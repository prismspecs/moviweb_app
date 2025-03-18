import pytest
from app import app, data_manager

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_add_user(client):
    response = client.post("/add_user", data={"name": "Test User"})
    assert response.status_code == 302  # Redirect
    users = data_manager.list_all_users()
    assert any(user[1] == "Test User" for user in users)

def test_add_movie(client):
    user_id = data_manager.add_user("Movie Tester")
    response = client.post(f"/users/{user_id}/add_movie", data={"name": "Inception"})
    assert response.status_code == 302  # Redirect
    movies = data_manager.get_user_movies(user_id)
    assert any(movie[2] == "Inception" for movie in movies)
