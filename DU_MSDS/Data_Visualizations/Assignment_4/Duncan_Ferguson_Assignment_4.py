# Student: Duncan Ferguson
# Student Id: 871641260
# Class: Comp 4433
# Assignment: Assignment 4
# Date 8/6/2021

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

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import geoplotlib
import numpy as np
import folium

from shapely.geometry import Polygon, MultiPolygon
p1 = Polygon( [ (0,0), (3,4), (6,0) ] )
p2 = Polygon( [ (0,0), (3,-4), (6,0) ] )
p3 = Polygon( [ (0,0), (-3,4), (-6,0) ] )
m1=MultiPolygon([ p1, p2, p3 ])
print(m1.geom_type) # MultiPolygon
print(m1.length, m1.area) # 48, 36

import json
with open('states_geo.json') as json_data:
    print(type(json_data))
    d = json.load(json_data)
    print(type(d))
    print(d['type'])
    print(d['features'][0]['geometry']['coordinates'][0][0:10])



# df = pd.read_csv('StrumData.csv')

# Looking at the head
# print(df.head())
# df.info()
# print(df['icpsr'])

# TODO Displaying heatmap of null values
# sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
# plt.title("Heatmap of the null values for all numeric columns")
# plt.tight_layout()
# plt.show()

# Displaying a map
# map = folium.Map()
# map.show()