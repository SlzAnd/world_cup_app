from fastapi import FastAPI, HTTPException, Request
from fastapi import Response, status, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from database import get_db
from sqlalchemy.orm import Session
from results import results_to_db


templates = Jinja2Templates(directory='templates')

app = FastAPI()

origins = ['http://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root(request:Request):
    return templates.TemplateResponse('index.html', {"request":request})

@app.get("/update")
def update_result():
    results_to_db()
    return {"Check your database!"}



    