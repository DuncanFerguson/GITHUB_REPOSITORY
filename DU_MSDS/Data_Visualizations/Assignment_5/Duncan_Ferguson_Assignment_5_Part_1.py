# Student: Duncan Ferguson
# Student Id: 871641260
# Class: Comp 4433
# Assignment: Assignment 5 Part 1
# Date 8/23/2021

"""Using the files capitals_lat_long.csv, form a DataFrame,
and write out an HTML file that when rendered in a browser displays marker for each capital city"""

import folium
import pandas as pd

# Importing the CSV file capitals_lat_long.csv
df = pd.read_csv('capitals_lat_long.csv')

# Printing off head of csv
print(df.head())

center = [0, 0]
map = folium.Map(location=center,
                 tiles='stamenterrain',
                 zoom_start=3)

for index, row in df.iterrows():
    folium.Marker([row['Latitude'], row['Longitude']],
                  popup=row['Country']+": "+row['Capital'],
                  icon=folium.Icon(icon_color='white')).add_to(map)

map.save('World_Capitals_Assignment_5_Part_1.html')