import matplotlib.pyplot as plt
import yfinance as yf

def appldata():
    """This imports the APPL Data"""
    df = yf.download('AAPL', '2020-01-01', '2020-10-26')
    appl_close = df['Close'].tolist()
    appl_dates = df.index.to_list()
    return appl_close, appl_dates


def dripdata():
    """This imports the DRIP Data"""
    df = yf.download('DRIP', '2020-01-01', '2020-10-26')
    drip_close = df['Close'].tolist()
    drip_dates = df.index.to_list()
    return drip_close, drip_dates


def gushdata():
    """This imports the GUSH Data"""
    df = yf.download('GUSH', '2020-01-01', '2020-10-26')
    gush_close = df['Close'].tolist()
    gush_dates = df.index.to_list()
    return gush_close, gush_dates


def makechart(a,b,c):
    """This definition makes our actual chart"""
    plt.plot(a[1], a[0], 'b', b[1], b[0], 'r', c[1], c[0], 'g')  # Adding lines to chart
    plt.legend(('APPL','GUSH','DRIP'), loc="upper right")  # Displaying Legend
    plt.xlabel('Dates')  # x Labels
    plt.ylabel('Close Price ($)')  # y Labels
    plt.title("Appl, Gush, Drip Close Prices")  # Chart Title
    plt.xticks(rotation=45)  # Rotating x axis ticks 45 degrees
    plt.show()  # Showing the graph
    return


appl = appldata()  # get apple Data
gush = gushdata()  # get Gush Data
drip = dripdata()  # Get Drip Data
makechart(appl,gush,drip)  # Pass through my data into making a chart