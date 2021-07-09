# Group: Alison, Jared, Hamza and Duncan
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

rain_central_park_df = pd.read_csv("Rain-Central Park.csv")
rain_central_park_df['DATE'] = pd.to_datetime(rain_central_park_df['DATE'])
rain_central_park_df['Weekday'] = rain_central_park_df['DATE'].dt.weekday
rain_central_park_df['Month'] = rain_central_park_df['DATE'].dt.month
rain_central_park_df['Year'] = rain_central_park_df['DATE'].dt.year
rain_central_park_df['Rainy Days'] = np.where(rain_central_park_df['PRCP (in)'], 1, 0)  # 1 for rainy day
rain_central_park_df['Week_End'] = np.where(rain_central_park_df.Weekday > 4, 1, 0)  # 1 for weekend

sns.boxplot(x=rain_central_park_df.Weekday,
            y=rain_central_park_df['PRCP (in)']).set_title("Box Plot of Rain over The week")

plt.show()

sns.boxplot(x=rain_central_park_df.Week_End,
            y=rain_central_park_df['PRCP (in)']).set_title("Box Plot of Rain over Weekday v Weekday")
plt.show()


print(rain_central_park_df.head())



