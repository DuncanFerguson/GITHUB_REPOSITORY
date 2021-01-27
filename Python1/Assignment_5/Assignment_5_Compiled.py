import random


def writetxt(a, b, c):
    """This Function writes a txt file named randomnumbers.txt with c amount of numbers inbetween a and b"""
    with open('RandomNumbers.txt', mode='w', encoding='UTF-8') as f:
        for i in range(int(c)):  # Looping through c amount of times
            randomnum = str(random.randint(a, b))  # choosing random number, making it a string
            f.write(randomnum)  # Writing the Random Number onto the txt file
            f.write('\n')  # Bumping down a line


def readfile():
    """This Point of this function is to read a list of numbers from a txt file and put them into a list"""
    filelist = []
    with open('RandomNumbers.txt', mode='r', encoding='UTF-8') as f:  # Opening my file
        for line in f:
            filelist.append(line.rstrip('\n'))  # Stripping each number of \n and adding it to a list
    return filelist


def list2dict(convertlist):
    """This takes in a list and turns it into a dictiony, aka a histogram"""
    histodic = {}
    for i in convertlist:  # Lopping through the list of numbers
        if i in histodic:  # if the number is already in the dictionary, we are adding a new count
            histodic[i] += 1
        else:  # Number is not in the dictionary, so make a dictionary entry and give it a 1 count
            histodic[i] = 1
    return histodic


def writefile(writelist):
    """This takes a list and writes it to a csv file"""
    packstring = "Number,Number '#' \n"
    for i in writelist:  # Looping through the dictionary and turning it into a string to write
        packstring += i  # First Dictionary Term
        packstring += ","  # Nice Double tap here with a shift of columns with the comma
        packstring += str(writelist[i])  # Lets pull that dictionary key's value
        packstring += '\n'  # Time to bump down rows

    with open("NumberCounts.csv", mode='w', encoding='UTF-8') as f:
        f.write(packstring)
    return packstring


lowerBound = 1  # Lower Bound of the Random Number
upperBound = 10  # Upper Bounder of the Random Number
numberOfNumbers = 100  # This is the amount of random numbers that we want to write

#This writes a Txt file of random numbers
writetxt(lowerBound, upperBound, numberOfNumbers)  # Writing a txt file with random numbers from a to b

print("Your txt File of ", numberOfNumbers,
      " numbers inbetween", lowerBound, " and ", upperBound, " has been created\n")

#This code reads the Txt file that was created
list_need_2_convert = readfile()

#This code takes the list of numbers and puts them into a histogram dictionary
histrogramdictionary = list2dict(list_need_2_convert)

#This writes the histogram dictionary into a CSV File
createdFile = writefile(histrogramdictionary)

print("Your new CSV File named NumberCounts has Been Created")
