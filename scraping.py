from bs4 import BeautifulSoup
import requests


# Last results
def results(url='https://www.skysports.com/world-cup-results'):
    wcup_results = requests.get(url)
    soup = BeautifulSoup(wcup_results.content, 'lxml')
    results = soup.find_all('div', class_="fixres__item")[:16]

    all_pairs = []

    for index,result in enumerate(results):
        side1 = result.find('span',
    class_="matches__item-col matches__participant matches__participant--side1").text.replace('\n','')
        side2 = result.find('span',
    class_="matches__item-col matches__participant matches__participant--side2").text.replace('\n','')
        
        score = result.find('span', class_="matches__teamscores").text.replace('\n','').replace(' ','')
        
        beauty_score = f'{score[0]} : {score[1]}'
        
        pair = {"Home Team":side1, "Score":beauty_score, "Away Team":side2}
            
        all_pairs.append(pair)
        
    return all_pairs
    
# World Cup Schedule
def schedule(url='https://www.skysports.com/world-cup-fixtures'):
    wcup_schedule = requests.get(url)
    soup = BeautifulSoup(wcup_schedule.content, 'lxml')
    results = soup.find_all('div', class_="fixres__item")

    all_matches = []

    for result in results:
        side1 = result.find('span',
    class_="matches__item-col matches__participant matches__participant--side1").text.replace('\n','')
        side2 = result.find('span',
    class_="matches__item-col matches__participant matches__participant--side2").text.replace('\n','')
        
        date = result.find('span', class_="matches__date").text.replace('\n','').replace(' ','')
        
        pair = [side1, date, side2]
            
        all_matches.append(pair)
