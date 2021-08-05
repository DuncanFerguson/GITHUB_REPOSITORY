import pandas as pd
from bokeh.io import output_notebook
import icecream as ic
from datetime import datetime
from ipywidgets import interact, interact_manual
from bokeh.models.widgets import Panel, Tabs
from bokeh.plotting import figure, show
from bokeh.io import show

file = 'Data-Visualization-with-Python-master\Lesson06\Exercise11\data\stock_prices\stock_prices.csv'

dataset = pd.read_csv(file)
# print(dataset)

def shorten_time_stamp(timestamp):
    shortened = timestamp[0]
    if len(shortened) > 10:
        parsed_date = datetime.strptime(shortened, '%Y-%m-%d %H:%M:%S')
        shortened = datetime.strftime(parsed_date, '%Y-%m-%d')
    return shortened

# Method to build the tab-based plot
def get_plot(stock):
    stock_name = stock['symbol'].unique()[0]
    line_plot = figure(title='stock prices',
                       x_axis_label='Date',
                       x_range=stock['short_date'],
                       y_axis_label='Price in $USD')
    line_plot.line(stock['short_date'], stock['high'], legend=stock_name)
    line_plot.xaxis.major_label_orientation = 1
    circle_plot = figure(title='Stock prices', x_axis_label='Date',
                        x_range=stock['short_date'], y_axis_label='Price in $USD')
    circle_plot.circle(stock['short_date'], stock['high'], legend=stock_name)
    circle_plot.xaxis.major_label_orientation = 1
    line_tab = Panel(child=line_plot, title='Line')
    circle_tab = Panel(child=circle_plot, title='Circles')
    tabs = Tabs(tabs=[line_tab, circle_tab])
    return tabs

dataset['short_date'] = dataset.apply(lambda x: shorten_time_stamp(x), axis=1)
stock_names = dataset['symbol'].unique()

@interact(Stock=stock_names)
def get_stock_for(Stock='AAPL'):
    stock = dataset[dataset['symbol'] == Stock][:25]
    show(get_plot(stock))


# print(dataset.head())



# show()