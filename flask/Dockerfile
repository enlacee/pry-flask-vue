# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster
ENV TZ="America/Lima"
# FROM python:3.8-alpine
RUN mkdir /app
WORKDIR /app
# Available to mount the volumen on container
VOLUME /app
EXPOSE 5000
ENV FLASK_ENV=development
# ADD . /app
# COPY . .
COPY requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt
# CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "-p 5000"]
