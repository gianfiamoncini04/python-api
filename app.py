# - API
# - localhost/movies (GET)
# - localhost/movies (POST)
# - localhost/movies/id (GET)
# - localhost/movies/id (PUT)
# - localhost/movies (DELETE)

from flask import Flask, jsonify, request

app = Flask(__name__)

movies = [
	{
		"id": 1,
		"title": "Interestelar",
		"genre": "Sci-fi"
	},
	{
		"id": 2,
		"title": "Avengers",
		"genre": "Adventure"
	},
	{
		"id": 3,
		"title": "Get Up",
		"genre": "Horror"
	}
]

# Consulta (GET)
@app.route('/movies', methods=['GET'])
def get_movies():
    return jsonify(movies)

# Consulta por parametro (GET)
@app.route('/movies/<int:id>', methods=['GET'])
def get_movies_id(id):
    for movie in movies:
        if movie.get('id') == id:
            return jsonify(movie)
        

# Criar (POST)
@app.route('/movies', methods=['POST'])
def create_movies():
    new_movie = request.get_json()        
    movies.append(new_movie)
    return jsonify(movies)
    

# Editar (PUT)
@app.route('/movies/<int:id>', methods=['PUT'])
def edit_movies_id(id):
    movie_edited = request.get_json()        
    for i,movie in enumerate(movies):
        if movie.get('id') == id:
            movies[i].update(movie_edited)
            return jsonify(movies[i])

# REMOVER (DELETE)
@app.route('/movies/<int:id>', methods=['DELETE'])
def delete_movies(id):
    for i,movie in enumerate(movies):
        if movie.get('id') == id:
            del movies[i]
    return jsonify(movies)
    
