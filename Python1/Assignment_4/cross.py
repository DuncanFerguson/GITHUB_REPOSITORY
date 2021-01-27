#Duncan Ferguson
#3005
#Assignment 4

def cross(a,b):
    '''This function returns all the combos of every tuple'''
    lista = list(a) #Cast set to list
    listb = list(b) #Cast set to list
    newList = [] #New Blank List

    for x in lista: #loop list a
        for y in listb: #loop list b
            newpair = (x,y) #making a new pair
            newList.append(newpair) #adding that new pair to the list
    return set(newList) #returning the new list as a set


a = {1,2,3}
b = {1,2,4,6,7,8}
print(cross(a,b))

b = cross(a,b)
# print(type(b))
