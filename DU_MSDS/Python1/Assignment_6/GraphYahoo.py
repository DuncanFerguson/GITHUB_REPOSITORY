import yfinance as yf
import matplotlib.pyplot as plt

#Gathering the yfinance info
df = yf.download('AAPL', '2020-01-01', '2020-10-26')
close = df['Close'].tolist()
dates = df.index.to_list()

plt.plot(dates, close, 'r--', )  # Making graph with red dotted line
plt.ylabel("$ Close Price")  # ylabel
plt.xlabel("Date")  # xlabel
plt.title("AAPL - Close Prices")  # Title
plt.xticks(rotation=45)  # Rotating x axis ticks 45 degrees

plt.show()
