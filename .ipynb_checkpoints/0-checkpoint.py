import folium

map = folium.Map(
    location = [-6.302386, 106.652290],
    zoom_start = 15
)
folium.Marker(
    [-6.302386, 106.652290],
    popup= '<b>Purwadhika</b>',
    tooltip = 'I\'m here!'
).add_to(map)

map.save('0.html')