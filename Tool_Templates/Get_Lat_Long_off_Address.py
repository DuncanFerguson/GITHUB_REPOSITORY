import pandas as pd
from geopy.geocoders import ArcGIS

addrs = ['2155 E Wesley Ave, Denver, CO 80208',
         '8500 Pena Blvd, Denver, CO 80249',
         '1600 Pennsylvania Ave NW, Washington, DC 20500']
nom = ArcGIS()
for addr in addrs:
    n = nom.geocode(addr)
    print(n)
    print(n.latitude)
    print(n.longitude)

df = pd.DataFrame({'Addr': addrs},
                  index=['DU-ECS', 'DEN', 'WHouse'])
df['Coord'] = df['Addr'].apply(nom.geocode)
df['Lat'] = df['Coord'].apply(lambda x: x.latitude)
df['Lon'] = df['Coord'].apply(lambda x: x.longitude)
df.drop('Coord', axis=1, inplace=True)
print(df)
