def digitsAsWords():
    '''This definition prints out the word version of the  number entered'''
    x = str(input("Enter a Number: "))
    newlist = []
    l = len(x)
    z = 0
    while z < l:
        i = int(x[z])
        z += 1
        newlist.append(digitToWord(i))
    newlist = " ".join(newlist)
    print(newlist)

def digitToWord(i):
    wordlist = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    return wordlist[i]

digitsAsWords()

# https://www.geeksforgeeks.org/python-program-to-convert-a-tuple-to-a-string/
# ^ For converting tuple into string