import json
import geoplotlib
from geoplotlib.colors import ColorMap
from geoplotlib.layers import BaseLayer
from geoplotlib.core import BatchPainter
from geoplotlib.colors import colorbrewer
from geoplotlib.utils import epoch_to_str, BoundingBox, DataAccessObject


import pandas as pd
import icecream as ic
from datetime import datetime

class TrackLayer(BaseLayer):
    def __init__(self, dataset,bbox=BoundingBox.WORLD):
        self.data = dataset
        self.cmap = colorbrewer(self.data['hex_ident'], alpha=200)
        self.time = self.data['timestamp'].min()
        self.painter = BatchPainter()
        self.view = bbox

    def draw(self, proj, mouse_x, mouse_y, ui_manager):
        self.painter = BatchPainter()
        df = self.data.where((self.data['timestamp'] > self.time) & (self.data['timestamp'] <= self.time +180))
        for element in set(df['hex_ident']):
            grp = df.where(df['hex_ident'] == element)
            self.painter.set_color(self.cmap[element])
            x, y = proj.lonlat_toscreen(grp['lon'], grp['lat'])
            self.painter.points(x, y, 15, rounded=True)
        self.time += 1
        if self.time > self.data['timestamp'].max():
            self.time = self.data['timestamp'].min()
        self.painter.batch_draw()
        ui_manager.info('Current timestamp: {}'.format(epoch_to_str(self.time)))

    def bbox(self):
        return self.view

def to_epoch(date, time):
    try:
        timestamp = round(datetime.strptime('{}{}'.format(date,time), '%Y/%m/%d %H:%M:%S.%f').timestamp())
        return timestamp
    except ValueError:
        return round(datetime.strptime('2017/09/11 17:02:06.418', '%Y/%m/%d %H:%M:%S.%f').timestamp())



# file = 'National_Obesity_By_State.geojson'
file = 'flight_tracking.csv'

dataset = pd.read_csv(file)
print(dataset.head())
print(type(dataset))

dataset = dataset.rename(index=str, columns={'latitude': "lat", 'longitude': 'lon'})

# Creating a new column called timestamp with the to_epoch method applied
dataset['timestamp'] = dataset.apply(lambda x: to_epoch(x['date'], x['time']), axis=1)

leeds_bbox = BoundingBox(north=53.8074, west=-3, south=53.7074, east=0)

data = DataAccessObject(dataset)
geoplotlib.add_layer(TrackLayer(data,bbox=leeds_bbox))
geoplotlib.show()

print(dataset.head())

# with open(file) as data:
#     dataset = json.load(data)
#     first_state = dataset.get('features')[0]
#     first_state['geometry']['coordinates'] = first_state['geometry']['coordinates'][0][0]
#     print(json.dumps(first_state, indent=4))

# with open(file) as data:
#     dataset = json.load(data)
#     states = [feature['properties']['NAME'] for feature in dataset.get('features')]
#     print(states)
#
# def get_color(properties):
#     return cmap.to_color(properties['Obesity'], maxvalue=40, scale='lin')
#
# cmap = ColorMap('Blues', alpha=255, levels=40)
#
# geoplotlib.geojson(dataset, fill=True, color=get_color)  # Adding Color to the obesity from get color
# geoplotlib.geojson(dataset, fill=False, color=[255, 255, 255, 255])  # Filling in the lines as whites
# geoplotlib.set_bbox(BoundingBox.USA)
# geoplotlib.tiles_provider('darkmatter')
# geoplotlib.tiles_provider({
#     'url':lambda zoom, xtile, ytile:
#     'http://a.tile.stamen.com/watercolor/%d/%d/%d.png' % (zoom, xtile, ytile),
#     'tiles_dir':'tiles_dir',
#     'attribution':'Python Data Visualization | Packt'
# })

# geoplotlib.tiles_provider('toner-lite')  # Will want to use this for the gray scale printing
# geoplotlib.show()


