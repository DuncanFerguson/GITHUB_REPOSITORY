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

Missing data are of particular interest in
that when a state has never achieved a given milestone, that should be indicated in a
standout manner such as cross-hatching.

Consider that the publication may be
grayscale. Provide a solution for that as well. Provide the titles, labels, and legends
necessary for clarification. File support is given as follows: SturmCodebook has the
explanation. SturmData is the data CSV."""

import json
import geoplotlib
from geoplotlib.colors import ColorMap
from geoplotlib.utils import BoundingBox

# file = 'National_Obesity_By_State.geojson'
file = 'states_geo.json'

# displaying one of the entries for the states
with open(file) as data:
    dataset = json.load(data)
    first_state = dataset.get('features')[0]
    # only showing one coordinate instead of all points
    first_state['geometry']['coordinates'] = first_state['geometry']['coordinates'][0][0]
    print(json.dumps(first_state, indent=4))

# listing the states in the dataset
with open(file) as data:
    dataset = json.load(data)
    states = [feature['id'] for feature in dataset.get('features')]
    print(states)


# plotting the information from the geojson file
# geoplotlib.geojson(file)
# geoplotlib.show()



