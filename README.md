
    docker build -t pry-flask-vue .
    docker images
    docker run --rm -p 5000:5000 pry-flask-vue