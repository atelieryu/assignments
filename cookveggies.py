# for row in rows:
#     print(row)
vegetables = [
 {"name": "eggplant", "color": "purple"},
 {"name": "tomato", "color": "red"},
 {"name": "corn", "color": "yellow"},
 {"name": "okra", "color": "green"},
 {"name": "arugula", "color": "green"},
 {"name": "broccoli", "color": "green"},
]
#print(vegetables)
import csv
# open a CSV flie
with open('veggies.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'color'])
	#loop through veggies
    for vegetable in vegetables:

	    # write each veggie to a CSV
        name = vegetable['name']
        color = vegetable['color']
        row = [name, color]

        writer.writerow(row)