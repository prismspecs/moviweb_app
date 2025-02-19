from flask import Blueprint, jsonify, request
from datamanager.sqlite_data_manager import SQLiteDataManager

api = Blueprint("api", __name__)
data_manager = SQLiteDataManager()

@api.route('/users', methods=['GET'])
def get_users():
    users = data_manager.list_all_users()
    return jsonify(users)

@api.route('/users/<int:user_id>/movies', methods=['GET'])
def get_user_movies(user_id):
    movies = data_manager.get_user_movies(user_id)
    return jsonify(movies)

@api.route('/users/<int:user_id>/movies', methods=['POST'])
def add_user_movie(user_id):
    data = request.json
    if "name" in data:
        data_manager.add_movie(user_id, data["name"], data.get("director"), data.get("year"), data.get("rating"))
        return jsonify({"message": "Movie added successfully"}), 201
    return jsonify({"error": "Invalid data"}), 400
