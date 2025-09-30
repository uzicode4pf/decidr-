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

@app.get("/create", response_class=HTMLResponse)
async def create(request: Request):
    return templates.TemplateResponse("create.html", {"request": request})

@app.get("/results", response_class=HTMLResponse)
async def results(request: Request):
    return templates.TemplateResponse("results.html", {"request": request})

@app.get("/vote", response_class=HTMLResponse)
async def vote(request: Request):
    return templates.TemplateResponse("vote.html", {"request": request})


@app.get("/servertest")
def read_root():
    return {"message": "hello, Decidr is ready!"}

app.include_router(polls.router)