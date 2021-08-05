import pandas as pd
from bokeh.io import output_notebook
import icecream as ic
from datetime import datetime
from ipywidgets import interact, interact_manual


file = 'Data-Visualization-with-Python-master\Lesson06\Exercise11\data\stock_prices\stock_prices.csv'

dataset = pd.read_csv(file)
print(dataset)

def shorten_time_stamp(timestamp):
    shortened = timestamp[0]
    if len(shortened) > 10:
        parsed_date=datetime.strptime(shortened, '%Y-%m-%d %H:%M:%S')
        shortened = datetime.strftime(parsed_date, '%Y-%m-%d')
    return shortened

dataset['short_date'] = dataset.apply(lambda x: shorten_time_stamp(x), axis=1)

print(dataset.head())

@interact(Value=False)
def checkbox(Value=False):
    print(Value)

options=['Option1', 'Option2', 'Option3', 'Option4']
@interact(Value=options)
def slider(Value=options[0]):
    print(Value)

