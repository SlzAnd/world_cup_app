from sqlalchemy.orm import Session
from fastapi import Depends
from scraping import Results
from database import get_db, SessionLocal, engine
import models, schemas

models.Base.metadata.create_all(bind=engine)

def update_results(result, db:Session, date):
    db_result = models.Result(date=date,**result)
    db.add(db_result)
    db.commit()
    db.refresh(db_result)

lastresults = Results(day=11, month=10)
lastresults.get_results()
print(lastresults.date)



for result in lastresults.all_pairs:
    update_results(result,SessionLocal(),date=lastresults.date)
