from sqlalchemy import TIMESTAMP, Column, Integer, String, Boolean, text, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Team(Base):
    __tablename__ = 'teams'
    
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    group = Column(String, nullable=False)
    points = Column(Integer, default = 0)
    games = Column(Integer, default = 0)
    wins = Column(Integer, default = 0)
    draws = Column(Integer, default = 0)
    loses = Column(Integer, default = 0)
    different = Column(Integer, default = 0)
    

class Result(Base):
    __tablename__ = 'results'
    
    id = Column(Integer, primary_key=True, nullable=False)
    home_team_name = Column(String, nullable=False)
    away_team_name = Column(String, nullable=False)
    home_team_score = Column(Integer)
    away_team_score = Column(Integer)
    date = Column(TIMESTAMP)