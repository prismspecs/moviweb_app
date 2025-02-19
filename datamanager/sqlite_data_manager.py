import sqlite3
from datamanager.data_manager_interface import DataManagerInterface

DB_FILE = "moviwebapp.db"

class SQLiteDataManager(DataManagerInterface):
    """SQLite implementation of the DataManagerInterface."""

    def __init__(self):
        self._create_tables()

    def _connect(self):
        """Establish a database connection."""
        return sqlite3.connect(DB_FILE, check_same_thread=False)

    def _create_tables(self):
        """Create tables if they don't exist."""
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT UNIQUE NOT NULL
                );
            """)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS movies (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    name TEXT NOT NULL,
                    director TEXT,
                    year INTEGER,
                    rating REAL,
                    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
                );
            """)
            conn.commit()

    def list_all_users(self):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users")
            return cursor.fetchall()

    def get_user_movies(self, user_id):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM movies WHERE user_id = ?", (user_id,))
            return cursor.fetchall()

    def add_user(self, name):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (name) VALUES (?)", (name,))
            conn.commit()
            return cursor.lastrowid

    def add_movie(self, user_id, name, director, year, rating):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO movies (user_id, name, director, year, rating) 
                VALUES (?, ?, ?, ?, ?)
            """, (user_id, name, director, year, rating))
            conn.commit()

    def update_movie(self, movie_id, name, director, year, rating):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE movies
                SET name = ?, director = ?, year = ?, rating = ?
                WHERE id = ?
            """, (name, director, year, rating, movie_id))
            conn.commit()

    def delete_movie(self, movie_id):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM movies WHERE id = ?", (movie_id,))
            conn.commit()
