from bs4 import BeautifulSoup
import requests
from dateutil.parser import *
from datetime import timedelta, datetime



res = requests.get('https://www.goal.com/en/uefa-champions-league/fixtures-results/2022-10-25/4oogyu6o156iphvdvphwpck10')
soup = BeautifulSoup(res.content, 'lxml')
results = soup.find_all('div', class_="match-main-data")

for result in results:
    status = result.find('div', class_="match-status")
    home_team_div = result.find('div', class_="team-home")
    home_team = home_team_div.find('span', class_="team-name").text
    home_team_score = home_team_div.find('span', class_="goals").text
    
    away_team_div = result.find('div', class_="team-away")
    away_team = away_team_div.find('span', class_="team-name").text
    away_team_score = away_team_div.find('span', class_="goals").text
    print(home_team, home_team_score,':', away_team_score, away_team)
    if 'FT' in str(status):
        print("Match was ended")
    else:
        match_time = parse(status.time['datetime'])+ timedelta(hours=3)
        print(match_time.time())