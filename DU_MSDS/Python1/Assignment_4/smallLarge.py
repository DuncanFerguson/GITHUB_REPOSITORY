#Duncan Ferguson
#3005
#Assignment 4

def smallLarge(numList):
    '''This Function takes in a list and returns the smallest and largest numbers in a tuple'''
    newList = [] #setting a new blank list
    numList.sort() #Sorting the List from smallest to largest
    newList += [numList[0]] #Adding Smallest Number to newList
    newList += [numList[len(numList)-1]] #Adding Largest number to newList
    smallLargeTuple = tuple(newList) #Converting newlist into tuple called smallLargeTuple
    return smallLargeTuple

numList = [5,2,3,4,5]
print(smallLarge(numList))

