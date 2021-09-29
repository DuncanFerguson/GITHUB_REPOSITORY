import numpy as np
from csv import reader



locations = ['SouthGlenn', 'Tamarac', 'HighlandsRanch', 'ColoradoBlvd', 'WashingtonPark', 'CherryCreek', 'GovernorsRanch', 'UnionStation', 'CastleRock']

itemCategories = ['produce', 'meat', 'bakery', 'freezer', 'dairy', 'deli', 'snack', 'softdrinks', 'beer', 'household']

numLocations = len(locations)
numItemCategories = len(itemCategories)

cube = np.zeros((12,numLocations,numItemCategories) )

print(cube.size)

# fin = open('z.csv', 'r') as read_obj:
with open('ds_ex3.txt', 'r') as read_obj:
	csv_reader = reader(read_obj)
	for row in csv_reader:
		print(row)
		print(row[1], row[2], row[3])



'''
# if want to process as .txt....
fin = open('z.txt','r')

while True:
	line = fin.readline()
	if not line:
		break
	print(line)
	# do string stuff with line....

'''