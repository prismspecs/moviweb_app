from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from datamanager.sqlite_data_manager import SQLiteDataManager
from api.api_routes import api
import requests
import os

app = Flask(__name__)
app.register_blueprint(api, url_prefix='/api')
data_manager = SQLiteDataManager()

OMDB_API_KEY = os.getenv("OMDB_API_KEY", "your_api_key_here")
OMDB_URL = "http://www.omdbapi.com/"

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
    if not name:
        flash("Movie name is required!", "error")
        return redirect(url_for("user_movies", user_id=user_id))

    # Fetch movie details from OMDb
    params = {"t": name, "apikey": OMDB_API_KEY}
    response = requests.get(OMDB_URL, params=params)
    movie_data = response.json()

    if movie_data.get("Response") == "True":
        director = movie_data.get("Director", "Unknown")
        year = movie_data.get("Year", None)
        rating = movie_data.get("imdbRating", None)
    else:
        flash("Movie not found in OMDb, adding with provided details.", "warning")
        director = request.form.get("director", "Unknown")
        year = request.form.get("year", None)
        rating = request.form.get("rating", None)

    data_manager.add_movie(user_id, name, director, year, rating)
    flash("Movie added successfully!", "success")
    return redirect(url_for("user_movies", user_id=user_id))

@app.route('/users/<int:user_id>/update_movie/<int:movie_id>', methods=['GET', 'POST'])
def update_movie(user_id, movie_id):
    movie = data_manager.get_movie_by_id(movie_id)
    if not movie:
        flash("Movie not found!", "error")
        return redirect(url_for("user_movies", user_id=user_id))

    if request.method == 'POST':
        name = request.form.get("name", movie[2])
        director = request.form.get("director", movie[3])
        year = request.form.get("year", movie[4])
        rating = request.form.get("rating", movie[5])
        
        data_manager.update_movie(movie_id, name, director, year, rating)
        flash("Movie updated successfully!", "success")
        return redirect(url_for("user_movies", user_id=user_id))

    return render_template("update_movie.html", movie=movie, user_id=user_id)


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
