from fastapi import FastAPI, HTTPException
from fastapi import Response, status, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from database import get_db
from sqlalchemy.orm import Session

from . import schemas


app = FastAPI()

origins = ['http://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# @app.get("/")
# async def read_root():
#     pair = await show_one_pair('Peru')
#     print(pair)
#     return f'{pair["Home Team"]} |{pair["Score"]}| {pair["Away Team"]}'

# @app.get("/update/{group}/{team_id}", response_model=schemas.BaseTeam)
# async def update_result(team_id:int, db: Session = Depends(get_db)):
#     await take_last_results()
#     return {"Check your database!"}



    