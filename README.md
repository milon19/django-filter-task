# Djando Advance Filtering

## Setup

It is best to use the python `virtualenv` tool to build locally:

- Clone the repository
```shell script
$ git clone https://github.com/milon19/django-filter-task
$ cd django-filter-task
```

- Create Virtual environment and Install dependencies
```diff
$ virtualenv env
$ source ./env/bin/activate
$ pip install -r requirements.txt
```

- Make `.env` file to the root directory of the project. `.env` file should contains following variables.
```
SECRET_KEY=
ALLOWED_HOSTS=
DEBUG=
SQLITE_URL=
DATABASE_URL=
```
```
note: As Database I use PostgreSQL in this project.
So in '.env' file DATABASE_URL should be postgres://<user_name>:<password>@<hostname>:5432/<database_name>.
```

## Run
```shell script
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```
Then visit [http://localhost:8000](http://localhost:8000) to view the app.

## Deploy to Heroku

This application is currently deployed in Heroku. 

To Visit follow this link: [Heroku App URL.](https://django-filtering.herokuapp.com/)