import pandas as pd
from bokeh.io import output_file
from datetime import datetime


dataset = pd.read_csv('stock_prices.csv')
# print(dataset.head())

def shorten_time_stamp(timestamp):
    shortened = timestamp[0]

    if len(shortened) > 10:
        parsed_date = datetime.strptime(shortened, '%Y-%m-%d %H:%M:%S')
        shortened = datetime.strftime(parsed_date, '%Y-%m-%d')
    return shortened


dataset['short_date'] = dataset.apply(lambda x: shorten_time_stamp(x), axis=1)

from bokeh.plotting import figure, show
from ipywidgets import interact, widgets

def add_candle_plot(plot, stock_name, stock_range, color):
    inc_1 = stock_range.close > stock_range.open
    dec_1 = stock_range.open > stock_range.close
    w = 0.5

    plot.segment(stock_range['short_date'], stock_range['high'],
                 stock_range['short_date'], stock_range['low'],
                 color="grey")

    plot.vbar(stock_range['short_date'][inc_1], w,
              stock_range['high'][inc_1], stock_range['close'][inc_1],
              fill_color="green", line_color="black",
              legend=('Mean price of ' + stock_name), muted_alpha=0.2)

    plot.vbar(stock_range['short_date'][dec_1], w,
              stock_range['high'][dec_1], stock_range['close'][dec_1],
              fill_color="red", line_color="black",
              legend=('Mean price of ' + stock_name), muted_alpha=0.2)

    stock_mean_val=stock_range[['high', 'low']].mean(axis=1)
    plot.line(stock_range['short_date'], stock_mean_val,
              legend=('Mean price of ' + stock_name), muted_alpha=0.2,
              line_color=color, alpha=0.5)


# method to build the plot
def get_plot(stock_1, stock_2, date, value):
    stock_1 = dataset[dataset['symbol'] == stock_1]
    stock_2 = dataset[dataset['symbol'] == stock_2]

    stock_1_name = stock_1['symbol'].unique()[0]
    stock_1_range = stock_1[(stock_1['short_date'] >= date[0]) & (stock_1['short_date'] <= date[1])]
    stock_2_name = stock_2['symbol'].unique()[0]
    stock_2_range = stock_2[(stock_2['short_date'] >= date[0]) & (stock_2['short_date'] <= date[1])]

    plot = figure(title='Stock prices',
                  x_axis_label='Date',
                  x_range=stock_1_range['short_date'],
                  y_axis_label='Price in $USD',
                  plot_width=800,
                  plot_height=500)

    plot.xaxis.major_label_orientation = 1
    plot.grid.grid_line_alpha = 0.3

    if value == 'open-close':
        add_candle_plot(plot, stock_1_name, stock_1_range, 'blue')
        add_candle_plot(plot, stock_2_name, stock_2_range, 'orange')

    if value == 'volume':
        plot.line(stock_1_range['short_date'], stock_1_range['volume'],
                  legend=stock_1_name, muted_alpha=0.2)
        plot.line(stock_2_range['short_date'], stock_2_range['volume'],
                  legend=stock_2_name, muted_alpha=0.2,
                  line_color='orange')

    plot.legend.click_policy = "mute"
    return plot

# extracing the necessary data
stock_names=dataset['symbol'].unique()
dates_2016=dataset[dataset['short_date'] >= '2016-01-01']['short_date']
unique_dates_2016=sorted(dates_2016.unique())
value_options=['open-close', 'volume']

# setting up the interaction elements
drp_1=widgets.Dropdown(options=stock_names,
                       value='AAPL',
                       description='Compare:')

drp_2=widgets.Dropdown(options=stock_names,
                       value='AON',
                       description='to:')

range_slider=widgets.SelectionRangeSlider(options=unique_dates_2016,
                                          index=(0,25),
                                          continuous_update=False,
                                          description='From-To',
                                          layout={'width': '500px'})

value_radio=widgets.RadioButtons(options=value_options,
                                 value='open-close',
                                 description='Metric')

# creating the interact method
@interact(stock_1=drp_1, stock_2=drp_2, date=range_slider, value=value_radio)
def get_stock_for_2016(stock_1, stock_2, date, value):
    output_file('This.html')
    show(get_plot(stock_1, stock_2, date, value))

