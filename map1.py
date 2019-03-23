import folium
map = folium.Map(location=[-33.92, 18.53], zoom_start=12, tiles="Stamen Toner")

fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[-33.91, 18.53], popup="Hi I am a Marker", icon=folium.Icon(color='green')))
map.add_child(fg)

map.save("Map1.html")
