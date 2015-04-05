"""turn scraped html into json"""
#possible libraries: numpy, pandas, or some database.

import os
from BeautifulSoup import BeautifulSoup
import json

overwrite = False

if not os.path.isdir('json'):
	os.makedirs('json')

player_dict = dict()
for player_file in os.listdir('scraped-html/players/'):
	print(player_file)
	if overwrite or not os.path.isfile("json/{}.json".format(player_file[:-5])):
		with open("scraped-html/players/{}".format(player_file)) as player_html:
			soup = BeautifulSoup(player_html)
			tables = soup.findAll('table')
			for table in tables:
				table_matrix = []
				table_id = table.get('id')
				if table_id != None:
					rows = table.findAll('tr')
					for row in rows:
						try:
							elements = row.findAll('td')
							if len(elements) < 1:
								elements = row.findAll('th')
							table_matrix.append([element.text for element in elements])
						except:
							raise
				player_dict[table_id] = table_matrix
				with open("json/{}.json".format(player_file[:-5]), 'w') as pjson:
					json.dump(player_dict, pjson)


"""
{
	Name: MJ
	Trivia: {
		Draft pick: 2
		Draft year: 1960

	}

	Totals:{
		1989:
		{
			reb: 10
			fg: 100

		},

	}

}"""