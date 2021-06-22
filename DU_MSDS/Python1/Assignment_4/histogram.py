#Duncan Ferguson
#3005
#Assignment 4

def histogram(example):
    '''This creates a dictionary that lists the number, and howmany times it appears. The index is the number, the value is the number of times it appears'''
    histogramDict = {} #Creating a Blank Dictionary
    numsAdding = list(set(example)) #Turning examples into a set to remove duplicates, then casting back to list, these will be the keys

    for (i,element) in enumerate(numsAdding): #looping through my list of keys
        histogramDict[numsAdding[i]] = example.count(numsAdding[i]) #counting the number of values a certain key contains
    return histogramDict

example =[1,3,5,2,1,2,5,8,4,5]
print("Histogram Dictionary", histogram(example))