"""turn scraped html into json"""

import os
from BeautifulSoup import BeautifulSoup
import json

overwrite = True

dirr = "scheduleresults"

def clean_text(text):
    p = text.replace("&nbsp;", '')
    p = p.replace("&#x274d;", '')
    p = p.replace('&#x2605;', '')
    try:
        p = text[text.index('>')+1:]
        return p
    except:
        return p
    

player_dict = dict()
for player_file in os.listdir(dirr):
    print(player_file)
    if overwrite or not os.path.isfile("{}.json".format(player_file[:-5])):
        with open("{}/{}".format(dirr,player_file)) as player_html:
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
                            table_matrix.append([clean_text(element.text) for element in elements])
                        except:
                            raise
                player_dict[table_id] = table_matrix
                with open("{}/{}.json".format(dirr,player_file[:-5]), 'w') as pjson:
                    json.dump(player_dict, pjson)
