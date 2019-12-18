# Use an official Python runtime as a parent image
FROM python:3.7
LABEL maintainer="brianbryo@gmail.com"

# Set environment varibles
ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENV dev

COPY ./requirements.txt /code/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /code/requirements.txt

COPY ./app /code/
WORKDIR /code/

EXPOSE 8000
CMD exec gunicorn app.wsgi:application --bind 0.0.0.0:8000 --workers 3
