# Import geopandas package
import geopandas as gpd
import json
import pandas as pd
import numpy as np

# Importing the JSON data set
file = 'states_geo.json'
file2 = 'StrumData.csv'
file3 = 'states_id.csv'

# Importing the JSON File
with open(file) as geoJSON_df:
    dataset = json.load(geoJSON_df)

# Importing the Strum Dataset
with open(file2) as strum:
    df_2 = pd.read_csv(strum)

# Importing the State IDs
with open(file3) as state_id:
    df_3 = pd.read_csv(file3, usecols=[0, 1], names=["state_id", "state"], header=None, sep=',"\t')
    df_3['state'] = df_3['state'].str.strip('"')

# Merging Data Sets and finding Missing States
strum_w_id = df_2.merge(df_3, left_on='state', right_on='state')  # Merged Data Set
missing_states = np.setdiff1d(df_3['state'].to_list(), strum_w_id['state'].to_list()).tolist()  # Missing States

# Removing Missing states from the JSON file
for element in reversed(dataset['features']):
    element['state'] = df_3.iloc[element['id'], :][1]  # Changing the state's id to abv
    if element['state'] in missing_states:  # If the state is in that change list, remove it
        dataset['features'].remove(element)  # Removing states that are in the data list

# Turning JSON dataset into Geopanda
j_dataset = gpd.GeoDataFrame.from_features(dataset["features"])


# print("Missing States", missing_states)
# print(strum_w_id.head())
# print(j_dataset.head())

