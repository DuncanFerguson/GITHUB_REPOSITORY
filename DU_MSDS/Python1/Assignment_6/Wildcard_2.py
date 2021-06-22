import matplotlib.pyplot as plt
# This Program takes in a Property values by zip code and puts them into a State average bin.


def openfile():
    """This Definition Opens up the desired excel file and places each list into a row and strips out the newline"""
    filelist = []  # blank list to store values
    with open("Property_Values.csv", mode='r', encoding='UTF-8') as csv_file:
        i = 1
        for row in csv_file:
            if i == 1:  # Printing Column Headers, but NOT adding them to the dictionary
                print(row)  # Printing out the column headers
                i += 1
            elif i > 1:
                filelist.append(row.rstrip('\n'))  # Stripping out the new line in my new list
                i += 1
    return filelist


def makestatedict(newlist):
    """This Function takes a list makes a dictionary with each state and all the values of the percent change in
    home prices. It then take that dictionary and makes another dictionary with the average change home prices by
    state"""
    statedict = {}  # First Dictionary with the key being the state values being a list of % Change
    averagedict = {}  # Second Dictionary, key as the state, value as the average of % Change
    for i in range(len(newlist)):  #Lopping through list and making 1st dictionary
        new = newlist[i].split(",")  # Taking my string values and turning them into a list
        state = new[3]  # State Value is the 3rd index (4) on each line of the list
        if new[16] == 'NA' or new[16] == 'none':
            continue  # I do not want to count the rows of data that are not there aka NA values
        else:
            if state in statedict:  # If the state exists, add the value to the end of the list
                statedict[state] = statedict[state] + [float(new[16])]
            else:
                statedict[state] = [float(new[16])]  # Adding my state and the initial value
    for key in statedict:  # Making an Average Dictionary of the Statedict values
        averagedict[key] = sum(statedict[key])/len(statedict[key])
    return averagedict


def makesortedlist(histo):
    """This Function takes a dictionary, sorts it, and returns it as two lists"""
    sorted_dict = sorted(histo.items(), key=lambda x: x[1])  # Sorting my graph from lowest to highest
    states = []  # Making a Blank State List
    average = []  # Making a Blank Average List
    for i in sorted_dict:  # Lopping through the sorted dict and making two new lists
        states.append(i[0])
        average.append(i[1])
    return states, average


def makebar(x, y):
    """This Takes a histogram and turns it into a bar chart"""
    fig = plt.figure(figsize=(15, 7))  # Making my chart size
    ax = fig.add_subplot(111)  # This is making the grid 1x1
    ax.bar(x, y, align='center')  # Adding my values and aligning them in the center
    plt.xlabel("States")  # xLabel
    plt.ylabel("State Change (%) in Home Value")  # yLable
    plt.title("Increase in Home Value (%) per state from 2010 to 2019")  # Title
    plt.show()  # Making sure to show the graph


file = openfile()  # Open file and put into each row into a list
average_state_increase = makestatedict(file)  #Take List of data and make dictionaries
list_4_Graph = makesortedlist(average_state_increase)  # Sorting my Dictionary then making two lists
makebar(list_4_Graph[0], list_4_Graph[1])  # Making Graph of my two lists


