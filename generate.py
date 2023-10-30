#!/usr/bin/env python3

import json

class Game():
    """ object to host all info about a specific fantasy game """

    def __init__(self, home_id, away_id, home_score, away_score, week, year):
        self.home_id = home_id
        self.away_id = away_id
        self.home_score = home_score
        self.away_score = away_score
        self.week = week
        self.year = year

    def team_and_owner_names(self):
        self.home_team_name = "Stroud Boys"
        self.home_owner_name = "Pat Blesco"
        self.away_team_name = "Tuanon"
        self.away_owner_name = "Sophie Bono"

    def display_game(self):
        print("{0}\t\t{1}".format(self.home_team_name, self.away_team_name))
        print("{0}\t\t{1}".format(self.home_owner_name, self.away_owner_name))
        print("{0}\t\t{1}".format(self.home_id, self.away_id))
        print("{0}\t\t{1}".format(self.home_score, self.away_score))
        print("Week {0} of {1}".format(week, year))

f = open("mBoxscore.txt")
data = json.load(f)
Schedule = {}
Schedule[2018] = data["2018"]["schedule"]

games = []

for year in range(2018, 2019, 1):
    for game in range(0, 5, 1):
        home_id = Schedule[year][game]["home"]["teamId"]
        away_id = Schedule[year][game]["away"]["teamId"]
        home_score = Schedule[year][game]["home"]["totalPoints"]
        away_score = Schedule[year][game]["away"]["totalPoints"]
        week = Schedule[year][game]["matchupPeriodId"]
        games.append(Game(home_id, away_id, home_score, away_score, week, year))

games[0].team_and_owner_names()
games[0].display_game()
