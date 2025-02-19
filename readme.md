# 🎬 MoviWeb App

**MoviWeb App** is a Flask-based web application that allows users to manage their favorite movies. Users can add, update, and delete movies from their personalized movie lists. The app uses an SQLite database for data storage and features a REST API for data retrieval and manipulation.

## 🚀 Features
- **User Management**: Users can be added dynamically.
- **Movie Management**:
  - Add movies with title, director, year, and rating.
  - Update or delete existing movies.
- **REST API**:
  - `GET /api/users` - List all users.
  - `GET /api/users/<user_id>/movies` - List movies for a user.
  - `POST /api/users/<user_id>/movies` - Add a movie for a user.
- **Preloaded Data**: One-click database population with real movie data.
- **Styled UI**: Clean and responsive layout using CSS.

## 📁 Project Structure
```
MoviWebApp/
|-- api/
|   |-- __init__.py
|   |-- api_routes.py  # API endpoints
|-- datamanager/
|   |-- __init__.py
|   |-- data_manager_interface.py
|   |-- sqlite_data_manager.py
|-- static/
|   |-- styles.css  # CSS styling
|-- templates/
|   |-- base.html  # Layout
|   |-- users.html  # User list
|   |-- movies.html  # Movie list
|-- moviwebapp.db  # SQLite database (auto-created)
|-- app.py  # Main Flask app
|-- config.py  # Configuration settings
|-- requirements.txt  # Dependencies
```

## 🛠 Installation
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/prismspecs/moviweb_app.git
cd moviweb_app
```
### 2️⃣ Set Up a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```
### 4️⃣ Run the Application
```sh
python app.py
```

## 🔗 Usage
### 📜 View Users
- Navigate to **[http://localhost:5000/users](http://localhost:5000/users)** to see the list of users.

### 🎥 View Movies for a User
- Click on a user’s name to view their favorite movies.

### ➕ Add a User
- Enter a new username in the input field and click **Add User**.

### ➕ Add a Movie
- Navigate to a user’s movie list and enter movie details.

### 🔄 Populate Database
- Click **Populate Database** to add sample users and movies.

## 📡 API Endpoints
### 📌 List All Users
```http
GET /api/users
```
### 🎥 List a User’s Movies
```http
GET /api/users/<user_id>/movies
```
### ➕ Add a Movie
```http
POST /api/users/<user_id>/movies
Content-Type: application/json
{
    "name": "Inception",
    "director": "Christopher Nolan",
    "year": 2010,
    "rating": 8.8
}
```

## 🎨 Styling
The application is styled using CSS with a clean and minimal design. The styles are located in `static/styles.css`.

## 🏗 Future Improvements
- User authentication system.
- More detailed movie pages.
- Enhanced search and filtering options.
- Extended API endpoints.

## 💡 Contributing
Pull requests are welcome! Fork the repository, make changes, and submit a PR.

## 📜 License
This project is licensed under the MIT License.

---
### 🏆 Made with ❤️ by [PrismSpecs](https://github.com/prismspecs) 🚀

