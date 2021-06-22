#Duncan Ferguson
#3005
#Assignment 4

def invertDict(a):
    '''This definition takes in a dictionary and inverserses the keys and values
    (keys become values and values become keys). , taking account for duplicates'''
    newDict = {}

    # This doesnt account for the duplicates
    # for key in a: newDict[a[key]] = key

    #This one returns two values for one key if they already exist
    for key, value in a.items():
        if value not in newDict:
            newDict[value] = [key]
        else:
            newDict[value].append(key)

    return newDict

a = {'Alice':'red', 'Bob':'blue', 'Susan':'green', 'Dan':'blue'}
print(invertDict(a))
