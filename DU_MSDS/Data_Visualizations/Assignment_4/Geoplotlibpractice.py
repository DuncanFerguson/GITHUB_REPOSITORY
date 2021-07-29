import json
with open('states_geo.json') as json_data:
 print(type(json_data)) # _io.TextIOWrapper
 d=json.load(json_data)
 print(type(d)) # dictionary
 print(d['type'])
 print(d['features'][0]['geometry']['coordinates'][0][0:10])
with open('world.geojson') as json_data2:
 d2=json.load(json_data2)
 print(d2['type'])
 print(d2['features'][0]['geometry']['coordinates'][0][0:10])
 print(d2['features'][1]['geometry']['coordinates'][0][0:2][0:10])