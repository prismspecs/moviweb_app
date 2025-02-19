from flask import Flask, render_template, request, redirect, url_for
from datamanager.sqlite_data_manager import SQLiteDataManager

app = Flask(__name__)
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

if __name__ == '__main__':
    app.run(debug=True)
