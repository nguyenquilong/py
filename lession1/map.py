import folium
import pandas as pd

data = pd.read_csv('Volcanoes.txt')
print(data)
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

map = folium.Map(location=[48,-121.8109970], tiles="OpenStreetMap", zoom_start=5)
#map.save("map1.html")

fg = folium.FeatureGroup('Map test')    
for lat, lon , elev in zip(lat, lon, elev):
    fg.add_child(folium.Marker(location=[lat, lon], popup=elev, icon=folium.Icon(color="blue")))

map.add_child(fg)
map.save("map1.html")