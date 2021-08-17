# Student: Duncan Ferguson
# Student Id: 871641260
# Class: Comp 4433
# Assignment: Assignment 5 Part 3
# Date 8/23/2021

""" Estimate the boundaries for Kansas (use just four lat-long points) and Nebraska (use just six points)
Construct a GeoJSON file from that. Then write a Python program to read that file, form a dictionary,
and plot the results"""

from geojson import Point, Feature, FeatureCollection, dump
from shapely.geometry import Point, Polygon

# Kansas in 4 lat-long points
NW_KA = Point((40.00581067533721, -102.0528170631371))
NE_KA = Point((39.99893185672504, -94.61847649961597))
SW_KA = Point((36.993067, -102.042071))
SE_KA = Point((36.99891776893816, -94.6179717441199))

# Nebraska in 4 lat-long points
# NW_NE = [43.0008807956697, -104.05310504007869]
# SW_NE_1 = [41.01237134482985, -104.05578499832443]
# SW_NE_2 = [41.00428887544674, -102.06029885056343]
# SW_NE_3 = [40.01000231641949, -102.04773884001962]
# SE_NE = [40.01894547099799, -95.3193142525115]
# NE_NE = [42.936541272131834, -96.53327113679717]

# Creating GeoJSON
features = []
features.append(Feature(geometry=[NW_KA, NE_KA, SE_KA, SW_KA], properties={'state':'Kansas'}))
feature_collection = FeatureCollection(features)

with open('Duncan_Ferguson_Assignment_5_Part_3.geojson', 'w') as f:
    dump(feature_collection, f)
