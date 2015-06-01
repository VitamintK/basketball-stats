"""find all players from that play this year"""
import os
import json
from datetime import date

def get_players(predicate):
    players = []
    for player in os.listdir('notable'):
        with open('json/'+player) as playerfile:
            playerdict = json.load(playerfile)
            
            if predicate(playerdict, player):
                players.append(player)
    return players

current_year = date.today().year - 1
current_season = str(current_year) + '-' + str(current_year%1000 + 1)
def played_this_year(playerdict, player=''):
    averages = playerdict['per_game']
    career = 0
    for i, header in enumerate(reversed(averages)):
        if header[0] == "Career":
            career = i
            break
    else:
        print("career not found for {}".format(player))
    return averages[-1*i-2][0] == '2014-15'

maybes = []
def user_select(playerdict, player=''):
    inp = input("{}: ".format(player[:-5]))
    if inp == 'm':
        maybes.append(player)
    return inp == 'y'

p = get_players(user_select)
print(p)
print(maybes)
