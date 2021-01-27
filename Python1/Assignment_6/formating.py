import matplotlib.pyplot as plt
import matplotlib.dates as md
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
    """This definition makes our actual char"""
    fig, ax = plt.subplots()
    ax.set(xlabel="Date", ylabel="Close Price ($)", title='Apple, Gush and Drip Close Price')
    ax.plot(a[1], a[0], 'b', label='APPL')
    ax.plot(b[1], b[0], 'r', label='DRIP')
    ax.plot(c[1], c[0], 'g', label='GUSH')
    leg = ax.legend()
    xfmt = md.DateFormatter('%m-%d-%y')
    ax.xaxis.set_major_formatter(xfmt)
    plt.xticks(rotation=90)
    plt.show()


appl = appldata()
gush = gushdata()
drip = dripdata()
makechart(appl,gush,drip)






