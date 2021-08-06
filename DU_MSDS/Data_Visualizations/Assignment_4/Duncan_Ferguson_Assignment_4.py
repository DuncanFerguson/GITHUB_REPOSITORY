# Student: Duncan Ferguson
# Student Id: 871641260
# Class: Comp 4433
# Assignment: Assignment 4
# Date 8/6/2021

# Cited Links
# https://towardsdatascience.com/walkthrough-mapping-basics-with-bokeh-and-geopandas-in-python-43f40aa5b7e9
# https://www.howtogeek.com/118594/how-to-edit-your-system-path-for-easy-command-line-access/
# https://geoffboeing.com/2014/09/using-geopandas-windows/
# https://towardsdatascience.com/how-to-step-up-your-folium-choropleth-map-skills-17cf6de7c6fe
# https://towardsdatascience.com/a-complete-guide-to-an-interactive-geographical-map-using-python-f4c5197e23e0
# https://towardsdatascience.com/walkthrough-mapping-basics-with-bokeh-and-geopandas-in-python-43f40aa5b7e9


""" Using free and open source tools, provide a set of choropleth visualizations for each of
the columns containing dates such that the resulting visualizations (48 states only) tell
the story by conveying through color, texture, or both the time lines of achievement of
each milestone/column in the provided dataset.

Missing geoJSON_df are of particular interest in
that when a state has never achieved a given milestone, that should be indicated in a
standout manner such as cross-hatching.

Consider that the publication may be
grayscale. Provide a solution for that as well. Provide the titles, labels, and legends
necessary for clarification. File support is given as follows: SturmCodebook has the
explanation. SturmData is the geoJSON_df CSV.

state – State abbreviation

fips – FIPS State Code

icpsr – ICPSR State Code

debtfree – Year of passage of state law protecting married women’s separate property from her husband’s debts

effectivemwpa – Year of passage of state law granting married women control and management rights over their separate property

earnings – Year of passage of state law granting married women ownership of their wages or earnings on par with other separate property

wills – Year of passage of state law granting married women the ability to write wills without their husband's consent or other restrictions

soletrader – Year of passage of state law granting married women as a class the right to sign contracts and engage in business without consent of husband

Note: This study examines the passage of married women’s economic rights reforms prior to the Nineteenth Amendment (1920, granting women the right to vote at the national level), so states that passed laws later (i.e. Florida passed a control-and-management law in 1943) should be treated as missing data for the purposes of data visualization.
"""

# Import geopandas package
import geopandas as gpd
import pandas as pd
import numpy as np
import json
import geoplot as gplt
# import geoplot.crs as gcrs
from bokeh.io import show, curdoc
from bokeh.models import (CDSView, ColorBar, ColumnDataSource,
                          CustomJS, CustomJSFilter,
                          GeoJSONDataSource, HoverTool,
                          LinearColorMapper, Slider, Dropdown, Select)
from bokeh.layouts import column, row, widgetbox
from bokeh.palettes import viridis
from bokeh.plotting import figure, output_file
from ipywidgets import interact, widgets

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


# source= ColumnDataSource(data=geosource)
print(j_dataset.head())

# Setting Up Color Scale to use
palette = viridis(100)
palette = palette[::-1]

# TODO This give's us the chart that we want to look at
category = 'soletrader'

color_mapper = LinearColorMapper(palette=palette, low=strum_w_id[category].min(), high=strum_w_id[category].max(),
                                 nan_color='#d9d9d9')  # Define custom tick labels for color bar.
color_bar = ColorBar(color_mapper=color_mapper, label_standoff=8, width=20, height=500,
                     border_line_color=None, location=(0, 0), orientation='vertical')

p = figure(title='Look at US ' + category + ' by Year',
           plot_height=600,
           plot_width=950,
           toolbar_location='right',
           tools='pan,box_select,zoom_in,zoom_out,save,reset')

# Blanking out the grid lines
p.xgrid.grid_line_color = None
p.ygrid.grid_line_color = None

p.patches('xs', 'ys', source=geosource,
          fill_color={'field': category, 'transform': color_mapper},
          line_color='black',
          line_width=0.25,
          fill_alpha=1,
          legend_label='Null Data')

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

# Adding Gray Scale box
output_file("index.html", title="Duncan Ferguson")
drop_bar = Select(title="Select Category:", options=datetime_cols, value=datetime_cols[0], width=200)

# show(checkbox_group)
p.add_tools(hover)
show(column(drop_bar, p))
# show(add_root(column(drop_bar, p)))