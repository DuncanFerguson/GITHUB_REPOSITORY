taleChapter1 = "It was the best of times,"


def nthWord(n, myString):
    ''' This is to find the nth word'''
    if(n<0):
        return ""
    elif n >= taleChapter1.count(" ")+1:
        return ""
    else:
        location = -1
        for i in range(n):
            location = myString.find(" ", location+1)
        return myString[location+1:myString.find(" ",location+1)]

# i  =  input("Which word would you like to print")
# print(nthWord(int(i), taleChapter1))

def howMany(sub, myString):
    ''' This counts how many words are in a string'''
    count = 0
    index = myString.find(sub)
    while index > 0:
        count += 1
        index = myString.find(sub, index+1)
    return count



