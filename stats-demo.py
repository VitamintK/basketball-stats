import json
import os

team_a = ['Michael Jordan', 'Tyreke Evans', 'Kevin Garnett', 'Kevin Durant', 'Kareem Abdul-Jabbar', 'John Stockton', 'Anthony Davis', 'Larry Bird']
team_b = ['Lebron James', 'Michael Carter-Williams', 'Damian Lillard', "Shaquille O'Neal", 'Hakeem Olajuwon', "Ricky Rubio", "Yao Ming", "Karl Malone"]
#team_a = ["Chris Bosh"]

HEADERS = ["Season", "Age", "Tm", "Lg", "Pos", "G", "GS", "MP", "FG", "FGA", "FG%", "3P", "3PA", "3P%", "2P", "2PA", "2P%", "eFG%", "FT", "FTA", "FT%", "ORB", "DRB", "TRB", "AST", "STL", "BLK", "TOV", "PF", "PTS"]

class Player:
    def __init__(self, player):
        self.name = player
        self._load_from_json()
    def _load_from_json(self):
        try:
            with open('json/{}.json'.format(self.name)) as pjson:
                pdic = json.load(pjson)
                self.totals = pdic["totals"]
        except FileNotFoundError:
                print("player {} not found".format(self.name))
                
    def _rookie(self):
        if self.totals[2][0] == self.totals[1][0]:
            return [sum(i) for i in zip(self.totals[1], self.totals[2])]
        else:
            return self.totals[1]
                

def make_float(string):
    try:
        return float(string)
    except:
        return 0

class Team:
    def __init__(self, team):
        self.team = [Player(player) for player in team]
        self.rookie = self.rookies()
    def rookies(self):
        rookie_team = []
        for player in self.team:
            try:
                rookie_totals = player._rookie()
            except:
                rookie_totals = [0]*30
            assert len(rookie_totals) == 30
            rookie_team.append(rookie_totals[5:])
        return list(sum([make_float(j) for j in i]) for i in zip(*rookie_team))

def winner(av, kev):
    try:
        if av>kev:
            return "Avi"
        else:
            return "Kevin"
    except:
        return None
kevin = Team(team_b)
avi = Team(team_a)
cats = {'FGP', 'FTP', 'PTS', '3P', 'TRB', 'AST', 'STL', 'BLK', 'TOV'}
print("AVI vs KEVIN")
for i,j,k in zip(HEADERS, [None, None, None, None, None] + avi.rookie, [None, None, None, None, None] + kevin.rookie):
    print('{}: {} vs {}.  WINNER IS: {}'.format(i, j, k, winner(j,k)))
"""  
for cat in cats:
    if cat == 'FGP':
        amt = lambda stats: stats[
    elif cat == 'FTP':

    elif cat == 'TO':

    else:"""
print("	".join(HEADERS))
for player in kevin.team:
    print("	".join([player.name] + player._rookie()))
for player in avi.team:
    print("	".join([player.name] + player._rookie()))
