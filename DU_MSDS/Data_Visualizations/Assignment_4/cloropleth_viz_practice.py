import json
import geoplotlib
from geoplotlib.colors import ColorMap
from geoplotlib.utils import BoundingBox

with open("National_Obesity_By_State.geojson") as data:
    dataset = json.load(data)
    first_state = dataset.get('features')[0]
    first_state['geometry']['coordinates'] = first_state['geometry']['coordinates'][0][0]
    states = [feature['properties']['NAME'] for feature in dataset. get('features')]
    print(states)
    print(json.dumps(first_state, indent=4))
    geoplotlib.geojson('National_Obesity_By_State.geojson')
    geoplotlib.show()
# geoplotlib.geojson('National_Obesity_By_State.geojson')
# geoplotlib.show()