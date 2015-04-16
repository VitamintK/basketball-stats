"""find all hall of famers"""
hofers = []
with open("HOF.csv") as HOF:
    for line in HOF:
        l = line.split(',')
        lindex= l[1].find('Player')
        if lindex > -1:
            hofers.append(l[1][:lindex])

#print(hofers)

"""find all players from 2005 and onwards who played 30+ minutes"""
import os
import json
from datetime import date

notable_recents = []

current_year = date.today().year
for player in os.listdir('json'):
    with open('json/'+player) as playerfile:
        playerdict = json.load(playerfile)
        averages = playerdict['per_game']
        for row in averages:
            try:
                year = int(row[0][:4])
                mp = float(row[7])
                if mp >= 2*(current_year - year) + 20:
                    #print(player[:-5])
                    notable_recents.append(player[:-5])
                    break
            except:
                pass
#print(notable_recents)

"""copy all notable players to their own folder."""
import shutil
all_notable = hofers + notable_recents
all_notable = set(all_notable)

for player in all_notable:
    try:
        shutil.copyfile('json/{}.json'.format(player), 'notable/{}.json'.format(player))
    except:
        print("{} not found :(".format(player))
