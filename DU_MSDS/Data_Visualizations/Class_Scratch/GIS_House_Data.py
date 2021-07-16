!conda install -c conda-forge folium=0.5.0 --yes

import pandas as pd
import folium
import webbrowser

latitude = 37.0902
longitude = -95.7129
traffic_map = folium.Map(location=[latitude, longitude], zoom_start=5)


# house_data = pd.read_csv("house_data.csv")
# # print(house_data)
# columns = list(house_data.columns.values)
#
# # house_data.info()
# # Cleaning up the time
#
# hd_list = house_data['date'].to_list()
# for i in enumerate(hd_list):
#     hd_list[i[0]] = i[1][:8]
# house_data['date'] = hd_list
# house_data['date'] = house_data['date'].astype('datetime64[ns]')

# print(house_data['date'])

# Break down for getting it into months
# for time in house_data['date']:
#     print(time)
#     print(time[:4], time[4:6], time[6:8])


