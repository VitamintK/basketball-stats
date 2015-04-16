"""find all players from that play this year"""
import os
import json

this_year = []
for player in os.listdir('json'):
    with open('json/'+player) as playerfile:
        playerdict = json.load(playerfile)
        averages = playerdict['per_game']
        career = 0
        for i, header in enumerate(reversed(averages)):
            if header[0] == "Career":
                career = i
                break
        else:
            print("career not found for {}".format(player))
        if averages[-1*i-2][0] == '2014-15':
            this_year.append(player)
        #print(averages[-1*i-2][0])
print(this_year)
        


