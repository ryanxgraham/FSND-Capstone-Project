import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json
from flask_migrate import Migrate, MigrateCommand

# database_name = 'capstone'
# database_path = 'postgres://postgres@localhost:5432/capstone'
database_path = os.environ['DATABASE_URL']
db = SQLAlchemy()


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    create_all()
    db_init_records()
    migrate = Migrate(app, db)

def db_init_records():
    new_actor1 = Actor(
                        name='John Doe',
                        gender='Male',
                        age='32'
                        )
    new_actor2 = Actor(
                        name='Jane Doe',
                        gender='Female',
                        age='32'
                        )
    new_actor3 = Actor(
                        name='Joe Shmoe',
                        gender='Male',
                        age='50'
                        )
    new_movie1 = Movie(
                        title='Two people have an argument',
                        release_date='5/1/2020',
                        genre='Drama'
                        )
    new_movie2 = Movie(
                        title='Two people fall in love',
                        release_date='5/1/2020',
                        genre='Romance'
                        )
    new_movie3 = Movie(
                        title='A guy kills two people',
                        release_date='5/1/2020',
                        genre='Horror'
                        )
    new_actor1.insert()
    new_actor2.insert()
    new_actor3.insert()
    new_movie1.actors.append(new_actor1)
    new_movie1.actors.append(new_actor2)
    new_movie2.actors.append(new_actor1)
    new_movie2.actors.append(new_actor2)
    new_movie3.actors.append(new_actor1)
    new_movie3.actors.append(new_actor2)
    new_movie3.actors.append(new_actor3)
    new_movie1.insert()
    new_movie2.insert()
    new_movie3.insert()

cast = db.Table('cast',
                db.Column(
                    'movie_id',
                    db.Integer,
                    db.ForeignKey('Movies.id'),
                    primary_key=True),
                db.Column(
                    'actor_id',
                    db.Integer,
                    db.ForeignKey('Actors.id'),
                    primary_key=True))

class Movie(db.Model):
    __tablename__ = 'Movies'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    release_date = Column(String)
    genre = Column(String)
    actors = db.relationship(
        'Actor',
        secondary=cast,
        backref=db.backref('Movies', lazy=True))

    def __init__(self, title, release_date, genre):
        self.title = title
        self.release_date = release_date
        self.genre = genre

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date,
            'genre': self.genre,
            'actors': [i.name for i in self.actors]
        }

    def short(self):
        return {
            'title': self.title
        }


class Actor(db.Model):
    __tablename__ = 'Actors'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    # movies = db.relationship(
    #   'Movie',
    #   secondary=cast,
    #   backref=db.backref('Actors', lazy=True))

    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'gender': self.gender,
            'age': self.age,
            'movies': [i.title for i in self.movies]
        }

    def short(self):
        return {
            'name': self.name
        }
