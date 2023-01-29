

Project using `python`, `vue`, `nginx`, `docker-compose`
## v1
    docker build -t pry-flask-vue .
    docker images
    docker run --rm -p 5000:5000 pry-flask-vue

## v2

    # without images created `--build`
    docker-compose up --build
    docker-compose stop
    docker-compose start
