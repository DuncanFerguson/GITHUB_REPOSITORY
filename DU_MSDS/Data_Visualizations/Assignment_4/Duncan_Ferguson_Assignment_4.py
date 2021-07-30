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
    print("Geo States", GEO_states)

# Importing the sample geoJSON_df
df = pd.read_csv('StrumData.csv')

# Grabbing States and wills column
df = df[["state", "wills"]]
df.head()

# Grabbing states from DF
df_states = df[["state"]].values.tolist()
print("DF States", df_states)

# We check how many rows we have and the types of our geoJSON_df
df.info()

# Checking Number of states showing difference
print("Number of Geo states", len(GEO_states))
print("Number of df states", len(df["state"].unique()))

# Finding the missing states
missing_states = np.setdiff1d(GEO_states, df_states)
print(missing_states)

# Finding the difference


# plotting the information from the geojson file
# TODO uncomment below to show file
# geoplotlib.geojson(file)
# geoplotlib.show()

