### To run locally, without docker:

apt install redis

systemctl redis start

pipenv sync

REDIS_HOST=localhost REDIS_PORT=6379 pipenv run python3 main.py

### To run localy, with docker:

apt install redis

systemctl redis start

docker build . -t fastapi_demo_k8s
docker push fastapi_demo_k8s

docker run --network host -e REDIS_HOST=localhost -e REDIS_PORT=6379 fastapi_demo_k8s:latest

### To run on KIND:

TODO