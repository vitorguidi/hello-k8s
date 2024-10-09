from fastapi import FastAPI
import os
import redis
import uvicorn


redis_host = os.getenv('REDIS_IP')
redis_port = os.getenv('REDIS_PORT')


class RedisDatabase:
    def __init__(self, host, port):
        self._redis = redis.Redis(host=host, port=port, decode_responses=True)

    def get_item(self, key: str) -> any:
        return self._redis.get(key)
    
    def put_item(self, key: str, val: any):
        self._redis.set(key, val)

db = RedisDatabase(host=redis_host, port=redis_port)
app = FastAPI()


@app.get("/items/{item_id}")
def get_item(item_id: str):
    return db.get_item(item_id)

@app.put("/items/{item_id}/{item_value}")
def get_item(item_id: str, item_value: int):
    db.put_item(item_id, item_value)
    return 'ok'

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)