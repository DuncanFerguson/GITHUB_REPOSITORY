from climata.snotel import StationDailyDataIO
import matplotlib.pyplot as plt
import pandas as pd


def choosestation():
    """" This allows you to pick which station you would like to look at. It returns [station name, #ID]
    https://www.nrcs.usda.gov/wps/portal/wcc/home/quicklinks/imap"""

    stationDict = {'Vail Station, CO': '840:CO',
                   'Sun Valley Station: ID': '895:ID',
                   'Snow Bird, UT': '766:UT',
                   'Wolf Creek, CO': '874:CO',
                   'Taos Powerhorn, NM':  '1168:NM',
                   'Grand Targhee, WY': '1082:WY',
                   'Squaw, CA': '784:CA'}

    print("\nWhich Station Would you Like to Look at?\n")

    i = 1
    stationChoiceDict ={}  # Making a blank dictionary to store choice values inn
    for key in sorted(stationDict):  #Looping through the station choices, sorted of course
        stationChoiceDict[i] = [key, stationDict[key]]
        print(i, " : ", key)  # Printing out the code
        i += 1

    station_num = int(input("\nEnter Number Station Number: "))
    stationChoice = stationChoiceDict[station_num]  # Making a list of the Station and it's call number

    return stationChoice


def dateselector():
    """ This Definition lets the user select the dates"""
    print('\n Select the Dates you would like to Graph\n')
    start_date = input("Enter the START date (YYYY-MM-DD): ")
    end_date = input("Enter the END date (YYYY-MM-DD): ")
    print("Downloading Data...")
    return [start_date, end_date]


def snowflowapi(datelist, id):
    """This uses the climata api to help get snow coverage Reports
    More infomation on the imported module can be found here: https://pypi.org/project/climata/"""

    station_id = id + ':SNTL'  # Adding the SNTL to the station ID
    params = StationDailyDataIO(station = station_id,
                                start_date = datelist[0],
                                end_date = datelist[1])
    elementlist = []  # Print this if you would like to see the element List options
    datalist = []
    i = 0
    for param in params:  # Making Element List
        elementlist.append(param.element_name)  # This is storing a list of element names
        i += 1
        for row in param.data:
            datalist.append([elementlist[i-1], row.date, row.value, param.storedunitcd])  #data into a list
    return [datalist, elementlist]


def chooseElement(elementlist):
    """This lets the user select which list of data they would like to use"""
    print("\nStation Element Types\n")
    for i in range(len(elementlist)):
        print(elementlist[i], ":", i+1)
    userelement = int(input("\nType the number next to the element list above that you would like to choose: "))
    userselect = elementlist[userelement-1]

    return userselect


def selectelement(elementname, datastring):
    """this function goes through the data string, and selects the on with the correct Element. This is then put into
    a year dictionary"""
    datelist = []
    metriclist = []

    for i in datastring:
        if i[0] == elementname:  # first i of this list. But is also coorelated to the element list
            datelist.append(i[1])
            metriclist.append(i[2])
            valuetype = str(i[3])
        else:
            continue
    return datelist, metriclist, valuetype


def makegraph(graphdata, graph_type, graph_title,stationName):
    """Make Graph"""
    df = pd.DataFrame({'value': graphdata[1]}, index=pd.DatetimeIndex(graphdata[0]))
    pv = pd.pivot_table(df, index=df.index.month, columns=df.index.year, values='value')
    pv.plot()
    plt.xlabel("Month")
    plt.ylabel(graph_type + " (" + graphdata[2]+")")
    plt.title(stationName + "\n" + graph_type + " from " + graph_title[0] + " to " + graph_title[1]+ "\n")
    plt.show()


station_name_call = choosestation()  # This lets the user choose the station. Returns, [Station Name, #ID]
dateSelected = dateselector()
snowdata = snowflowapi(dateSelected,station_name_call[1])  # 0 index is data in list form 1 index is list of elements
element = chooseElement(snowdata[1])
graphdata = selectelement(element, snowdata[0])  # Composition [[Data List], [metriclist], 'valuetype']
makegraph(graphdata, element, dateSelected,station_name_call[0])
