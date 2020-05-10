import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from auth import AuthError, requires_auth
from models import Actor, Movie, setup_db
import sys


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.after_request
    def after_request(response):
        response.headers.add(
            'Access-Control-Allow-Headers',
            'Content-Type, Authorization')
        response.headers.add(
            'Access-Control-Allow-Methods',
            'GET,POST,DELETE,PATCH')
        return response

    @app.route('/actors', methods=['GET'])
    @requires_auth('get:actors')
    def get_actors(payload):
        actors = list(map(Actor.format, Actor.query.all()))
        if actors is None:
            abort(404)
        result = {
            'success': True,
            'actors': actors
        }
        return jsonify(result)

    @app.route('/movies', methods=['GET'])
    @requires_auth('get:movies')
    def get_movies(payload):
        movies = list(map(Movie.format, Movie.query.all()))
        if movies is None:
            abort(404)
        result = {
            'success': True,
            'movies': movies
        }
        return jsonify(result)

    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def post_actor(payload):
        data = request.get_json()

        try:
            actor = Actor(
                        name=data['name'],
                        gender=data['gender'],
                        age=data['age']
                        )
            actor.insert()

            result = {
                'success': True,
                'created': actor.id,
                'actor_created': actor.name
                }
            return jsonify(result)

        except Exception:
            print(sys.exc_info())
            abort(422)

    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movies')
    def post_movie(payload):
        data = request.get_json()

        try:
            movie = Movie(
                        title=data['title'],
                        release_date=data['release_date'],
                        genre=data['genre']
                        )
            movie.insert()

            result = {
                'success': True,
                'created': movie.id,
                'movie_created': movie.title
                }
            return jsonify(result)

        except Exception:
            print(sys.exc_info())
            abort(422)

    @app.route('/actors/<int:id>', methods=['PATCH'])
    @requires_auth('patch:actors')
    def patch_actor(payload, id):
        actor = Actor.query.filter(Actor.id == id).one_or_none()
        if actor is None:
            abort(404)
        try:
            data = request.get_json()
            if 'name' in data:
                actor.name = data['name']
            if 'gender' in data:
                actor.gender = data['gender']
            if 'age' in data:
                actor.age = data['age']
            actor.update()
            result = {
                'success': True,
                'actor': Actor.format(actor)
                }
            return jsonify(result)
        except Exception:
            print(sys.exc_info())
            abort(422)

    @app.route('/movies/<int:id>', methods=['PATCH'])
    @requires_auth('patch:movies')
    def patch_movie(payload, id):
        movie = Movie.query.filter(Movie.id == id).one_or_none()
        if movie is None:
            abort(404)
        try:
            data = request.get_json()
            if 'actors' in data:
                movie.actors.append(actors)
            if 'title' in data:
                movie.name = data['title']
            if 'release_date' in data:
                movie.release_date = data['release_date']
            if 'genre' in data:
                movie.genre = data['genre']
            movie.update()
            result = {
                'success': True,
                'movie': Movie.format(movie)
                }
            return jsonify(result)
        except Exception:
            print(sys.exc_info())
            abort(422)

    @app.route('/actors/<int:id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actor(payload, id):
        actor = Actor.query.filter(Actor.id == id).one_or_none()
        if actor is None:
            abort(404)
        actor.delete()

        result = {
            'success': True,
            'delete': id
        }
        return jsonify(result)

    @app.route('/movies/<int:id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movies(payload, id):
        movie = Movie.query.filter(Movie.id == id).one_or_none()
        if movie is None:
            abort(404)
        movie.delete()

        result = {
            'success': True,
            'delete': id
        }
        return jsonify(result)

    @app.errorhandler(AuthError)
    def auth_error(error):
        return jsonify({
            "success": False,
            "error": error.status_code,
            "message": error.error['code']
            }), 401

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
                      "success": False,
                      "error": 404,
                      "message": "resource not found"
                      }), 404

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
                        "success": False,
                        "error": 422,
                        "message": "unprocessable"
                        }), 422

    return app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
