from fastapi import FastAPI
from app.routers import polls

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "hello, Decidr is ready!"}

app.include_router(polls.router)