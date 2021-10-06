from csv import reader
import collections
from itertools import combinations
import pandas as pd

NUMTRANS = 0
minSupCount = 3

itemSetCount = collections.defaultdict(int)
with open('smallinput.csv','r') as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        string = "".join(row)
        perms = [''.join(l) for i in range(len(string)) for l in combinations(string, i + 1)]
        for i in perms:
            itemSetCount[i] += 1

print(itemSetCount)
dictionary = dict(itemSetCount)
df = pd.DataFrame(itemSetCount.values(), index=dictionary.keys())
print(df)