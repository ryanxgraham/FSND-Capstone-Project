import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db
from auth import AuthError, requires_auth
from models import Actor, Movie

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.route('/actors', methods=['GET'])
    @requires_auth('get:actors')
    def get_actors(payload):
        actors = list(map(Actor.short, Actor.query.all()))
        result = {
            'success':True,
            'actors':actors
        }
        return jsonify(result)

    @app.route('/movies', methods=['GET'])
    @requires_auth('get:movies')
    def get_movies(payload):
        movies = list(map(Movie.short, Movie.query.all()))
        result = {
            'success':True,
            'movies':movies
        }
        return jsonify(result)

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
                      "success": False,
                      "error": 400,
                      "message": "bad request"
                      }), 400


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
