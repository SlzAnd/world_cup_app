from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import settings


SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


























# import scraping

# #MongoDB driver
# import motor.motor_asyncio


# client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017/')
# database = client.CL
# collection = database.Matches


# async def take_last_results():
#     results = scraping.results()
#     await collection.insert_many(results)
#     print('OK')
    
# async def show_one_pair(team):
#     result = await collection.find_one({"Home Team": team})
#     return result