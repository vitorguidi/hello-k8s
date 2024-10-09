FROM python:3.11

WORKDIR /app

COPY . /app

RUN apt update && apt install -y pipenv
RUN pipenv sync

ENTRYPOINT ["pipenv", "run", "python", "main.py"]
