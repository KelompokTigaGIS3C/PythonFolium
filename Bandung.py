import folium

k = folium.Map(
    location=[-6.915188, 107.616022],
    zoom_start=12,
    tiles='Stamen Terrain'
)

tooltip = 'Click me!'
    
folium.Marker([-6.969774, 107.682983], popup='<i>Tegalluar Bojongsoang, Bandung, West Java</i>').add_to(k)
folium.Marker([-6.966957, 107.686105], popup='<i>Derwati Rancasari, Bandung City, West Java</i>').add_to(k)
folium.Marker([-6.968044, 107.688031], popup='<i>Rancabolang Gedebage, Bandung City, West Java</i>').add_to(k)
folium.Marker([-6.903444, 107.554920], popup='<i>Cibeureum South Cimahi, Cimahi City, West Java</i>').add_to(k)
folium.Marker([-6.903956, 107.658776], popup='<i>Cicaheum Kiaracondong, Bandung City, West Java</i>').add_to(k)
folium.Marker([-6.847544, 107.536381], popup='<i>Cipageran North Cimahi, Cimahi City, West Java</i>').add_to(k)
folium.Marker([-6.824876, 107.619980], popup='<i>Lembang West Bandung Regency, West Java</i>').add_to(k)
folium.Marker([-6.822489, 107.551487], popup='<i>Jambudipa Cisarua, West Bandung Regency, West Java</i>').add_to(k)
folium.Marker([-6.866462, 107.668732], popup='<i>Cimenyan Bandung, West Java</i>').add_to(k)
folium.Marker([-6.911113, 107.711304], popup='<i>Pasanggrahan Ujung Berung, Bandung City, West Java</i>').add_to(k)