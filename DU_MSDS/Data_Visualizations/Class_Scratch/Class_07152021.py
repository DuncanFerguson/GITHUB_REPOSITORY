import pandas as pd
# import matplotlib
# import seaborn as sns
# import matplotlib.pyplot as plt
# import numpy as np
# from matplotlib.colors import ListedColormap
# from datetime import datetime
import folium


house_data = pd.read_csv("house_data.csv")
print(house_data.head())
# print(list(house_data.columns.values))

# # cmap = ListedColormap(sns.color_palette("muted", ncolors=5))
# plt.scatter(house_data['price'], house_data['grade'])
# plt.xlabel("Price")
# plt.ylabel("Grade")
# plt.show()

# hs = sns.load_dataset(house_data)
#
# g = sns.factorplot('price', 'bedrooms', 'sqft_lot', data=house_data, kind='bar', size=6, pallete='muted', legend=False)
# g.dispin(left=True)
# plt.legend(loc='upper left')
# g.setylabels('bedrooms')
#
# plt.show()
# Price and sqft_lot15
#


# fix, ax = plt.subplots()
# ax.set(xscale='log', yscale='log')
#
# sns.regplot(house_data['price'], house_data['bedrooms'], house_data, ax=ax, scatter_kws={'s': 100}, fit_reg=True)
# plt.show()

# g = sns.FacetGrid(house_data, row='price', col='bedrooms')
# g.map(plt.hist, 'sqft_lot')
# plt.tight_layout()
# plt.show()

#
# sns.boxplot(y='price', x='grade', data=house_data, showfliers=False)
#
# plt.show()
# house_data = house_data.sort_values(by=['waterfront'], ascending=True)
# sns.relplot(y='price', x='sqft_living', hue='waterfront', data=house_data, alpha=.5)
#
# plt.show()
#
#
# plt.show()
#
# columns = ['id', 'date', 'price', 'bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'waterfront', 'view', 'condition', 'grade',
#  'sqft_above', 'sqft_basement', 'yr_built', 'yr_renovated', 'zipcode', 'lat', 'long', 'sqft_living15', 'sqft_lot15']
#
#
#
# print(house_data['condition'])

# This is a bad as plot
# mpg = sns.load_dataset("mpg")
# mpg.head()
#
# ## Scatterplot with varying point sizes and hues
#
# # Plot miles per gallon against horsepower with other semantics
# sns.relplot(x="horsepower", y="mpg", hue="origin", size="weight",
#             sizes=(40, 400), alpha=.5, palette="muted",
#             height=6, data=mpg)
#
# fig, ax = plt.subplots()
#
# # Load in data
# tips = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv")
#
# # Create violinplot
# ax.violinplot(tips["total_bill"], vert=False)
#
# # Show the plot
# plt.show()

## New eamples

# import pandas as pd
# xlat=[40, 30, 20, 10, 0, -10]
# xlon=[-105, -100, -90, -100, -108, -80]
# df = pd.DataFrame({'Lat': xlat, 'Lon': xlon})
# clist=[]
# for i in range(len(df)):
#  clist.append([df.iloc[i]['Lat'], df.iloc[i]['Lon']])
# print(clist)
# import folium
# map=folium.Map(location=[39.7,-105], zoom_start=6) # Denver
# for c in clist:
#  map.add_child(folium.Marker(location=c,popup="Site is here",
#  icon=folium.Icon(color='blue')))
# map.save("Map.html")


# Now point browser at that file