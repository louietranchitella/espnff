#!/usr/bin/env python3

import json
import numpy as np
import xlsxwriter

TwentyFiveWinsTest = 0

class Game():
    """ object to host all info about a specific fantasy game """

    def __init__(self, home_id, away_id, home_score, away_score, week, year):
        self.home_id = home_id
        self.away_id = away_id
        self.home_score = int(home_score)
        self.away_score = int(away_score)
        self.week = week
        self.year = year

    def team_and_owner_names(self):
        names = generateTeams(self.home_id, self.away_id, self.year)
        self.home_team_name = names[0]
        self.home_owner_name = names[1]
        self.away_team_name = names[2]
        self.away_owner_name = names[3]

    def display_game(self):
        print("{0}\t\t{1}".format(self.home_team_name, self.away_team_name))
        print("{0}\t\t{1}".format(self.home_owner_name, self.away_owner_name))
        print("{0}\t\t{1}".format(self.home_id, self.away_id))
        print("{0}\t\t{1}".format(self.home_score, self.away_score))
        print("Week {0} of {1}".format(self.week, self.year))

    def scores(self):
        return self.home_score, self.away_score

    def date(self):
        return self.week, self.year

def generateGames(start_year, end_year):
    for year in range(start_year, end_year+1, 1):
        teams = boxscoreData[str(year)]["status"]["teamsJoined"]
        weeks = boxscoreData[str(year)]["scoringPeriodId"]
        games = round(teams / 2) * weeks
        for game in range(0, games+1, 1):
            try:
                home_id = boxscoreData[str(year)]["schedule"][game]["home"]["teamId"]
                away_id = boxscoreData[str(year)]["schedule"][game]["away"]["teamId"]
                home_score = boxscoreData[str(year)]["schedule"][game]["home"]["totalPoints"]
                away_score = boxscoreData[str(year)]["schedule"][game]["away"]["totalPoints"]
                week = boxscoreData[str(year)]["schedule"][game]["matchupPeriodId"]
                if TwentyFiveWinsTest == 1:
                    if home_id == 4:
                        if home_score > away_score:
                            print("win")
                            recordedGames.append(Game(home_id, away_id, home_score, away_score, week, year))
                    elif away_id == 4:
                        if home_score < away_score:
                            print("win")
                            recordedGames.append(Game(home_id, away_id, home_score, away_score, week, year))
                else:
                    recordedGames.append(Game(home_id, away_id, home_score, away_score, week, year))

            except IndexError:
                continue
            except KeyError: 
                """ bye weeks or teams out of playoffs dont have an away team """
                continue

def generateTeams(home_id, away_id, year):
    """ grab team name from id """
    for team in boxscoreData[str(year)]["teams"]:
        if team["id"] == home_id:
            home_team_name = team["name"]
        if team["id"] == away_id:
            away_team_name = team["name"]

    """ grab owner tag from id """
    for team in teamData[str(year)]["teams"]:
        if team["id"] == home_id:
            home_owner_tag = team["primaryOwner"]
        if team["id"] == away_id:
            away_owner_tag = team["primaryOwner"]

    """ grab owner name from tag """
    for team in teamData[str(year)]["members"]:
        if team["id"] == home_owner_tag:
            home_owner_name = "{0} {1}".format(team["firstName"], team["lastName"])
        if team["id"] == away_owner_tag:
            away_owner_name = "{0} {1}".format(team["firstName"], team["lastName"])
    return home_team_name, home_owner_name, away_team_name, away_owner_name

f = open("mBoxscore.json")
boxscoreData = json.load(f)
f.close()

f = open("mTeam.json")
teamData = json.load(f)
f.close()

recordedGames = []
scorigami = np.zeros((300,300))

generateGames(2018, 2022)

for game in recordedGames:
    game.team_and_owner_names()
    game.display_game()
    x = max(game.scores())
    y = min(game.scores())
    scorigami[x][y] += 1

workbook = xlsxwriter.Workbook("scorigami.xlsx")
worksheet = workbook.add_worksheet()

row = 0

for col, data in enumerate(scorigami):
    worksheet.write_column(row, col, data)

workbook.close()
