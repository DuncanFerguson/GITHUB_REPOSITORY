from csv import reader
import collections
from itertools import combinations
import pandas as pd

NUMTRANS = 0
minSupCount = 3

itemSetCount = collections.defaultdict(int)
with open('smallinput.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        NUMTRANS += 1
        string = "".join(row)
        perms = [''.join(l) for i in range(len(string)) for l in combinations(string, i + 1)]
        for i in perms:
            itemSetCount[i] += 1

df = pd.DataFrame({'Keys': list(itemSetCount.keys()), 'Values': list(itemSetCount.values())})
df.set_index('Keys', inplace=True)
df['min_sup'] = df['Values']/NUMTRANS * 100
print(df)

