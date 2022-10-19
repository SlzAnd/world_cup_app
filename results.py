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

def results_to_db(db:Session=SessionLocal()):
    lastresults = Results(day=14, month=9)
    lastresults.get_results()

    for result in lastresults.all_pairs:
        if (db.query(models.Result).filter(models.Result.home_team_name == result['home_team_name']).first() and 
        db.query(models.Result).filter(models.Result.away_team_name == result['away_team_name']).first()):
            print('results already here')
        else:
            update_results(result,SessionLocal(),date=lastresults.date)
