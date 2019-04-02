import folium
import pandas as pd

data = pd.read_csv("Clinics_2018.csv")
lat = list(data["LAT"])
lon = list(data["LON"])
addr = list(data["ADR"])
name = list(data["NAME"])

"""
def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000<= elevation < 3000:
        return 'orange'
    else:
        return 'red'
"""
html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

map = folium.Map(location=[-33.918861, 18.423300], zoom_start=6, tiles="Stamen Toner")

"""
fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln, el, name in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius = 6, popup=folium.Popup(iframe), fill_color = color_producer(el), color = 'grey', fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 1000000
else 'orange' if 1000000 <=  x['properties']['POP2005'] < 50000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
"""
map.save("CPT_Clinics_html.html")
