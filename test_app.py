"""TESTING SUITE FOR TRIVIA API."""
import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Actor, Movie


class CapstoneTestCase(unittest.TestCase):
    """This class represents the trivia test case."""

    def setUp(self):
        """Define test variables and initialize app."""
        self.token_assistant = os.environ['assistant_token']
        self.token_director = os.environ['director_token']
        self.token_producer = os.environ['producer_token']
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "capstonetest"
        self.database_path = "postgres://postgres@localhost:5432/capstonetest"
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        self.test_actor_success = {
            'name': 'name',
            'gender': 'gender',
            'age': 'age'
        }
        self.test_actor_fail = {
            'name': False,
        }
        self.test_movie_success = {
            'title': 'title',
            'release_date': 'release_date',
            'genre': 'genre'
        }
        self.test_movie_fail = {
            'title':False
        }
    def tearDown(self):
        """Execute after reach test."""
        pass



### /actors tests
# / GET

    def test_get_actors(self):
        res = self.client().get('/actors', headers={
            "Authorization": 'bearer '+self.token_assistant})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])

    def test_get_actors_endpoint_error(self):
        res = self.client().get('/actor', headers={
            "Authorization": 'bearer '+self.token_assistant})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(body['success'], False)

    def test_get_actors_bad_auth(self):
        res = self.client().get('/actors')
        body = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(body['success'], False)
# / POST
    def test_post_actor_success(self):
        res = self.client().post('/actors', json=self.test_actor_success, headers={
            "Authorization": 'bearer '+self.token_director})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actor_created'])
        self.assertTrue(data['created'])

    def test_post_actors_bad_data(self):
        res = self.client().post('/actors', json=self.test_actor_fail, headers={
            "Authorization": 'bearer '+self.token_director})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)

    def test_post_actor_bad_auth(self):
        res = self.client().delete('/actors', json=self.test_actor_success, headers={
            "Authorization": 'bearer '+self.token_assistant})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
# /PATCH
    def test_patch_actor_success(self):
        res = self.client().patch('/actors/1', json={'name': 'patch'}, headers={
            "Authorization": 'bearer '+self.token_director})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_patch_actor_bad_data(self):
        res = self.client().patch('/actors/1', json={'car': 'toyota'}, headers={
            "Authorization": 'bearer '+self.token_director})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)

    def test_patch__nonexistant_actor(self):
        res = self.client().patch('/actors/666', json={'name': 'patch'}, headers={
            "Authorization": 'bearer '+self.token_director})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_patch_actor_bad_auth(self):
        res = self.client().patch('/actors/1', json={'name': 'patch'}, headers={
            "Authorization": 'bearer '+self.token_assistant})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
# / DELETE
    def test_delete_actor_success(self):
        res = self.client().delete('/actors/1', headers={
            "Authorization": 'bearer '+self.token_director})
        data = json.loads(res.data)
        actor = Actor.query.filter_by(id=1).one_or_none()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(actor, None)

    def test_delete_nonexistant_actor(self):
        res = self.client().delete('/actors/666', headers={
            "Authorization": 'bearer '+self.token_director})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)

    def test_delete_actor_bad_auth(self):
        res = self.client().delete('/actors/1', headers={
            "Authorization": 'bearer '+self.token_assistant})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
### /movie tests
# / GET
    def test_get_movies(self):
        res = self.client().get('/movies', headers={
            "Authorization": 'bearer '+self.token_assistant})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])

    def test_get_movies_endpoint_error(self):
        res = self.client().get('/movie', headers={
            "Authorization": 'bearer '+self.token_assistant})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(body['success'], False)

    def test_get_movies_bad_auth(self):
        res = self.client().get('/movies')
        body = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(body['success'], False)
# / POST
    def test_post_movie_success(self):
        res = self.client().post('/movies', json=self.test_movie_success, headers={
            "Authorization": 'bearer '+self.token_director})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movie_created'])
        self.assertTrue(data['created'])

    def test_post_actors_bad_data(self):
        res = self.client().post('/movies', json=self.test_movie_fail, headers={
            "Authorization": 'bearer '+self.token_director})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)

    def test_post_movie_bad_auth(self):
        res = self.client().delete('/actors', json=self.test_actor_success, headers={
            "Authorization": 'bearer '+self.token_director})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
# /PATCH
    def test_patch_movie_success(self):
        res = self.client().patch('/movie/1', json={'title': 'patch'}, headers={
            "Authorization": 'bearer '+self.token_director})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_patch_movie_bad_data(self):
        res = self.client().patch('/movies/1', json={'car': 'toyota'}, headers={
            "Authorization": 'bearer '+self.token_director})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)

    def test_patch__nonexistant_movie(self):
        res = self.client().patch('/movies/666', json={'title': 'patch'}, headers={
            "Authorization": 'bearer '+self.token_director})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_patch_movie_bad_auth(self):
        res = self.client().patch('/movies/1', json={'title': 'patch'}, headers={
            "Authorization": 'bearer '+self.token_assistant})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
# / DELETE
    def test_delete_movie_success(self):
        res = self.client().delete('/movies/1', headers={
            "Authorization": 'bearer '+self.token_producer})
        data = json.loads(res.data)
        movie = Movie.query.filter_by(id=1).one_or_none()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(movie, None)

    def test_delete_nonexistant_movie(self):
        res = self.client().delete('/movies/666', headers={
            "Authorization": 'bearer '+self.token_producer})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)

    def test_delete_actor_bad_auth(self):
        res = self.client().delete('/movies/1', headers={
            "Authorization": 'bearer '+self.token_director})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

if __name__ == '__main__':
    unittest.main()
