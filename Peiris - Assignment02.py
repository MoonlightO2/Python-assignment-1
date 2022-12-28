import folium
from folium.plugins import MarkerCluster
import pandas as pd
import webbrowser

# Load data
data = pd.read_csv("GrowLocations.csv")
lat = data['Latitude']
lon = data['Longitude']
typ = data['Type']

# Create a base map
map = folium.Map(location=[56.473763, -2.964372], zoom_start=4.5, tiles="openstreetmap")

# To create clusters
markercluster = MarkerCluster().add_to(map)

# Add all markers
for lat, lon, typ in zip(lat, lon, typ):
    folium.CircleMarker(location=[lat, lon], radius=8, popup=str(typ), fill_color="red", color="white", fill_opacity=0.9).add_to(map)

title_html = '''
                <div style="position: fixed; 
                            bottom: 50px; left: 50px; width: 300px; height: 30px; 
                            border:2px solid black; z-index:9999; font-size:16px; font-align:center;
                            color:white">&nbsp; Grow Locations UK
                </div>
                '''

map.get_root().html.add_child(folium.Element(title_html))
print("Saving map....")
map.save("Grow Locations UK.html")
print("Loading map....")
webbrowser.open_new_tab("Grow Locations UK.html")
print("Map loaded successfully....")
