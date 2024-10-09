### To run locally, without docker:

apt install redis

systemctl redis start

pipenv sync

REDIS_HOST=localhost REDIS_PORT=6379 pipenv run python3 main.py

### To run localy, with docker:

apt install redis

systemctl redis start

docker build . -t fastapi_demo_k8s

docker run --network host -e REDIS_HOST=localhost -e REDIS_PORT=6379 fastapi_demo_k8s:latest

### To run on KIND:


Install [KIND](https://kind.sigs.k8s.io/docs/user/quick-start/)

Install [kubectl](https://kubernetes.io/docs/tasks/tools/)

kind create cluster --config=./infra/kind-cluster.yaml

kubectl apply ./infra/*

kubectl port-forward service/inventory-service 8000:8000

curl localhost:8000/items/2/3 -X PUT

curl localhost:8000/items/2