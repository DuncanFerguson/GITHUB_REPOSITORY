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
        # print(json.dumps(first_state, indent=4))

    # listing the states in the dataset
    with open(file) as geoJSON_df:
        dataset = json.load(geoJSON_df)
        GEO_states = [feature['id'] for feature in dataset.get('features')]
        # print("Geo States", GEO_states)

    # TODO Uncomment to display map
    # geoplotlib.geojson(file)
    # geoplotlib.show()
    return dataset, GEO_states

def CSV_Fun():
    """ Aimed at importing an aligning the CSV sheets"""
    # Importing the sample geoJSON_df
    df = pd.read_csv('StrumData.csv')
    # df_states_id = pd.read_csv('states_id.csv', sep='\t', names=["id", "state"])
    df_states_id = pd.read_csv('states_id.csv', usecols=[0, 1], names=["id", "state"], header=None, sep=',"\t')
    # df_states_id['state'] = df_states_id['state'].str.strip('"')


    print(df_states_id)

    # Grabbing States and wills column
    df = df[["state", "wills"]]
    # df.head()
    # Grabbing states from DF
    df_states = df[["state"]].values.tolist()
    df_states_index = df[["state"]].values.tolist()
    # print("DF States", df_states)
    # We check how many rows we have and the types of our geoJSON_df
    df.info()
    return df, df_states

def main():
    """Runs the main data"""
    dataset, GEO_states = JSON_Fun()
    df, df_states = CSV_Fun()

    # Checking Number of states showing difference
    # print("Number of Geo states", len(GEO_states))
    # print("Number of df states", len(df_states))


if __name__ == '__main__':
    main()
