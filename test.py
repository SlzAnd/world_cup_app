from bs4 import BeautifulSoup
import requests


res = requests.get('https://www.skysports.com/football/qatar-vs-ecuador/462959')
soup = BeautifulSoup(res.content, 'lxml')
results = soup.find_all('span', class_="sdc-site-match-header__team-score-block")
for result in results:
    print(result.text)