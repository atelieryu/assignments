#Read superheroes.json
import json


#read superheroes.json
with open('superheroes.json', 'r') as f:
	superheroes = json.load(f)

members = superheroes['members']


#Write a header to the CSV file
import csv
# open a CSV flie
with open('superheroes.csv', 'w') as g:
    writer = csv.writer(g)
    writer.writerow(['name', 'age', 'secretIdentity', 'powers', 'squadName', 'homeTown', 'formed', 'secretBase', 'avtive'])
#Loop over the members, and for each member write a row to the csv file

# loop through each member
    for member in members:
        name = member['name']


        output = [powers]
        
        writer.writerow(output)
