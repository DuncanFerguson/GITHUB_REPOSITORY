import pandas as pd
import folium
from folium.plugins import StripePattern
import geopandas as gpd
import numpy as np
import requests
from shapely.geometry import shape

# # Next we import the data.
# df = pd.read_csv("StrumData.csv")
#
# # We grab the state and wills column
# df = df[["state","wills"]]
# print(df.head())
#
# # We check how many rows we have and the types of our data.
# df.info()
#
# # We import the geoJSON file.
# url = ("https://raw.githubusercontent.com/python-visualization/folium/master/examples/data")
# state_geo = f"{url}/us-states.json"
#
#
# # We read the file and print it.
#
# print(type(state_geo))
# print(state_geo)
# geoJSON_df = gpd.read_file(state_geo)
# # geoJSON_df.head()

import requests
import geopandas as gpd
from shapely.geometry import shape

r = requests.get("https://data.cityofnewyork.us/resource/5rqd-h5ci.json")
r.raise_for_status()

data = r.json()
for d in data:
    d['the_geom'] = shape(d['the_geom'])

gdf = gpd.GeoDataFrame(data).set_geometry('the_geom')
print(gdf.head())
