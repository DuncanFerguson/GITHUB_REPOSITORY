from csv import reader
import collections



NUMTRANS = 0
minSupCount = 3

itemSetCount = collections.defaultdict(int)
with open('smallinput.csv','r') as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        NUMTRANS += 1
        itemSet = ""
        for i in range(len(row)):
            itemSet += row[i]
        itemSetCount[itemSet] += 1





print(itemSetCount)

