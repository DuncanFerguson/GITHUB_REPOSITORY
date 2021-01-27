from urllib.request import Request, urlopen

def startprogram():
    """This function is a user interface"""
    print("We are about to create a DB for storing: Upper Colorado River Info")
    startdate = input("Start Date(YYYY-MM-DD): ")
    enddate = input("End Date (YYYY-MM-DD): ")
    datelist = [startdate, enddate]
    return datelist


def getwebdata(dates):
    """This goes through and collects web data"""
    print(type(dates))
    # url = 'https://waterdata.usgs.gov/usa/nwis/uv?09058000'

    url = 'https://waterdata.usgs.gov/nwis/uv?cb_00010=on&cb_00045=on&cb_00060=on&cb_00065=on&format=gif_default&site_no=09058000&period=&begin_date='
    newUrl = url + str(dates[0]) + "&end_date=" + str(dates[1])
    req = Request(newUrl, headers={'User-Agent': 'Mozilla/5.0'})
    web_byte = urlopen(req).read()
    webpage = web_byte.decode('utf-8')
    item = webpage[webpage.find('</td> <td class="highlight2" nowrap>')+36:webpage.find('</td> <td>')]  # Finding my CFS Number
    return item


dates = startprogram()
webdata = getwebdata(dates)
# print(webdata)



