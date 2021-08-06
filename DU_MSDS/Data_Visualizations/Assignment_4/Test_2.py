# Import geopandas package
import geopandas as gpd
import pandas as pd
import numpy as np
import json
import geoplot as gplt
# import geoplot.crs as gcrs
from bokeh.io import show
from bokeh.models import (CDSView, ColorBar, ColumnDataSource,
                          CustomJS, CustomJSFilter,
                          GeoJSONDataSource, HoverTool,
                          LinearColorMapper, Slider, Dropdown)
from bokeh.layouts import column, row, widgetbox
from bokeh.palettes import brewer, viridis
from bokeh.plotting import figure, output_file
from bokeh.models.widgets import CheckboxGroup
import icecream as ic

# Importing the JSON data set
file = 'states_geo.json'
file2 = 'StrumData.csv'
file3 = 'states_id.csv'

# Importing the JSON File
with open(file) as geoJSON_df:
    dataset = json.load(geoJSON_df)

# Importing the Strum Dataset
with open(file2) as strum:
    df_2 = pd.read_csv(strum)

# Importing the State IDs
with open(file3) as state_id:
    df_3 = pd.read_csv(file3, usecols=[0, 1], names=["state_id", "state"], header=None, sep=',"\t')
    df_3['state'] = df_3['state'].str.strip('"')

# Merging Data Sets and finding Missing States
strum_w_id = df_2.merge(df_3, left_on='state', right_on='state')  # Merged Data Set
missing_states = np.setdiff1d(df_3['state'].to_list(), strum_w_id['state'].to_list()).tolist()  # Missing States

# Removing Missing states from the JSON file
datetime_cols = ['debtfree', 'effectivemwpa', 'earnings', 'wills', 'soletrader']  # columns to turn into datetime
for element in reversed(dataset['features']):
    element['state'] = df_3.iloc[element['id'], :][1]  # Add state
    add_df = strum_w_id[strum_w_id['state_id'] == element['id']]
    if element['state'] in missing_states:  # If the state is in that change list, remove it
        dataset['features'].remove(element)  # Removing states that are in the data list
    else:
        for i in add_df:
            element['properties'][i] = add_df[i].values[0]

# Reformatting the difference in the data
for element in dataset['features']:
    for i in element['properties']:
        if i in datetime_cols:
            if np.isnan(element['properties'][i]):
                element['properties'][i] = 'No Data'
            else:
                element['properties'][i] = int(element['properties'][i])

# Creating a GeoDataFrame
j_dataset = gpd.GeoDataFrame.from_features(dataset["features"])
json_data = json.dumps(json.loads(j_dataset.to_json()))
geosource = GeoJSONDataSource(geojson=json_data)
print(j_dataset.head())

# Setting Up Color Scale to use
palette = viridis(100)
palette = palette[::-1]

fields = ['state', 'debtfree', 'effectivemwpa', 'earnings', 'wills', 'soletrader']

d = Dropdown(label=fields[0], menu=fields)
def handler(event):
    print(event.item)

d.on_click(handler)

color_mapper = LinearColorMapper(palette=palette, low=strum_w_id['earnings'].min(), high=strum_w_id['earnings'].max(),
                                 nan_color='#d9d9d9')  # Define custom tick labels for color bar.

color_bar = ColorBar(color_mapper=color_mapper, label_standoff=8, width=20, height=500,
                     border_line_color=None, location=(0, 0), orientation='vertical')

p = figure(title='Look at US Earnings Metrics',
           plot_height=600,
           plot_width=950,
           toolbar_location='right',
           tools='pan, box_select,zoom_in,zoom_out,save,reset')

# Blanking out the grid lines
p.xgrid.grid_line_color = None
p.ygrid.grid_line_color = None

#
p.patches('xs', 'ys', source=geosource,
          fill_color={'field': 'earnings', 'transform': color_mapper},
          line_color='black',
          line_width=0.25,
          fill_alpha=1)

p.add_layout(color_bar, 'right')

# Setting Up Hover Options
hover = HoverTool()
hover.tooltips = """
    <div>
        <h3>@state</h3>
        <div><strong>Earnings: </strong>@earnings</div>
        <div><strong>Debtfree: </strong>@debtfree</div>
        <div><strong>Effective_mwpa: </strong>@effectivemwpa</div>
        <div><strong>Earnings: </strong>@earnings</div>
        <div><strong>Wills: </strong>@wills</div>
        <div><strong>Sole_Trader: </strong>@soletrader</div>
    </div>
"""

# RadioGroup(labels, active)

output_file("index.html")
cb = CheckboxGroup(labels=["Grey Scale"], active=[0])

# show(checkbox_group)

p.add_tools(hover)
show(column(cb, d, p))