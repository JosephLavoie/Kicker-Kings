import Scrape.KickerClass as c
import requests
from bs4 import BeautifulSoup

def kickerList():

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
               AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    

    response = requests.get("https://www.espn.com/nfl/players/_/position/k", headers=headers)
    players_soup = BeautifulSoup(response.content, "html.parser")

    kickers = []

    for player_row in players_soup.find_all("tr", class_=lambda x: x and "player-" in x):

        columns = player_row.find_all("td")

        profile = columns[0].a["href"]
        athleteid = profile[37:].split('/')[0]
        team = columns[1].a.text
        
        name = (columns[0].a.text).replace(',', '')
        name_list = name.split()
        name_list.reverse()
        name = " ".join(name_list)

        kickers.append(c.Kicker(name, team, athleteid, profile, "NFL"))
    
    return kickers

def KickerInfo(kicker:c.Kicker):
    
    return kicker
