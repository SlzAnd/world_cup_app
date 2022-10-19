from pydantic import BaseModel


class BaseTeam(BaseModel):
    points: int
    games: int
    wins: int
    draws: int
    loses: int
    different: int
    
    class Config:
        orm_mode = True
        

class GetResults(BaseModel):
    home_team_name: str
    away_team_name: str
    home_team_score: int
    away_team_score: int