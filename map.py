import folium
import pandas
map = folium.Map(location=[28 , 78] , tiles="Stamen Terrain",zoom_start=6) 

fg = folium.FeatureGroup(name = "my map" )

data= pandas.read_csv("IndianSites.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
title = list(data["Title"])
name  = list(data["Title"]) 


html = """
Site Name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
 
"""



for lt , ln  , ti ,na in zip(lat , lon , title , name):
        iframe = folium.IFrame(html=html % (na , ti), width=200, height=100)
        fg.add_child(folium.Marker(location=[ln , lt] , popup=folium.Popup(iframe), icon=folium.Icon(color='green')))

map.add_child(fg)

map.save("India.html")
