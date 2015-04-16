import json
from collections import defaultdict
json_file = 'scheduleresults/2014-2015.json'

class Season():
    def __init__(self):
        self.season = defaultdict(list)
    def add_match(self, team1, team2, team1score, team2score):
        try:
            winner = (team1, team2)[int(team1score) > int(team2score)]
        except:
            winner = None
        teams = (team1, team2)
        self.season[frozenset(teams)].append(winner)
    def get_records(self, team):
        pass
    def get_record(self, team1, team2):
        x = self.season[frozenset((team1, team2))]
        return x.count(team1), x.count(team2)
    def get_winner(self, team1, team2):
        records = self.get_record(team1, team2)
        if records[1] == records[0]:
            return None
        return (team1, team2)[records[1] > records[0]]    

with open(json_file) as k:
    jsn = json.load(k)
#print json.dumps(jsn, sort_keys=True, indent=4, separators=(',', ': '))
print len(jsn)
season = Season()
for match in jsn['games'][1:]:
    print('{} scored {} and {} scored {}.'.format(match[2], match[3], match[4], match[5]))

    #print('winner is {}.'.format(winner))
    season.add_match(match[2], match[4], match[3], match[5])



