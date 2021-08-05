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

import numpy as np
import pandas as pd
import json
import geoplotlib
from geoplotlib.colors import ColorMap
from geoplotlib.utils import BoundingBox
import geopandas as gpd
from datetime import datetime


# from bokeh.io import curdoc, output_notebook
# from bokeh.models import Slider, HoverTool
from bokeh.layouts import widgetbox, row, column
from bokeh.palettes import brewer, cividis, gray, viridis
from bokeh.io import output_notebook, show, output_file
from bokeh.plotting import figure, show
from bokeh.models import (CDSView, ColorBar, ColumnDataSource,
                          CustomJS, CustomJSFilter,
                          GeoJSONDataSource, HoverTool,
                          LinearColorMapper, Slider, Dropdown)
from bokeh.models.widgets import Panel, Tabs, Select
from bokeh.io import show
from bokeh.application import Application
from bokeh.application.handlers import FunctionHandler


from ipywidgets import interact, interact_manual
from bokeh.io import curdoc
from icecream import ic  # print tester


def JSON_Fun():
    """ Aimed at importing the JSON files"""
    file = 'states_geo.json'
    # listing the states in the dataset
    with open(file) as geoJSON_df:
        dataset = json.load(geoJSON_df)
        GEO_states = [feature['id'] for feature in dataset.get('features')]
    return dataset, GEO_states


def CSV_Fun():
    """ Aimed at importing an aligning the CSV sheets"""
    # Importing StrumData and States ID
    df = pd.read_csv('StrumData.csv')

    # There is a tab space located in the csv file. Stripping that out and cleaning the data
    df_states_id = pd.read_csv('states_id.csv', usecols=[0, 1], names=["state_id", "state"], header=None, sep=',"\t')
    df_states_id['state'] = df_states_id['state'].str.strip('"')

    # Joining the two sheets together
    combo_df = df.set_index('state').join(df_states_id.set_index('state'))

    # Grabbing states from DF
    combo_df_states = combo_df[["state_id"]].values.tolist()
    return df_states_id, combo_df, combo_df_states


def get_color(properties, field):
    cmap = ColorMap('Blues', alpha=255, levels=40)
    return cmap.to_color(properties[field], maxvalue=50, scale='lin')


def remove_states(dataset, df, df_1, missing_states_id):
    """This function removes the missing states and adds in new data properties"""
    # Removing the missing states from the json file, also renaming the state ID to abv
    datetime_cols = ['debtfree', 'effectivemwpa', 'earnings', 'wills', 'soletrader']  # columns to turn into datetime
    for element in reversed(dataset['features']):
        element['state'] = df_1.iloc[element['id'], :][1]  # Changing the state's id to abv
        add_df = df[df['state_id'] == element['id']]
        if element['state'] in missing_states_id:  # If the state is in that change list, remove it
            dataset['features'].remove(element)
        else:
            for i in add_df:
                element['properties'][i] = add_df[i][0]

    # Reformating Nan and years
    for element in dataset['features']:
        for i in element['properties']:
            if i in datetime_cols:
                if np.isnan(element['properties'][i]):
                    element['properties'][i] = 'No Data'
                else:
                    element['properties'][i] = int(element['properties'][i])  # Turning it into Year from float
    return dataset


# @interact(Value=options)
# def slider(Value=options[0]):
#     print(Value)


def main():
    """Runs the main data"""
    dataset, GEO_states = JSON_Fun()
    df_1, df, df_states = CSV_Fun()

    # Checking Number of states showing difference
    print("\nNumber of Geo states", len(GEO_states))
    print("Number of df states", len(df_states))

    # Finding Missing States
    missing_states_id = np.setdiff1d(GEO_states, df_states).tolist()
    print("\nMissing States ID", missing_states_id)
    print(df_1[df_1['state_id'].isin(missing_states_id)])
    list = df_1[df_1['state_id'].isin(missing_states_id)]
    missing_states_id = list['state'].tolist()

    # Sending off Data to add properties and remove missing states
    dataset = remove_states(dataset, df, df_1, missing_states_id)

    # Place the dataset into a GeoPanda Convert to String like object then dump json
    dataset = gpd.GeoDataFrame.from_features(dataset["features"])
    json_data = json.dumps(json.loads(dataset.to_json()))
    geosource = GeoJSONDataSource(geojson=json_data)

    # Adding Colors for graph
    # palette = gray(100)
    palette = viridis(100)
    palette = palette[::-1]  # This inverses the colors

    low_year = 1835
    high_year = 1890

    color_mapper = LinearColorMapper(palette=palette, low=low_year, high=high_year, nan_color='white')

    # Create color bar.
    color_bar = ColorBar(color_mapper=color_mapper,
                         label_standoff=8,
                         width=500, height=20,
                         border_line_color=None,
                         location=(0, 0),
                         orientation='horizontal')

    # Creating initial figure
    p = figure(title='Will Need to place title here',
               plot_height=600,
               plot_width=950,
               toolbar_location='below',
               tools='pan, wheel_zoom, box_zoom, reset')

    # Hiding grid lines
    p.xgrid.grid_line_color = None
    p.ygrid.grid_line_color = None

    # Add patch renderer to figure.
    states = p.patches('xs', 'ys', source=geosource,
                       fill_color={'field': 'debtfree', 'transform': color_mapper},
                       line_color='grey',
                       line_width=0.25,
                       fill_alpha=1)

    # Create hover tool
    p.add_tools(HoverTool(renderers=[states],
                          tooltips=[('State', '@NAME'),
                                    ('Population', '@POPESTIMATE2018')]))

    # Add Color Bar
    p.add_layout(color_bar, 'below')
    p.add_tools()
    # ic(dataset.columns[6::])
    # creating a dropdown
    options = ['option1', 'option1', 'option1', 'option1']

    menu = [("Item 1", "item_1"), ("Item 2", "item_2"), ("Item 3", "item_3")]
    dropdown = Dropdown(label="Dropdown button", button_type="warning", menu=menu)
    dropdown.js_on_event("menu_item_click", CustomJS(code="console.log('dropdown: ' + this.item, this.toString())"))

    #Addubg defaykt case
    ms_default = 'BASE'
    dfk_filt = dfk.query('mol_spe')


    show(column(p,dropdown)


if __name__ == '__main__':
    main()
