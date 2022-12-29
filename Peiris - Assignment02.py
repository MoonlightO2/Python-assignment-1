import folium
from folium.plugins import MarkerCluster
import pandas as pd
import webbrowser
import matplotlib.pyplot as plt
import time
start = time.process_time()

# Load data from CSV to Dataset "data"
data = pd.read_csv("GrowLocations.csv")
print("\nGrow Locations Dataset - Shape (Before cleaning)")
print(data.shape)

# Removing erroneous data
print("\nShow all erroneous data....")
print(data.isna().sum())
print("\nRemoving erroneous data....")
data = data.dropna(subset=['Serial'])
print("\nErroneous data removed....")
print("\nGrow Locations Dataset - First 5 rows")
print(data.head())
print("\nGrow Locations Dataset - Shape (After cleaning)")
print(data.shape)
print("\nGrow Locations Dataset - Data Types")
print(data.dtypes)

print("\nShow all unique types")
data = pd.DataFrame(data)
data.Type = data.Type.replace('Thingful.Connectors.GROWSensors.AirTemperature', 'Air Temperature')
data.Type = data.Type.replace('Thingful.Connectors.GROWSensors.BatteryLevel', 'Battery Level')
data.Type = data.Type.replace('Thingful.Connectors.GROWSensors.FertilizerLevel', 'Fertilizer Level')
data.Type = data.Type.replace('Thingful.Connectors.GROWSensors.Light', 'Light')
data.Type = data.Type.replace('Thingful.Connectors.GROWSensors.SoilMoisture', 'Soil Moisture')
data.Type = data.Type.replace('Thingful.Connectors.GROWSensors.WaterTankLevel', 'Water Tank Level')

# Adding Legend based on Type

"""
# Map image showing
plt.legend("map7.png")
plt.show()
"""
# print(data.Type.unique())
print(data['Type'].value_counts())

lat = data['Latitude']
lon = data['Longitude']
typ = data['Type']

# Create base map
map = folium.Map(location=[56.473763, -2.964372], zoom_start=4.5, tiles="openstreetmap")

# add tile layers
folium.TileLayer('openstreetmap').add_to(map)
folium.TileLayer('stamenterrain').add_to(map)
folium.TileLayer('stamentoner').add_to(map)
folium.TileLayer('stamenwatercolor').add_to(map)
folium.TileLayer('cartodbpositron').add_to(map)
folium.TileLayer('cartodbdark_matter').add_to(map)

# The following tile layers did not work
# folium.TileLayer('mapquestopen').add_to(map)
# folium.TileLayer('MapQuest Open Aerial').add_to(map)
# folium.TileLayer('Mapbox Bright').add_to(map)
# folium.TileLayer('Mapbox Control Room').add_to(map)

# add layers control over the map
folium.LayerControl().add_to(map)

"""
# To create clusters (I didn't like this feature so did not use it)
# markercluster = MarkerCluster().add_to(map)
"""

# Add all markers according to types (Types in different colors)
for lat, lon, typ in zip(lat, lon, typ):
    if typ == "Air Temperature":
        folium.CircleMarker(fill_color="blue", location=[lat, lon], radius=8, popup=str(typ), color="white", fill_opacity=0.9).add_to(map)
    elif typ == "Battery Level":
        folium.CircleMarker(fill_color="green", location=[lat, lon], radius=8, popup=str(typ), color="white", fill_opacity=0.9).add_to(map)
    elif typ == "Fertilizer Level":
        folium.CircleMarker(fill_color="red", location=[lat, lon], radius=8, popup=str(typ), color="white", fill_opacity=0.9).add_to(map)
    elif typ == "Light":
        folium.CircleMarker(fill_color="orange", location=[lat, lon], radius=8, popup=str(typ), color="white", fill_opacity=0.9).add_to(map)
    elif typ == "Soil Moisture":
        folium.CircleMarker(fill_color="brown", location=[lat, lon], radius=8, popup=str(typ), color="white", fill_opacity=0.9).add_to(map)
    elif typ == "Water Tank Level":
        folium.CircleMarker(fill_color="purple", location=[lat, lon], radius=8, popup=str(typ), color="white", fill_opacity=0.9).add_to(map)

title_html = '''
<div style="position: fixed; bottom: 50px; left: 50px; width: 250px; height: 30px; z-index:9999; font-family: Tahoma; font-size:20px; font-weight: bold; color:black">&nbsp; Grow Locations UK
</div>
'''

map.get_root().html.add_child(folium.Element(title_html))
print("\nSaving map....")
map.save("Grow Locations UK.html")
print("\nLoading map....", time.process_time() - start)
webbrowser.open_new_tab("Grow Locations UK.html")
print("\nMap loaded successfully....")
print("\n\nTotal time taken: ", time.process_time() - start)
