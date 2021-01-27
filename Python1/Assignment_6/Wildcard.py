import csv
import matplotlib.pyplot as plt


def openfile():
    """This Definition Opens up the desired excel file"""
    filelist = []
    with open("Raw_Tax_Roll_Example.csv", mode='r', encoding='UTF-8') as f:
        data = csv.reader(f)
        for line in data:
            filelist.append(line)
    return filelist


def makedictionary(filelist):
    """This goes through the sheet and determines how many properties each Owner has"""
    ownerdict = {}
    for i in filelist:
        key = i[0]
        if key in ownerdict:
            dictlist = ownerdict[key]  # Grabbing the dictionary value which is in a list
            newpropcount = dictlist[2] + 1  # Adding a count to the property
            newnra = float(dictlist[1]) + float(i[12])  # Adding the old NRA count to the new NRA Count
            ownerdict[key] = [i[4], newnra, newpropcount]  # Giving my dictionary an updated value
        else:
            ownerdict[key] = [i[4], i[12], 1]
    return ownerdict


def statehistogram(dict):
    """this Function takes in a dictionary and gives me a list in histogram form"""
    statehisto = {}
    for i in dict:  # Making a Dictionary of the states
        key = dict[i]
        if key[0] not in statehisto:
            statehisto[key[0]] = 1
        else:
            statehisto[key[0]] += 1
    return statehisto

def histo2list(histo):
    """This Function takes a dictionary and makes two lists, one of the values the other of the keys"""
    states = []
    statecount = []
    for i in histo:
        states.append(i)
        statecount.append(histo[i])
    states.pop(0)  # Popping off the first term
    statecount.pop(0)  # Popping off the first term
    return states, statecount


def makechart(x,y):
    """This definition makes our actual char"""
    plt.bar(x,y, color = 'maroon', width = .5)
    plt.xlabel("States")
    plt.ylabel("Number of Owners")
    plt.title("Ownership By State")
    plt.show()
    return

def makepie(x,y):
    """This definition makes a Pie Char"""
    fig1, ax1=plt.subplots()
    ax1.pie(y, labels=x, autopct='%1.f%%')
    ax1.axis('equal')
    plt.show()
    return

def averagePropNumByState(dictionary):
    """This function returns a list of states and the average number of properties owned in that state"""
    statepropaverage = {}
    for i in dictionary:
        key = dictionary[i]
        if key[0] not in statepropaverage:
            statepropaverage[key[0]] =


        print(value)



file_data = openfile()
ownerdictionary = makedictionary(file_data)
statehist = statehistogram(ownerdictionary)
data4graph = histo2list(statehist)
makechart(data4graph[0],data4graph[1])
makepie(data4graph[0],data4graph[1])
averagePropNumByState(ownerdictionary)




