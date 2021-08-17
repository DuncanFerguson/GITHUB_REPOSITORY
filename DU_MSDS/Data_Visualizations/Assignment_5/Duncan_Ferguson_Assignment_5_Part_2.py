# Student: Duncan Ferguson
# Student Id: 871641260
# Class: Comp 4433
# Assignment: Assignment 5 Part 2
# Date 8/23/2021

"""Estimate the latitude and longitude for three points of a triangle that would cover Africa or come close
(Hint: Rabat, Cape Town, and Mogadishu, for exampled) Use folium to demonstrate where the points are on the map
so that a person could see  at a glance that they do nearly cover Africa. Use Shapely to define a polygon
from those three points. Compute the area and perimeter of the triangle assuming flat earth and allowing each
degree of latitude and each degree of longitude to be considered one unit of length"""

import folium

rabat = [34.020882, -6.841650]
Cape_town = [-33.918861, 18.423300]
Mogadishu = [45.318161, 2.046934]