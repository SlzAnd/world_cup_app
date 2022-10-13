from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from database import take_last_results, show_one_pair

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
async def read_root():
    pair = await show_one_pair('Peru')
    print(pair)
    return f'{pair["Home Team"]} |{pair["Score"]}| {pair["Away Team"]}'

@app.get("/results/update")
async def read_root():
    await take_last_results()
    return {"Check your database!"}



    