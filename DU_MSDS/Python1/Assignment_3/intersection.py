# Duncan Ferguson
# Comp 3007

def intersection(a,b):
    '''This Functions returns the numbers that appear in both lists'''
    #Setting up variables
    dubs = []
    for i in range(len(a)):
        findNum = a[i]
        if b.count(findNum) >= 1:
            if dubs.count(findNum) == 0:
                dubs.append(a[i])
    return dubs

a = [1,2,2,3,4]
b = [2,3,4]

print("These numbers are in Both lists: ", intersection(a,b))
print("a list: ", a)
print("b list: ", b)





