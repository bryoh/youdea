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
echo ""
echo ""
echo ""
echo ""
echo ""
cd app
ls -alt
echo "============================================================== Create migrations based on django models"
echo ""
echo ""
echo ""
echo ""
echo ""
python manage.py makemigrations

echo "============================================================== Migrate created migrations to database"
echo ""
echo ""
echo ""
echo ""
echo ""
python manage.py migrate

echo "============================================================== Collect Static "
echo ""
echo ""
echo ""
echo ""
echo ""
#python manage.py collectstatic --no-input --clear


if [ "$DEBUG" = 'true' ]; then
    echo "============================================================== create superuser "
    echo ""
    echo ""
    echo ""
    echo ""
    echo ""
    echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('waka', 'admin@myproject.com', '1pass')" | python manage.py shell
fi

echo "============================================================== Start the server"
echo ""
echo ""
echo ""
echo ""
echo ""
gunicorn app.wsgi:application --timeout 300 --workers 3 --reload
#python manage.py runserver

exec "$@"
