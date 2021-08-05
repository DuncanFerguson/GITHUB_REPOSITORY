# Student: Duncan Ferguson
# Student Id: 871641260
# Class: Comp 4433
# Assignment: Assignment 4
# Date 8/6/2021

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
from bokeh.io import curdoc, output_notebook
from bokeh.models import Slider, HoverTool
from bokeh.layouts import widgetbox, row, column
from bokeh.palettes import brewer
from bokeh.io import output_notebook, show, output_file
from bokeh.plotting import figure
from bokeh.models import GeoJSONDataSource, LinearColorMapper, ColorBar

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


def get_color(properties):
    cmap = ColorMap('Blues', alpha=255, levels=40)
    return cmap.to_color(properties['fips'], maxvalue=50, scale='lin')


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

    # Removing the missing states from the json file, also renaming the state ID to abv
    for element in reversed(dataset['features']):
        element['state'] = df_1.iloc[element['id'], :][1]  # Changing the state's id to abv
        add_df = df[df['state_id'] == element['id']]
        if element['state'] in missing_states_id:  # If the state is in that change list, remove it
            dataset['features'].remove(element)
        else:
            for i in add_df:
                element['properties'][i] = add_df[i][0]

    # Place the dataset into a GeoPanda
    dataset = gpd.GeoDataFrame(dataset)
    dataset = gpd.GeoDataFrame.from_features(dataset["features"])
    ic(dataset.head())

    # TODO REWRITE EVERYTHING BELOW HERE
    merged_json = json.loads(dataset.to_json())
    # Convert to String like object.
    json_data = json.dumps(merged_json)

    # Input GeoJSON source that contains features for plotting.
    geosource = GeoJSONDataSource(geojson=json_data)  # Define a sequential multi-hue color palette.
    palette = brewer['YlGnBu'][8]  # Reverse color order so that dark blue is highest obesity.
    palette = palette[::-1]  # Instantiate LinearColorMapper that linearly maps numbers in a range, into a sequence of colors.
    color_mapper = LinearColorMapper(palette=palette, low=0, high=40)  # Define custom tick labels for color bar.
    tick_labels = {'0': '0%', '5': '5%', '10': '10%', '15': '15%', '20': '20%', '25': '25%', '30': '30%', '35': '35%',
                   '40': '>40%'}  # Create color bar.
    color_bar = ColorBar(color_mapper=color_mapper, label_standoff=8, width=500, height=20,
                         border_line_color=None, location=(0, 0), orientation='horizontal',
                         major_label_overrides=tick_labels)  # Create figure object.
    p = figure(title='Look at US Population Metrics', plot_height=600, plot_width=950, toolbar_location=None)
    p.xgrid.grid_line_color = None
    p.ygrid.grid_line_color = None  # Add patch renderer to figure.
    p.patches('xs', 'ys', source=geosource, fill_color={'field': 'fips', 'transform': color_mapper},
              line_color='black', line_width=0.25, fill_alpha=1)  # Specify figure layout.
    # p.add_layout(color_bar, 'below')  # Display figure inline in Jupyter Notebook.
    # output_notebook()  # Display figure.
    show(p)




    # TODO the start of adding Data Color
    # geoplotlib.geojson(dataset, fill=True, color=get_color)
    # geoplotlib.geojson(dataset, fill=False, color=[255, 255, 255, 255])  # Filling in the lines as whites
    # geoplotlib.labels(dataset, , color=[0, 0, 225, 255], font_size=15, anchor_x='center')
    # geoplotlib.set_bbox(BoundingBox.USA)
    # geoplotlib.tiles_provider('toner-lite')  # Great for gray scale printing
    # geoplotlib.show()

    # json_data = json.dumps(dataset)
    # print(json_data)
    # merged_json = json.loads(dataset)
    # print(type(merged_json))
    # geosource = GeoJSONDataSource(geojson = dataset)



if __name__ == '__main__':
    main()
