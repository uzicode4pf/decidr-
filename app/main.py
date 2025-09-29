from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from app.routers import polls

app = FastAPI()

app.mount("/static",
          StaticFiles(directory="static"),
          name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/servertest")
def read_root():
    return {"message": "hello, Decidr is ready!"}

app.include_router(polls.router)