#!/bin/sh

#if [ "$DATABASE" = "postgres" ]
#then
    #echo "Waiting for postgres..."

    #while ! nc -z $SQL_HOST $SQL_PORT; do
      #sleep 0.1
    #done

    #echo "PostgreSQL started"
#fi
echo "============================================================== cd into app"
cd app
ls -alt
echo "============================================================== Create migrations based on django models"
python manage.py makemigrations

echo "============================================================== Migrate created migrations to database"
python manage.py migrate

#echo "============================================================== Collect Static "
#python manage.py collectstatic --no-input --clear


echo "============================================================== Start the server"
if [ "$DEBUG" = 'true' ]; then
    echo "============================================================== create superuser "
    echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('bry', 'admin@myproject.com', 'pass')" | python manage.py shell
fi
gunicorn --reload app.wsgi
#python manage.py runserver

exec "$@"
