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
        return "orange"

    # if greater than 300
    return "red"


# creating map
map = folium.Map(location=[38, -99], zoom_start=6, tiles="Stamen Terrain")
fgv = folium.FeatureGroup(name="Volcanoes")

# adding marker
for lt, lg, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, lg], radius=6, popup=str(
        el)+" m", fill_color=color_generator(el), color="grey", fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(
    data=open("world.json", "r", encoding="utf-8-sig").read(),
    style_function=lambda x: {"fillColor":"green" if x["properties"]["POP2005"] <= 10_000_000 
    else "orange" if x["properties"]["POP2005"] <= 20_000_000 else "red"}
    ))

# generating html
map.add_child(fgv)
map.add_child(fgp)
# adding layer swith: on/off
map.add_child(folium.LayerControl())

map.save("index.html")
