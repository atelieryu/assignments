
# open veggies csv 
import csv

with open('veggies.csv', 'r') as f:
    reader = csv.DictReader(f)
    vegetables = list(reader)

from pprint import pprint

#Group color
vegtables_by_color = {}
for vegetable in vegetables:
    color = vegetable['color']
    if color in vegtables_by_color:
        vegtables_by_color[color].append(vegetable)
    else:
        vegtables_by_color[color] = [vegetable]
#Print to terminal 

pprint(vegtables_by_color)


#output to json
import json

rows = [vegtables_by_color]

with open('vegtables_by_color', 'w') as f:
    json.dump(rows, f)