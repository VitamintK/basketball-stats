"""idea for this came from
http://www.reddit.com/r/nba/comments/23a9x8/i_took_the_playoff_bracket_and_moved_teams_up/ from 2014's playoffs"""
import json
from collections import defaultdict
json_file = 'scheduleresults/2014-2015.json'

class Season():
    def __init__(self):
        self.season = defaultdict(list)
        self.scores = defaultdict(list)
    def add_match(self, team1, team2, team1score, team2score):
        try:
            winner = (team1, team2)[int(team2score) > int(team1score)]
        except:
            winner = None
        teams = (team1, team2)
        self.season[frozenset(teams)].append(winner)
        self.scores[frozenset(teams)].append({team1: team1score, team2: team2score})
    def get_records(self, team):
        pass
    def get_record(self, team1, team2):
        x = self.season[frozenset((team1, team2))]
        return x.count(team1), x.count(team2)
    def get_winner(self, team1, team2):
        print("Matchup is {} vs. {}.".format(team1, team2))
        records = self.get_record(team1, team2)
        if records[1] == records[0]:
            print("    The teams are tied with a record of {} - {} against each other".format(records[1], records[0]))
            score = dict()
            scores = self.scores[frozenset((team1, team2))]
            for team in scores[0].keys():
                score[team] = sum(int(x[team]) for x in scores)
            winur = max(score, key=lambda x: score[x])
            print('    Point tiebreaker.  winner is {} with {} over {} with {}.'.format(
                winur, max(score.values()), min(score, key=lambda x: score[x]), min(score.values())))
            return winur
        print("    {} wins with a records of {}-{} over {}".format(
            (team1, team2)[records[1] > records[0]], max(records[1], records[0]), min(records[1], records[0]), (team2, team1)[records[1] > records[0]]))
        return (team1, team2)[records[1] > records[0]]    

with open(json_file) as k:
    jsn = json.load(k)
#print json.dumps(jsn, sort_keys=True, indent=4, separators=(',', ': '))
season = Season()
for match in jsn['games'][1:]:
    #print('{} scored {} and {} scored {}.'.format(match[2], match[3], match[4], match[5]))
    #print('winner is {}.'.format(winner))
    season.add_match(match[2], match[4], match[3], match[5])

class Playoffs():
    def __init__(self, seeds):
        self.seeds = seeds
    def run(self):
        seeds = self.seeds
        while True:
            if len(seeds['west']) >=8:
                print("---FIRST ROUND---")
            elif len(seeds['west']) >= 4:
                print("---SECOND ROUND---")
            elif len(seeds['west']) >= 2:
                print("---CONFERENCE FINALS---")
            next_round = {'east': [], 'west': []}
            for division in ('west','east'):
                s = seeds[division]
                for i in range(len(s)//2):
                    team1, team2 = s[i], s[-i-1]
                    winner = season.get_winner(team1, team2)
                    next_round[division].append(winner)
            if all(len(x) == 1 for x in next_round.values()):
                print("---CHAMPIONSHIP MATCH---")
                winner = season.get_winner(next_round['east'][0], next_round['west'][0])
                return winner
            else:
                seeds = next_round
            #GROSS GROSS GROSS prof bull would be ashamed of this code :( do this recursively instead

def run_sim():
    """this method named after bhullar"""
    seeds = {'east': ['Atlanta Hawks', "Cleveland Cavaliers", "Chicago Bulls", "Toronto Raptors", "Washington Wizards", "Milwaukee Bucks", "Boston Celtics", "Brooklyn Nets"],
             'west': ['Golden State Warriors', 'Houston Rockets', 'Los Angeles Clippers', "Portland Trail Blazers", "Memphis Grizzlies", "San Antonio Spurs", "Dallas Mavericks", "New Orleans Pelicans"]}
    playoffs = Playoffs(seeds)
    print(playoffs.run())
run_sim()
