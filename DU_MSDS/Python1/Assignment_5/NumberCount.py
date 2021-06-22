def readfile():
    """This Point of this function is to write the list of numbers to a file"""
    filelist = []
    with open('RandomNumbers.txt', mode='r', encoding='UTF-8') as f:
        for line in f:
            filelist.append(line.rstrip('\n'))
    return filelist


def list2dict(convertlist):
    """This takes in a list and turns it into a dictiony, aka a histogram"""
    histodic = {}
    for i in convertlist:
        if i in histodic:
            histodic[i] += 1
        else:
            histodic[i] = 1
    return histodic


def writefile(writelist):
    """This takes my new dictionary and writes it to a csv file"""
    packstring = "Number, Number '#' \n"
    for i in writelist:  # Looping through the dictionary and turning it into a string to write
        packstring += i  # First Dictionary Term
        packstring += ","  # Nice Double tap here with a shift of columns with the comma
        packstring += str(writelist[i])  # Lets pull that dictionary key's value
        packstring += '\n'  # Time to bump down rows

    with open("NumberCounts.csv", mode='w', encoding='UTF-8') as f:
        f.write(packstring)
    return packstring


list_need_2_convert = readfile()
histogramdictionary = list2dict(list_need_2_convert)
print(histogramdictionary)
writefile(histogramdictionary)
