from flask import Flask, render_template, request, redirect, url_for
from datamanager.sqlite_data_manager import SQLiteDataManager
from api.api_routes import api

app = Flask(__name__)
app.register_blueprint(api, url_prefix='/api')
data_manager = SQLiteDataManager()

@app.route('/')
def home():
    return render_template("base.html")

@app.route('/users')
def list_users():
    users = data_manager.list_all_users()
    return render_template("users.html", users=users)

@app.route('/users/<int:user_id>')
def user_movies(user_id):
    movies = data_manager.get_user_movies(user_id)
    return render_template("movies.html", movies=movies, user_id=user_id)

@app.route('/add_user', methods=['POST'])
def add_user():
    name = request.form.get("name")
    if name:
        data_manager.add_user(name)
    return redirect(url_for("list_users"))

@app.route('/users/<int:user_id>/add_movie', methods=['POST'])
def add_movie(user_id):
    name = request.form.get("name")
    director = request.form.get("director")
    year = request.form.get("year")
    rating = request.form.get("rating")
    if name:
        data_manager.add_movie(user_id, name, director, year, rating)
    return redirect(url_for("user_movies", user_id=user_id))

@app.route('/populate_db')
def populate_db():
    """Populate the database with sample users and movies."""
    users = ["Alice", "Bob", "Charlie"]
    movies = [
        {"name": "Inception", "director": "Christopher Nolan", "year": 2010, "rating": 8.8},
        {"name": "The Matrix", "director": "The Wachowskis", "year": 1999, "rating": 8.7},
        {"name": "Interstellar", "director": "Christopher Nolan", "year": 2014, "rating": 8.6},
        {"name": "The Godfather", "director": "Francis Ford Coppola", "year": 1972, "rating": 9.2},
    ]

    for user in users:
        user_id = data_manager.add_user(user)
        for movie in movies:
            data_manager.add_movie(user_id, movie["name"], movie["director"], movie["year"], movie["rating"])

    return redirect(url_for('list_users'))


if __name__ == '__main__':
    app.run(debug=True)
