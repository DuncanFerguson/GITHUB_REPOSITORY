import json
import geoplotlib
from geoplotlib.colors import ColorMap
from geoplotlib.utils import BoundingBox

# file = 'National_Obesity_By_State.geojson'
file = 'states_geo.json'

# displaying one of the entries for the states
with open(file) as data:
    dataset = json.load(data)
    first_state = dataset.get('features')[0]
    # only showing one coordinate instead of all points
    first_state['geometry']['coordinates'] = first_state['geometry']['coordinates'][0][0]
    print(json.dumps(first_state, indent=4))

# listing the states in the dataset
# with open(file) as data:
#     dataset = json.load(data)
#     states = [feature['properties']['NAME'] for feature in dataset.get('features')]
#     print(states)


# plotting the information from the geojson file
geoplotlib.geojson(file)
geoplotlib.show()