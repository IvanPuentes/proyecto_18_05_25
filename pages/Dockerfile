#version de pyton
FROM python:3.9

ENV PYTHONNDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#LA CARPETA DONDE TRABAJAMOS 
WORKDIR /code

COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv && pipenv install --system

COPY . /code/