
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import geoplotlib
import numpy as np
from geoplotlib.utils import read_csv
import folium

# import pandas as pd
# xlat=[40, 30, 20, 10, 0, -10]
# xlon=[-105, -100, -90, -100, -108, -80]
# df = pd.DataFrame({'Lat': xlat, 'Lon': xlon})
# clist=[]
# for i in range(len(df)):
#     clist.append([df.iloc[i]['Lat'], df.iloc[i]['Lon']])
# print(clist)
# import folium
# map=folium.Map(location=[39.7,-105], zoom_start=6) # Denver
# for c in clist:
#     map.add_child(folium.Marker(location=c,popup="Site is here",
#     icon=folium.Icon(color='blue')))
#
# map.save("Map_g3.html") # Now point browser at that file

# import pandas as pd
# from geopy.geocoders import ArcGIS
# addrs=['2155 E Wesley Ave, Denver, CO 80208',
#        '8500 Pena Blvd, Denver, CO 80249',
#        '1600 Pennsylvania Ave NW, Washington, DC 20500']
# nom=ArcGIS()
# for addr in addrs:
#     n=nom.geocode(addr)
#     print(n)
#     print(n.latitude)
#     print(n.longitude)
#
# df=pd.DataFrame({'Addr': addrs},
#                 index=['DU-ECS','DEN','WHouse'])
# df['Coord']=df['Addr'].apply(nom.geocode)
# df['Lat']=df['Coord'].apply(lambda x: x.latitude)
# df['Lon']=df['Coord'].apply(lambda x: x.longitude)
# df.drop('Coord', axis=1, inplace=True)
# print(df)