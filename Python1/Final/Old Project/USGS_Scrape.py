from climata.snotel import StationDailyDataIO
import matplotlib.pyplot as plt
import datetime
import pandas as pd

def dateselector():
    """ This Definition lets the user select the dates"""
    start_date = input("Enter the START date (YYYY-MM-DD): ")
    end_date = input("Enter the END date (YYYY-MM-DD): ")
    print("Downloading Data...")
    return [start_date, end_date]


def snowflowapi(datelist):
    """This uses the climata api to help get snow coverage Reports"""
    station_id = '1041:CO:SNTL'  # Beaver creek
    params = StationDailyDataIO(station=station_id,
                                start_date=datelist[0],
                                end_date=datelist[1])
    elementlist = []  # Print this if you would like to see the element List options
    datalist = []
    i = 0
    for param in params:  # Making Element List
        elementlist.append(param.element_name)  # This is storing a list of element names
        i += 1
        for row in param.data:
            datalist.append([elementlist[i-1], row.date, row.value, param.storedunitcd])  # This putting all of this data into a lis
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
        if i[0] == elementname:  # This is looking for the precipitation increment, which is the first i of this list. But is also coorelated to the element list
            datelist.append(i[1])
            metriclist.append(i[2])
            valuetype = str(i[3])
        else:
            continue
    return datelist, metriclist, valuetype


# def year_over_year(raw_list):
#     """This Functionn goes through and takes the data and turns it into a year over year aspect. """
#     yearcount = []  # This stores a list of all the years
#     for day in raw_list[0]:
#         if day.year not in yearcount:  # Making my year list
#             yearcount.append(day.year)
#     return yearcount
#
#
# def get_years(years, yeardata):
#     """This definition goes through and makes a certain amount of lists. Then adds the data to them"""
#     year_dict ={}
#     for i in enumerate(years):  # Making a dictionary of the years
#         year_dict[i[1]] =  []
#     i = 0
#     for y in yeardata[0]:
#         if y.year in year_dict:
#             data = y,yeardata[1][i]  # Need to reindex this to have the second part with ofd list with the values
#             year_dict[y.year].append(data)  # Adding that date and value to the year dictionary
#             i += 1  # reindexing my way along the datetime list
#     return year_dict
#
#
# def makegraph_year(graphdata, years):
#     """This is taking in a string of graph data."""
#     i = -1
#     # print(years)
#     dates= []
#     for q in years:  # Making a dates list that mirros the amount of dates in the year list
#         dates.append([])
#     for year in graphdata:
#         # print(type(graphdata))
#         # print(years, graphdata[years])
#         year_data = graphdata[year]
#         i += 1
#         years[i] = []  # Taking my years, and making them into a blank list to then have the values added to
#         for data in year_data:
#             # print("Year: ", year, 'Data: ', data[1],"I Value", i)
#             years[i].append(data[1])  # Creating a list of my measurement value for all the years
#             dates[i].append(data[0])
#     return years, dates


# def makegraph(x,y):
#     """This function takes in my year data and rips out a sweet graph"""
#     from datetime import datetime
#
#     for i in range(len(x)):
#         monthdates = []
#         # plt.plot(x[i],y[i])
#         for z in enumerate(x[i]):  # Stripping out the year and making it month day
#             date_index = z[1]
#             str_date = date_index.strftime('%m-%d')
#             newdate = datetime.strptime(str_date, '%m-%d')
#             monthdates.append(newdate)
#             print(z)
#         plt.plot(monthdates, y[i])
#     plt.show()

def makegraph(graphdata,graph_type,graph_title):
    """Make Graph"""
    df = pd.DataFrame({'value': graphdata[1]}, index=pd.DatetimeIndex(graphdata[0]))
    pv = pd.pivot_table(df, index=df.index.month, columns=df.index.year, values='value')
    pv.plot()
    plt.xlabel("Month")
    plt.ylabel(graph_type +" ("+ graphdata[2]+")")
    plt.title(graph_type + " from " + graph_title[0] + " to " + graph_title[1])
    plt.show()



dateSelected = dateselector()
snowdata = snowflowapi(dateSelected)  # 0 index is data in list form 1 index is list of elements
element = chooseElement(snowdata[1])
graphdata = selectelement(element, snowdata[0])  #Composition [[Data List], [metriclist], 'valuetype']

## Probably dont need this all below
# yearlist = year_over_year(graphdata) # Getting a list of all the years
# getyear = get_years(yearlist, graphdata)
# yeardate_values = makegraph_year(getyear, yearlist)
# makegraph(yeardate_values[1],yeardate_values[0])

makegraph(graphdata, element, dateSelected)

