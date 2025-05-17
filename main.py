from fastapi import FastAPI
import time

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "자동매매 서버 정상 작동 중 😎"}

@app.get("/time")
def get_time():
    return {"timestamp": int(time.time() * 1000)}
