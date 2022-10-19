from calendar import day_abbr
from bs4 import BeautifulSoup
import requests
from dateutil.parser import *
from datetime import timedelta, datetime


# Last results
class Results():
    def __init__(self, day, month) -> None:
        if day >= 10:
            self.day = day
        else:
            self.day = f'0{day}'
        if month >= 10:
            self.month = month
        else:
            self.month = f'0{month}'
        self.all_pairs = []
        self.date = f'{self.day}.{self.month}.2022'
        
    def get_results(self):
        url=f'https://www.goal.com/en/uefa-champions-league/fixtures-results/2022-{self.month}-{self.day}/4oogyu6o156iphvdvphwpck10'
        print(url)
        wcup_results = requests.get(url)
        soup = BeautifulSoup(wcup_results.content, 'lxml')
        results = soup.find_all('div', class_="match-main-data")
        
        for result in results:
            status = result.find('div', class_="match-status")
            
            home_team_div = result.find('div', class_="team-home")
            home_team = home_team_div.find('span', class_="team-name").text
            home_team_score = home_team_div.find('span', class_="goals").text
            
            away_team_div = result.find('div', class_="team-away")
            away_team = away_team_div.find('span', class_="team-name").text
            away_team_score = away_team_div.find('span', class_="goals").text
            
            # if 'FT' in str(status):
            #     print("Match was ended")
            # else:
            #     match_time = parse(status.time['datetime'])+ timedelta(hours=3)
            #     print(match_time.time())
                
                                
            pair = {"home_team_name":home_team, "home_team_score":home_team_score, "away_team_score":away_team_score, "away_team_name":away_team}
            
            self.all_pairs.append(pair)
           
    
    
# World Cup Schedule
# def schedule(url='https://www.skysports.com/world-cup-fixtures'):
#     wcup_schedule = requests.get(url)
#     soup = BeautifulSoup(wcup_schedule.content, 'lxml')
#     results = soup.find_all('div', class_="fixres__item")

#     all_matches = []

#     for result in results:
#         side1 = result.find('span',
#     class_="matches__item-col matches__participant matches__participant--side1").text.replace('\n','')
#         side2 = result.find('span',
#     class_="matches__item-col matches__participant matches__participant--side2").text.replace('\n','')
        
#         date = result.find('span', class_="matches__date").text.replace('\n','').replace(' ','')
        
#         pair = [side1, date, side2]
            
#         all_matches.append(pair)
