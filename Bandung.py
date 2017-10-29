import folium
m = folium.Map(
    location=[-6.917418, 107.619465],
    zoom_start=12,
    tiles='Stamen Terrain'
)
tooltip = 'Click me!'
folium.Marker([-6.871369, 107.573665], popup='<i>POLBAN</i>').add_to(m)
folium.Marker([-6.873206, 107.575965], popup='<i>Politeknik Pos Indonesia</i>').add_to(m)
folium.Marker([-6.878085, 107.573909], popup='<i>SMAN 15 Bandung</i>').add_to(m)
folium.Marker([-6.879619, 107.579284], popup='<i>SMK Pasundan 5 Bandung</i>').add_to(m)
folium.Marker([-6.885547, 107.580947], popup='<i>Universitas Kristen Maranatha</i>').add_to(m)
folium.Marker([-6.889348, 107.603676], popup='<i>SMA Negeri 2 Bandung</i>').add_to(m)
folium.Marker([-6.866352, 107.592781], popup='<i> Universitas Pasundan Bandung</i>').add_to(m)
folium.Marker([-6.868355, 107.594583], popup='<i> Sekolah Tinggi Pariwisata Bandung</i>').add_to(m)
folium.Marker([-6.861143, 107.592921], popup='<i> FPIPS Universitas Pendidikan Indonesia</i>').add_to(m)
folium.Marker([-6.891496, 107.610654], popup='<i> Institut Teknologi Bandung</i>').add_to(m)
folium.Marker([-6.874806, 107.605113], popup='<i> Universitas Katolik Parahyangan</i>').add_to(m)
folium.Marker([-6.898046, 107.644692], popup='<i> Universitas Widyatama</i>').add_to(m)
folium.Marker([-6.902606, 107.643690], popup='<i> Sekolah Menengah Atas Negeri 10 Bandung</i>').add_to(m)
folium.Marker([-6.900007, 107.642628], popup='<i> STIMIK Bandung</i>').add_to(m)
folium.Marker([-6.886823, 107.615287], popup='<i> Universitas Komputer Indonesia </i>').add_to(m)
folium.Marker([-6.926047, 107.774602], popup='<i> Universitas Padjadjaran </i>').add_to(m)
folium.Marker([-6.928475, 107.779475], popup='<i> SMA Negeri Jatinangor</i>').add_to(m)
folium.Marker([-6.931271, 107.717319], popup='<i> Universitas Islam Negeri Sunan Gn. Djati</i>').add_to(m)
 
folium.Marker([-6.903921, 107.607880], popup='<i> Universitas Islam Bandung </i>').add_to(m)
folium.Marker([-6.905070, 107.608312], popup='<i> Universitas Pasundan Kampus 2</i>').add_to(m)

m

