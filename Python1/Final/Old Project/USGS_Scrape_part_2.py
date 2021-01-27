from climata.snotel import StationDailyDataIO
import matplotlib.pyplot as plt
import datetime
import pandas as pd

# Mock Data List
graphdata = [[datetime.date(2011, 1, 2), datetime.date(2011, 1, 3), datetime.date(2011, 1, 4), datetime.date(2011, 2, 1),
              datetime.date(2012, 1, 2), datetime.date(2012, 1, 3), datetime.date(2012, 1, 4), datetime.date(2012, 2, 1),
              datetime.date(2013, 1, 2), datetime.date(2013, 1, 3), datetime.date(2013, 1, 4), datetime.date(2013, 2, 1)],
             [10,16,13,16,
              10,11,12,13,
              10,10,11,5], 'in']

def year_over_year(raw_list):
    """This Functionn goes through and takes the data and turns it into a year over year aspect. """
    yearcount = []  # This stores a list of all the years
    for day in raw_list[0]:
        if day.year not in yearcount:  # Making my year list
            yearcount.append(day.year)
    return yearcount

def get_years(years, yeardata):
    """This definition goes through and makes a certain amount of lists. Then adds the data to them"""
    year_dict ={}
    for i in enumerate(years):  # Making a dictionary of the years
        year_dict[i[1]] =  []
    i = 0
    for y in yeardata[0]:
        if y.year in year_dict:
            data = y,yeardata[1][i]  # Need to reindex this to have the second part with ofd list with the values
            year_dict[y.year].append(data)  # Adding that date and value to the year dictionary
            i += 1  # reindexing my way along the datetime list
    return year_dict

def makegraph_year(graphdata, years):
    """This is taking in a string of graph data."""
    i = -1
    # print(years)
    dates= []
    for q in years:  # Making a dates list that mirros the amount of dates in the year list
        dates.append([])
    for year in graphdata:
        # print(type(graphdata))
        # print(years, graphdata[years])
        year_data = graphdata[year]
        i += 1
        years[i] = []  # Taking my years, and making them into a blank list to then have the values added to
        for data in year_data:
            # print("Year: ", year, 'Data: ', data[1],"I Value", i)
            years[i].append(data[1])  # Creating a list of my measurement value for all the years
            dates[i].append(data[0])
    return years, dates


def makegraph(graphdata):
    """Make Graph"""
    print(graphdata[2])
    df = pd.DataFrame({'value': graphdata[1]}, index=pd.DatetimeIndex(graphdata[0]))
    pv = pd.pivot_table(df, index=df.index.month, columns=df.index.year, values='value')
    pv.plot()
    plt.xlabel("Months")
    plt.ylabel("But the type in here Right now Snow: " + graphdata[2])
    plt.show()


# yearlist = year_over_year(graphdata)
# getyear = get_years(yearlist, graphdata)
# yeardate_values = makegraph_year(getyear, yearlist)
# makegraph(yeardate_values[1],yeardate_values[0])

makegraph(graphdata)

### Look into this
#https://stackoverflow.com/questions/30379789/plot-pandas-data-frame-with-year-over-year-data