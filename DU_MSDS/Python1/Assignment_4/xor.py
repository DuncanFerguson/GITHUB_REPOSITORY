#Duncan Ferguson
#3005
#Assignment 4

def xor(a,b):
    '''This function returns both A and B and returns a new frozen set containing elements that are in A or B but not both'''
    lista = list(a) #Casting set a into list
    listb = list(b) #Casting Set b into a list
    newList = lista + listb #Combining both lists
    xorSet = [] #Making a blanklist

    for i in range(len(newList)): #Looping through the list
        if newList.count(newList[i]) == 1: #If that number only appears once
            xorSet.append(newList[i]) #Add it back to the list
    return frozenset(xorSet) #Returning a Frozen Set

a = {1,2,3}
b = {1,2,4}
print(xor(a,b))