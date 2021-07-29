import

df_states= gpd.read_file('states_geo.json')
np.random.seed(51)
randy=pd.Series(np.random.rand(50))
df_states['randy']=randy
print(df_states.head(50))
geoplot.choropleth(
 df_states, hue=df_states['randy'],
 cmap='viridis', figsize=(15, 8))
plt.tight_layout()
plt.show()

