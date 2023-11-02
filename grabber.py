#!/usr/bin/env python3

import json
import requests
from datetime import date

league_id = 1570607
start_year = 2018
last_year = date.today().year
cookies={"swid": "{8095DE7B-520D-4619-BE38-33293C2BD1B4}",
         "espn_s2": "AEBiCbsmWjb1zWWG0%2B1DDj%2FxqAlV2eHcnYlKPJUA9f0WkcN9qmtyFeubqJDGH0EajqFWWjtUp5AWWtnBRhheukByJGEW0eJUfdHzlMMnNjplc7rXnXngO2DrT0P6r5sxJHOUmpvKz9wmbXDTBSWZkAHxZPtA1skkQMFGOqdxVt7GOkdV0xNj%2B5sdeeCQrKVS4sElWaIbhE13Piyqj%2FY5P7kguXN2QaOn6m5cdRytl97JJPdyelUXTEcWy7RHUeFJlhde%2Fx1ilfGJMT86WAKJIO6ef6paM72R7jYRyLA3uye0twXPm5qae2zjh3z18b6juvg%3D"}
boxscoreParams={"view": "mBoxscore"}
teamParams={"view": "mTeam"}

if (date.today().month < 9):
    last_year -= 1

data = dict()

for year in range(start_year, last_year, 1):
    url = url = "https://fantasy.espn.com/apis/v3/games/ffl/leagueHistory/" + str(league_id) + "?seasonId=" + str(year)

    r = requests.get(url, cookies=cookies)

    json_data = r.json()[0]

    json_formatted_str = json.dumps(json_data, indent=2)

    data[str(json_data["seasonId"])] = json_data

with open("default.json", "w") as outfile:
    outfile.write(json.dumps(data))

for year in range(start_year, last_year, 1):
    url = url = "https://fantasy.espn.com/apis/v3/games/ffl/leagueHistory/" + str(league_id) + "?seasonId=" + str(year)

    r = requests.get(url, cookies=cookies, params=boxscoreParams)

    json_data = r.json()[0]

    json_formatted_str = json.dumps(json_data, indent=2)

    data[str(json_data["seasonId"])] = json_data

with open("mBoxscore.json", "w") as outfile:
    outfile.write(json.dumps(data))

for year in range(start_year, last_year, 1):
    url = url = "https://fantasy.espn.com/apis/v3/games/ffl/leagueHistory/" + str(league_id) + "?seasonId=" + str(year)

    r = requests.get(url, cookies=cookies, params=teamParams)

    json_data = r.json()[0]

    json_formatted_str = json.dumps(json_data, indent=2)

    data[str(json_data["seasonId"])] = json_data

with open("mTeam.json", "w") as outfile:
    outfile.write(json.dumps(data))
