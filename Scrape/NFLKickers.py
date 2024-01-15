import Classes.KickerClass as c
import requests
from bs4 import BeautifulSoup

def UrlToResponce(url:str):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
               AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response
    else:
        print("Error:", response.status_code)
        return None
    
def kickerList():

    data = UrlToResponce("https://www.espn.com/nfl/players/_/position/k")

    players_soup = BeautifulSoup(data.content, "html.parser")

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
    url = "https://site.web.api.espn.com/apis/common/v3/sports/football/nfl/athletes/" + kicker.athleteid + "/overview"

    data = UrlToResponce(url).json()


    # Extract the values
    for split in data["statistics"]["splits"]:
        if split["displayName"] == "Career":
            # field_goal_percent_career = float(split["stats"][0])
            field_goal_career = (split["stats"][1]).split('-')
        elif split["displayName"] == "Regular Season":
            # field_goal_percent_season = float(split["stats"][0])
            field_goal_season = (split["stats"][1]).split('-')
        

    #field_goal_percent_season = float(data["statistics"]["splits"][0]["stats"][0])
    #field_goal_season = (data["statistics"]["splits"][0]["stats"][1]).split('-')
    field_goal_made_season = int(field_goal_season[0])
    field_goal_attempt_season = int(field_goal_season[1])
    field_goal_percent_season = (field_goal_made_season/field_goal_attempt_season) *100

    #field_goal_percent_career = float(data["statistics"]["splits"][3]["stats"][0])
    #field_goal_career = (data["statistics"]["splits"][3]["stats"][1]).split('-')
    field_goal_made_career = int(field_goal_career[0])
    field_goal_attempt_career = int(field_goal_career[1])
    field_goal_percent_career = (field_goal_made_career/field_goal_attempt_career) *100

    url = "https://www.espn.com/nfl/player/gamelog/_/id/" + kicker.athleteid

    data = UrlToResponce(url)

    soup = BeautifulSoup(data.text, 'html.parser')
    target_row = soup.find('tr', {'class': 'Table__TR Table__TR--sm Table__even', 'data-idx': '0'})
    field_goal_last_game = (target_row.find_all('td')[10].text.strip()).split('-')
    field_goal_made_last_game = int(field_goal_last_game[0])
    field_goal_attempt_last_game = int(field_goal_last_game[1])

    url = "https://www.espn.com/nfl/player/stats/_/id/" + kicker.athleteid

    data = UrlToResponce(url)

    soup = BeautifulSoup(data.text, 'html.parser')

    table = soup.find('table', class_='Table Table--align-right')
    rows = table.find('tbody', class_='Table__TBODY').find_all('tr')

    games_career = 0
    for i in rows[:-1]:
        games_career += int(i.find_all('td')[0].text)
    # If ESPN fixes their website, this will get games_career instead:
    #games_career = int(rows[-1].find_all('td')[0].text)
    games_season = int(rows[-2].find_all('td')[0].text)


    kicker.field_goal_percent_season = field_goal_percent_season
    kicker.field_goal_percent_career = field_goal_percent_career
    kicker.field_goal_made_last_game = field_goal_made_last_game
    kicker.field_goal_attempt_last_game = field_goal_attempt_last_game
    kicker.field_goal_made_average_season = field_goal_made_season / games_season
    kicker.field_goal_made_average_career = field_goal_made_career / games_career
    kicker.field_goal_attempt_average_season = field_goal_attempt_season / games_season
    kicker.field_goal_attempt_average_career = field_goal_attempt_career / games_career

    print("v-v-v--------Removable-------v-v-v")

    print(kicker.field_goal_percent_season)
    print(kicker.field_goal_percent_career)
    print(kicker.field_goal_made_last_game)
    print(kicker.field_goal_attempt_last_game)
    print(kicker.field_goal_made_average_season)
    print(kicker.field_goal_made_average_career)
    print(kicker.field_goal_attempt_average_season)
    print(kicker.field_goal_attempt_average_career)

    print("-------------Removable-------------")


    return kicker
