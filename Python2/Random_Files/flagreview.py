import sys

list = []
for val in sys.argv:
    print(val)
    list.append([val])

print(list)