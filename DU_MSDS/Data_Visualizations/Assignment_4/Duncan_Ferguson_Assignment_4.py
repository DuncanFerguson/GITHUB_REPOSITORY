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
explanation. SturmData is the geoJSON_df CSV."""

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
from bokeh.models import GeoJSONDataSource, LinearColorMapper, ColorBar, CustomJS, Dropdown, Slider, HoverTool
from bokeh.models.widgets import Panel, Tabs
# Example of adding in a drop down
from bokeh.io import show
from ipywidgets import interact, interact_manual
from icecream import ic  # print tester

def JSON_Fun():
    """ Aimed at importing the JSON files"""
    # file = 'National_Obesity_By_State.geojson'
    file = 'states_geo.json'

    # displaying one of the entries for the states
    with open(file) as geoJSON_df:
        dataset = json.load(geoJSON_df)
        first_state = dataset.get('features')[0]
        # only showing one coordinate instead of all points
        first_state['geometry']['coordinates'] = first_state['geometry']['coordinates'][0][0]
        print(json.dumps(first_state, indent=4))

    # listing the states in the dataset
    with open(file) as geoJSON_df:
        dataset = json.load(geoJSON_df)
        GEO_states = [feature['id'] for feature in dataset.get('features')]

    # TODO Uncomment to display map
    # print(type(dataset))
    # geoplotlib.geojson(file)
    # geoplotlib.show()
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
    # print(combo_df.head())

    # TODO this is a spot to filter the columns
    # Grabbing States and wills column
    # df = df[["state", "wills"]]
    # df.head()

    # Grabbing states from DF
    combo_df_states = combo_df[["state_id"]].values.tolist()
    return df_states_id, combo_df, combo_df_states


def get_color(properties, field):
    cmap = ColorMap('Blues', alpha=255, levels=40)
    return cmap.to_color(properties[field], maxvalue=50, scale='lin')


def remove_states(dataset, df, df_1, missing_states_id):
    """This function removes the missing states and adds in new data properties"""
    # Removing the missing states from the json file, also renaming the state ID to abv
    datetime_cols = ['debtfree','effectivemwpa', 'earnings', 'wills', 'soletrader']  # columns to turn into datetime
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

# def update_plot(attr, old, new):
#     yr = slider.value
#     new_data = json_data(yr)
#     geosource.geojson = new_data
#     p.title.text = 'Share of adults who are obese, %d' %yr


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

    # Color Options
    # palette = gray(100)
    palette = viridis(100)
    palette = palette[::-1]  # This inverses the colors
    color_mapper = LinearColorMapper(palette=palette, low=0, high=100, nan_color='#000000')  # Define custom tick labels for color bar.

    p = figure(title='Look at US Earnings Metrics', plot_height=600, plot_width=950, toolbar_location=None)

    # Blanking out the grid lines
    p.xgrid.grid_line_color = None
    p.ygrid.grid_line_color = None

    # Define custom tick labels for color bar.
    tick_labels = {'0': '0%',
                   '20': '20%',
                   '40': '40%',
                   '60': '60%',
                   '80': '80%',
                   '100': '100%'}

    # hover = HoverTool(tooltips=[('Country/region', '@country'), ('% obesity', '@per_cent_obesity')])

    color_bar = ColorBar(color_mapper=color_mapper, label_standoff=8, width=500, height=20,
                         border_line_color=None, location=(0, 0), orientation='horizontal',
                         major_label_overrides=tick_labels)
    p.add_layout(color_bar, 'below')  # Adding Scale on the bottom

    # Patching together the map
    p.patches('xs', 'ys', source=geosource, fill_color={'field': 'earnings', 'transform': color_mapper},
              line_color='black', line_width=0.25, fill_alpha=1)  # Specify figure layout.

    # # Make a slider object: slider
    # slider = Slider(title='earnings', start=1975, end=2016, step=1, value=2016)
    # slider.on_change('value', update_plot)

    # Make a column layout of widgetbox(slider) and plot, and add it to the current document
    # layout = column(p, widgetbox(slider))
    # layout.add_root(layout)
    # show(column(p))

    # menu = [("Item 1", "item_1"), ("Item 2", "item_2"), None, ("Item 3", "item_3")]
    # dropdown = Dropdown(label="Dropdown button", button_type="warning", menu=menu)
    # dropdown.js_on_event("menu_item_click", CustomJS(code="console.log('dropdown: ' + this.item, this.toString())"))


    # # Displaying the graph and buttons
    # show(column(p))


if __name__ == '__main__':
    main()
