
def divisibleBy(numList):
    '''This Function Makes a list of all even numbers divisable by 3 from 3 to 1000 '''
    #It is t
    for i in range(2,1001,2):
        if i%3 == 0:
            numList.append(i)
    return numList

numList = []
print(divisibleBy(numList))
