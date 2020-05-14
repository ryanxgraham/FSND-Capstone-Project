# Casting-Agency-API

This API models a company that creates, manages, and assigning actors movies.

No frontend is present for this api, it can be accessed using cURL or [Postman](https://www.postman.com)

## Getting Started

### Prerequesites
Ensure that Python 3 and git are installed:
```
python --version
git --version
```
### Installing

From the Terminal, clone this repo onto your computer with:

```
https://github.com/ryanxgraham/FSND-Capstone-Project/
```

Move into the new directory:

```
cd FSND-Capstone-Project/
```
#### Dependencies
Install dependencies with:

```
pip install -r requirements.txt
```

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we use to handle cross origin requests from the frontend server.

## Running the server

First ensure that you are working in the FSND-Capstone-Project directory.

To run the server, use:

```
source setup.sh
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```
`setup.sh` sets environment variables used by the app.

Setting `FLASK_ENV` to `development` will detect changes and restart the server automatically.

Setting `FLASK_APP` to `app.py` directs flask to use the this file to find the application.

You can run this API locally at `http://127.0.0.1:5000/`

## Testing

To run the tests, run
```
dropdb capstonetest
createdb capstonetest
psql capstonetest < capstone.db
python test_app.py
```

## Deployment

The app is deployed on Heroku [link](https://fsnd-capstone-project-rgraham.herokuapp.com/).

## API Reference

### Getting Started

- Base URL: [link](https://fsnd-capstone-project-rgraham.herokuapp.com/)

- Authentication: This app has 3 authorization levels. Each has it's own token, located in `setup.sh`. User privileges detailed below.

### Endpoints

- GET '/actors'
- GET '/movies'
- POST '/actors'
- POST '/movies'
- PATCH '/actors/<int:id>'
- PATCH '/movies/<int:id>'
- DELETE '/actors/<int:id>'
- DELETE '/movies/<int:id>'

Example responses of the requests:

- GET '/actors'
	- Get Actor from database
	- Request Argument : None
	- Returns : JSON response containing all actors with their formatted info, and request status
		```
		{
            "actors": [
          {
              "age": 50,
              "gender": "Male",
              "id": 3,
              "name": "Patch"
          },
          {
              "age": 32,
              "gender": "Male",
              "id": 4,
              "name": "John Doe"
          },
          {
              "age": 32,
              "gender": "Female",
              "id": 5,
              "name": "Jane Doe"
          }
		  ],
		  "success": true
		}
		```

- GET '/movies'
	- Get Movie from database
	- Returns : JSON response containing all movies with their formatted info, and request status
		```
		{
            "movies": [
            {
              "actors": [],
              "genre": "Drama",
              "id": 1,
              "release_date": "5/1/2020",
              "title": "Two people have an argument"
            },
            {
              "actors": [
                  "Patch"
              ],
              "genre": "Horror",
              "id": 3,
              "release_date": "5/1/2020",
              "title": "A guy kills two people"
            },
            {
              "actors": [
                  "John Doe",
                  "Jane Doe"
              ],
              "genre": "Drama",
              "id": 4,
              "release_date": "5/1/2020",
              "title": "Two people have an argument"
            }
            ],
            "success": true
        }
		```

- POST '/actors'
	- Insert Actor into database
	- Request Argument :  `name` `gender` `age`
	- Returns : JSON response containing created actor name, id, and request status
		```
        {
            "actor_created": "name",
            "created": 10,
            "success": true
        }
		```

- POST '/movies'
	- Insert Movie into database
	- Request Argument : `name` `release_date` `genre`
	- Returns : JSON response containing created movie title, id, and request status
		```
        {
            "created": 15,
            "movie_created": "title",
            "success": true
        }       
		```

- PATCH '/actors/<int:id>'
	- Update Actor info and insert into database
	- Request Argument : `Actor id`  `name` `gender` `age`
	- Returns : JSON response containing request status
		```
		{
		  "success": true
		}
		```

- PATCH '/movies/<int:id>'
	- Update Movie info and insert into database
	- Request Argument : `Movie id` `name` `length` `genre`
	- Returns : JSON response containing request status
		```
		{
		  "success": true
		}
		```

- DELETE '/actors/<int:id>'
	- Delete Actor from database
	- Request Argument : Actor id
	- Returns : JSON response containing the ID of deleted actor and request status
		```
		{
          "delete": 11,
		  "success": true
		}
		```

- DELETE '/movies/<int:id>'
	- Delete Movie from database
	- Request Argument : Movie id
	- Returns : JSON response containing ID of deleted movie and request status
		```
		{
          "delete": 5,
		  "success": true
		}
		```

### Users

The app has 3 Authorization Levels:

- Casting Assistant
	- Can GET actors and movies

- Casting Director
	- All permissions of a Casting Assistant
	- Can POST/DELETE actors
	- Can PATCH actors and movies

- Executive Producer
	- All permissions of a Casting Director
	- can POST/DELETE movies

## Built With

* Python 3
* git 2.14.1

## Authors

* **Ryan Graham** - [Github](https://github.com/ryanxgraham)

## Acknowledgments

* Thanks to Udacity for the guidance!
