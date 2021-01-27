

def readfile():
    """This Point of this function is to read a the list of numbers from a txt file and put them into a list"""
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
    print(histodic)


list_need_2_convert = readfile()
list2dict(list_need_2_convert)
