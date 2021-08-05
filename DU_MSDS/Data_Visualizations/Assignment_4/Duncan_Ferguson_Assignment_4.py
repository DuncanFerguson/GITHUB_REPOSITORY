# Student: Duncan Ferguson
# Student Id: 871641260
# Class: Comp 4433
# Assignment: Assignment 4
# Date 8/6/2021

# https://www.howtogeek.com/118594/how-to-edit-your-system-path-for-easy-command-line-access/
# https://geoffboeing.com/2014/09/using-geopandas-windows/
# https://towardsdatascience.com/how-to-step-up-your-folium-choropleth-map-skills-17cf6de7c6fe

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
import folium
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
        # print("Geo States", GEO_states)

    # TODO Uncomment to display map
    # ic(file)
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
                # TODO maybe add in the state name on this inside property
                print(add_df[i][0])
                if add_df[i][0] != 'nan':
                    element['properties'][i] = add_df[i][0]


    # To pring out the current data

    # Place the dataset into a GeoPanda
    # ic(dataset)
    # dataset = gpd.GeoDataFrame(dataset)
    # dataset = gpd.GeoDataFrame.from_features(dataset["features"])

    # TODO the start of adding Data Color
    geoplotlib.geojson(dataset, fill=True, color=get_color)
    # geoplotlib.geojson(dataset, fill=False, color=[255, 255, 255, 255])  # Filling in the lines as whites
    geoplotlib.set_bbox(BoundingBox.USA)
    geoplotlib.tiles_provider('toner-lite')  # Great for gray scale printing
    geoplotlib.show()



if __name__ == '__main__':
    main()
