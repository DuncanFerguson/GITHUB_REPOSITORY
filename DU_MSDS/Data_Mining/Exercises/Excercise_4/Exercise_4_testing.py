import numpy as np

row = ['A', 'B', 'C', 'D']

for a in range(len(row)-2):
    for b in range(a+1, len(row)):
        for c in range(b+1, len(row)):
            print(str(a)+str(b)+str(c))
            print(row[a]+""+row[b]+""+row[c])
            itemSet = row[a] + "," + row[b] + "," + row[c]

print(itemSet)

print("\nPrinting all 2-itemsets:")

for a in range(len(row)-1):
    print(str(a)+str(b))
    print(row[a]+""+row[b])
    itemSet = row[a] + ""+row[b]
    print(itemSet)
