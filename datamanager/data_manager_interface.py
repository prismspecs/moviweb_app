from abc import ABC, abstractmethod

class DataManagerInterface(ABC):
    """Abstract interface for data managers."""

    @abstractmethod
    def list_all_users(self):
        pass

    @abstractmethod
    def get_user_movies(self, user_id):
        pass

    @abstractmethod
    def add_user(self, name):
        pass

    @abstractmethod
    def add_movie(self, user_id, name, director, year, rating):
        pass

    @abstractmethod
    def update_movie(self, movie_id, name, director, year, rating):
        pass

    @abstractmethod
    def delete_movie(self, movie_id):
        pass
