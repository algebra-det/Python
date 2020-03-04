from folium import *

# Initializing Map
map = Map(location=[28.339080, 77.319134], zoom_start=7, title="Mapbox Bright")

# Taking a variable for Tooltip
tooltip = "Click Me!"

# Defining a Marker
map.add_child(Marker(location=[28.539080, 77.319134], popup="<i>Pochinki</i>", tooltip="click to know more", icon=Icon(color='blue')))

# Anothere way of marking - in here we can enable the whole set with map.add_child(fg)
#If map.add_child(fg) is not written this whole fg won't work
fg = FeatureGroup(name="My Map")
fg.add_child(Marker(location=[28.739080, 77.319134], popup="<b>Bootcamp</b>", icon=Icon(color="green"),tooltip=tooltip))
fg.add_child(Marker(location=[28.939080, 77.319134], popup="<b>Bootcamp</b>", icon=Icon(color="green"),tooltip=tooltip))
fg.add_child(Marker(location=[28.139080, 77.319134], popup="<b>Bootcamp</b>", icon=Icon(color="green"),tooltip=tooltip))
map.add_child(fg)

# One more way of marking
Marker([28.739080, 77.519134], popup="Camp Alpha", icon=Icon(color="red"), tooltip="CLICK").add_to(map)

# defining click to mark function
map.add_child(ClickForMarker(popup="Waypoint Bro"))

# defining latitude/longitude popovers
#map.add_child(LatLngPopup())

map.save("Mapping.Html")
