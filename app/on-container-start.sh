#!/bin/sh

#if [ "$DATABASE" = "postgres" ]
#then
    #echo "Waiting for postgres..."

    #while ! nc -z $SQL_HOST $SQL_PORT; do
      #sleep 0.1
    #done

    #echo "PostgreSQL started"
#fi
# Create migrations based on django models

echo "==============================================================="
cd app
python manage.py makemigrations

# Migrate created migrations to database
python manage.py migrate

# Start gunicorn server at port 8000 and keep an eye for app code changes
# If changes occur, kill worker and start a new one

#python manage.py flush --no-input
#python manage.py migrate
#python manage.py collectstatic --no-input --clear

#python manage.py runserver

echo "==============================================================="
gunicorn --reload app.wsgi 
#useradd wagtail
#chown -R wagtail /code

exec "$@"
