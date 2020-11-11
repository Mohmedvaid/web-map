import folium
import pandas

# accessing txt
data = pandas.read_csv("Volcanoes_USA.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

# color generator
def color_generator(elevation):
    if elevation < 1000:
        return "green"
    elif elevation < 3000:
        return 'orange'
    
    # if greater than 300
    return 'red'


# creating map
map = folium.Map(location=[38, -99], zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

# adding marker
for lt, lg, el in zip(lat, lon, elev):
    map.add_child(folium.CircleMarker(location=[lt, lg], radius=6, popup=str(el)+" m", fill_color=color_generator(el), color='grey', fill_opacity=0.7))

# generating html
map.add_child(fg)
map.save("Map1.html")
