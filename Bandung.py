import folium

def marker (long, lat):
  m = folium.Map(
      location=[long, lat],
      zoom_start=12,
      tiles='Stamen Terrain')
  return m
  
def regularpolygon (long,lat):
  a = folium.Map(
      location=[long,lat],
      zoom_start=12,
      tiles='Stamen Toner')
  return a
      
def circle (long,lat):
  p = folium.Map(
      location=[long,lat],
      zoom_start=12,
      tiles='Stamen Terrain')
  return p
      
m = marker (-6.917418, 107.619465)
r = regularpolygon   (-6.917418, 107.619465)
c = circle   (-6.917418, 107.619465)
tooltip = 'Click me!'

folium.Marker([-6.871369, 107.573665], popup='<i> POLBAN</i>').add_to(m)
folium.Marker([-6.873206, 107.575965], popup='<i> Politeknik Pos Indonesia</i>').add_to(m)
folium.Marker([-6.878085, 107.573909], popup='<i> SMAN 15 Bandung</i>').add_to(m)
folium.Marker([-6.879619, 107.579284], popup='<i> SMK Pasundan 5 Bandung</i>').add_to(m)
folium.Marker([-6.885547, 107.580947], popup='<i> Universitas Kristen Maranatha</i>').add_to(m)
folium.Marker([-6.889348, 107.603676], popup='<i> SMA Negeri 2 Bandung</i>').add_to(m)
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

folium.Marker([-6.973314, 107.628806], popup='<i> Asrama Putri Telkom University</i>').add_to(m)
folium.Marker([-6.971991, 107.631161], popup='<i> School of Creative Industries, Telkom University</i>').add_to(m)
folium.Marker([-6.908559, 107.611097], popup='<i> Bandung Indah Plaza</i>').add_to(m)
folium.Marker([-6.907720, 107.610100], popup='<i> Gramedia Merdeka</i>').add_to(m)
folium.Marker([-6.907303, 107.609412], popup='<i> Istana Bandung Elektrik Center</i>').add_to(m)
folium.Marker([-6.910153, 107.610168], popup='<i> Taman Sejarah Bandung</i>').add_to(m)
folium.Marker([-6.912995, 107.609614], popup='<i> Taman Balai Kota Bandung</i>').add_to(m)
folium.Marker([-6.914033, 107.610214], popup='<i> Taman Vanda</i>').add_to(m)
folium.Marker([-6.898705, 107.612427], popup='<i> Taman Cikapundung</i>').add_to(m)
folium.Marker([-6.909303, 107.615191], popup='<i> Taman Maluku</i>').add_to(m)

folium.Marker([-6.898067, 107.609224], popup='<i> Taman Jomblo</i>').add_to(m)
folium.Marker([-6.893640, 107.610678], popup='<i> Taman Ganesha</i>').add_to(m)
folium.Marker([-6.894464, 107.608145], popup='<i> Museum Zoologi</i>').add_to(m)
folium.Marker([-6.894194, 107.613705], popup='<i> Rumah Sakit Santo Borromeus</i>').add_to(m)
folium.Marker([-6.895839, 107.612354], popup='<i> SMA Kristen Dago</i>').add_to(m)
folium.Marker([-6.894940, 107.612651], popup='<i> PT. Bank Nusantara Parahyangan</i>').add_to(m)
folium.Marker([-6.893443, 107.612651], popup='<i> Warung Pasta Bandung</i>').add_to(m)
folium.Marker([-6.893280, 107.612914], popup='<i> Martabak San Francisco</i>').add_to(m)
folium.Marker([-6.894977, 107.610949], popup='<i> Black Romantic</i>').add_to(m)
folium.Marker([-6.879233, 107.620205], popup='<i> Daily Routine Coffe</i>').add_to(m)

folium.Marker([-6.877100, 107.618113], popup='<i> Borma Dago</i>').add_to(m)
folium.Marker([-6.877650, 107.616938], popup='<i> Lumbung Rasa</i>').add_to(m)
folium.Marker([-6.868993, 107.533635], popup='<i> La Viva Cafe</i>').add_to(m)
folium.Marker([-6.868803, 107.593699], popup='<i> Rumah Imoet</i>').add_to(m)
folium.Marker([-6.871033, 107.593568], popup='<i> 18 Hrs cafe</i>').add_to(m)
folium.Marker([-6.872607, 107.593217], popup='<i> Ludwick Cafe</i>').add_to(m)
folium.Marker([-6.875744, 107.597420], popup='<i> Cafe Tungku</i>').add_to(m)
folium.Marker([-6.854777, 107.589008], popup='<i> Warkop Modjok</i>').add_to(m)
folium.Marker([-6.878945, 107.594161], popup='<i> Serasa Salad Bar</i>').add_to(m)
folium.Marker([-6.879016, 107.594227], popup='<i> Absolut</i>').add_to(m)

folium.Marker([-6.884589, 107.599008], popup='<i> Terminal Coffee Cemara</i>').add_to(m)
folium.Marker([-6.870031, 107.585067], popup='<i> Nimna Boocafe</i>').add_to(m)
folium.Marker([-6.907220, 107.566802], popup='<i> Ngopi Doeloe</i>').add_to(m)
folium.Marker([-6.877622, 107.593919], popup='<i> Cafe Puri Bumbu</i>').add_to(m)
folium.Marker([-6.877905, 107.593474], popup='<i> Mie Ayam Mas Joko Gepeng</i>').add_to(m)
folium.Marker([-6.877999, 107.593112], popup='<i> Nasi Uduk Cita Rasa</i>').add_to(m)
folium.Marker([-6.877952, 107.593363], popup='<i> Serabi Bu Erna</i>').add_to(m)
folium.Marker([-6.884246, 107.596840], popup='<i> MonSoon Cafe</i>').add_to(m)
folium.Marker([-6.884443, 107.598969], popup='<i> Cafe Kesini Geura</i>').add_to(m)
folium.Marker([-6.938785, 107.638081], popup='<i> Tempat Pemakaman Umum Gumuruh</i>').add_to(m)

folium.Marker([-6.937714, 107.637276], popup='<i> Shifu Ramen</i>').add_to(m)
folium.Marker([-6.937613, 107.636833], popup='<i> More Waffles</i>').add_to(m)
folium.Marker([-6.937251, 107.636682], popup='<i> Batagor Queen Hanawa</i>').add_to(m)
folium.Marker([-6.870455, 107.591732], popup='<i> Rumah Makan Kambing Bakar Cairo</i>').add_to(m)
folium.Marker([-6.870153, 107.591805], popup='<i> Cahaya Cakes 02</i>').add_to(m)
folium.Marker([-6.870057, 107.591866], popup='<i> FishnCheaps</i>').add_to(m)
folium.Marker([-6.869947, 107.591847], popup='<i> Sari Bundo</i>').add_to(m)
folium.Marker([-6.870240, 107.592164], popup='<i> Warung Nasi Sedan</i>').add_to(m)
folium.Marker([-6.870104, 107.592450], popup='<i> Ayam Goreng Kecap Acep</i>').add_to(m)
folium.Marker([-6.870452, 107.592996], popup='<i> Nobu Ramen and sushi</i>').add_to(m)

folium.Marker([-6.872020, 107.594125], popup='<i> Atok Rizal</i>').add_to(m)
folium.Marker([-6.871971, 107.594080], popup='<i> Holland Bakery</i>').add_to(m)
folium.Marker([-6.872029, 107.594571], popup='<i> Apotek Bona Farma</i>').add_to(m)
folium.Marker([-6.872223, 107.594683], popup='<i> Mie Baso-Mie Kocok Campur Tetelan</i>').add_to(m)
folium.Marker([-6.872456, 107.594825], popup='<i> Bakso Boedjangan Setiabudhi</i>').add_to(m) 
folium.Marker([-6.872532, 107.594883], popup='<i> Three Sixty Cafe</i>').add_to(m) 
folium.Marker([-6.872573, 107.594901], popup='<i> Apotik Setiabudhi</i>').add_to(m) 
folium.Marker([-6.872783, 107.594979], popup='<i> Warung Nasi Khas Sunda Laksana</i>').add_to(m) 
folium.Marker([-6.872781, 107.595048], popup='<i> Abuba Steak</i>').add_to(m) 
folium.Marker([-6.873015, 107.595191], popup='<i> Amanda Setiabudi</i>').add_to(m) 

folium.Marker([-6.912781, 107.664919], popup='<i> SMA Negeri 23 Bandung</i>').add_to(m)
folium.Marker([-6.900972, 107.585742], popup='<i> SMAN 9 Bandung</i>').add_to(m)
folium.Marker([-6.905546, 107.582892], popup='<i> SMA Angkasa</i>').add_to(m)
folium.Marker([-6.906233, 107.592395], popup='<i> SMKN 12 Bandung</i>').add_to(m)
folium.Marker([-6.890490, 107.558189], popup='<i> SMK 11 Bandung</i>').add_to(m)
folium.Marker([-6.913189, 107.608553], popup='<i> Sekolah Menengah Kejuruan Negeri 1 Bandung</i>').add_to(m)
folium.Marker([-6.895333, 107.612575], popup='<i> Sekolah Menengah Atas Negeri 1 Bandung</i>').add_to(m)
folium.Marker([-6.891334, 107.603975], popup='<i> Sekolah Menengah Atas Pasundan 8</i>').add_to(m)
folium.Marker([-6.873583, 107.616192], popup='<i> Sekolah Menengah Atas Negeri 19 Bandung</i>').add_to(m)
folium.Marker([-6.904103, 107.622166], popup='<i> Sekolah Menengah Atas Negeri 20 Bandung</i>').add_to(m)

folium.Marker([-6.875609, 107.595739], popup='<i> St. Laurent Catholic Church</i>').add_to(m)
folium.Marker([-6.811432, 107.644959], popup='<i> Hotel Narima</i>').add_to(m)
folium.Marker([-6.904356, 107.611774], popup='<i> Gereja Katolik Mahasiswa</i>').add_to(m)
folium.Marker([-6.826721, 107.595434], popup='<i> Kampung Gajah Wonderland</i>').add_to(m)
folium.Marker([-6.849249, 107.595880], popup='<i> Amazing Art World</i>').add_to(m)
folium.Marker([-6.852839, 107.611127], popup='<i> Kebun Hidroponik Punclut</i>').add_to(m)
folium.Marker([-6.896005, 107.655626], popup='<i> Saung Angklung Udjo </i>').add_to(m)
folium.Marker([-6.917082, 107.764963], popup='<i> Bandung Giri Gahana Golf and Resort </i>').add_to(m)
folium.Marker([-6.931275, 107.763968], popup='<i> Institut Pemerintaan dalam Negeri</i>').add_to(m)
folium.Marker([-6.969376, 107.584427], popup='<i> PS Phoneshop JABAR</i>').add_to(m)

folium.Marker([-6.944649, 107.495419], popup='<i> Cihampelas</i>').add_to(m)
folium.Marker([-6.955716, 107.560650], popup='<i> Margaasih </i>').add_to(m)
folium.Marker([-6.995691, 107.557012], popup='<i> Katapang</i>').add_to(m)
folium.Marker([-6.869125, 107.658339], popup='<i> Warung Seblak Kustian</i>').add_to(m)
folium.Marker([-6.858343, 107.573770], popup='<i> Olea Fruit Salad</i>').add_to(m)
folium.Marker([-6.849143, 107.592888], popup='<i> Peakwineonline.com</i>').add_to(m)
folium.Marker([-6.846564, 107.599281], popup='<i> Polsekta Cidadap</i>').add_to(m)
folium.Marker([-6.820394, 107.596704], popup='<i> Lembang</i>').add_to(m)
folium.Marker([-6.8716943,107.578043], popup='<i> Parahyangan Rumah Villa PRV</i>').add_to(m)
folium.Marker([-6.8699048,107.582120], popup='<i> KPAD Gegerkalong</i>').add_to(m)

folium.Marker([-6.8680407,107.584148], popup='<i> Masjid At-Taqwa KPADs</i>').add_to(m)
folium.Marker([-6.8683336,107.582989], popup='<i> Polsek Sukasari</i>').add_to(m)
folium.Marker([-6.8681246,107.583086], popup='<i> Warung Risa</i>').add_to(m)               
folium.Marker([-6.868044,107.5830357], popup='<i> Indomaret</i>').add_to(m)
folium.Marker([-6.8682591,107.5829626], popup='<i> Azalia Cake & Bakery</i>').add_to(m)
folium.Marker([-6.8683556,107.5834086], popup='<i> Pecel Lele SKA</i>').add_to(m)
folium.Marker([-6.8683237,107.583375], popup='<i> Pawitra Animation Studio</i>').add_to(m)
folium.Marker([-6.8683862,107.584179], popup='<i> Mitra Car Wash</i>').add_to(m)
folium.Marker([-6.8683197,107.5840905], popup='<i> Sudinar Artha Industri, Pt</i>').add_to(m)
folium.Marker([-6.868973, 107.569125], popup='<i> Warung Seblak Kustian, Pt</i>').add_to(m)

folium.Marker([-6.875622, 107.590448], popup='<i> Toko Ibu Cucu</i>').add_to(m) 
folium.Marker([-6.875579, 107.590579], popup='<i> Rikatur Lampion</i>').add_to(m)
folium.Marker([-6.875855, 107.590500], popup='<i> Toko 33</i>').add_to(m)
folium.Marker([-6.876028, 107.589707], popup='<i> De Mooie Kast</i>').add_to(m)
folium.Marker([-6.876545, 107.589586], popup='<i> Nusantara Satria Agung. PT</i>').add_to(m)
folium.Marker([-6.877388, 107.589900], popup='<i> Lotus Indah Textile Industri. PT</i>').add_to(m)
folium.Marker([-6.877487, 107.589550], popup='<i> Han Kook Gwan</i>').add_to(m)
folium.Marker([-6.877664, 107.589606], popup='<i> Telkom Risty</i>').add_to(m)
folium.Marker([-6.877727, 107.590085], popup='<i> Prudential</i>').add_to(m)
folium.Marker([-6.877758, 107.589796], popup='<i> Kinderland Preschool Bandung</i>').add_to(m)

folium.Marker([-6.878264, 107.590325], popup='<i> Orca Garaga</i>').add_to(m)
folium.Marker([-6.878334, 107.590278], popup='<i> Orga Motor Wash</i>').add_to(m)
folium.Marker([-6.879602, 107.590045], popup='<i> RIDECORE COMPANY</i>').add_to(m)
folium.Marker([-6.880053, 107.590011], popup='<i> Puri JPS</i>').add_to(m)
folium.Marker([-6.880111, 107.590168], popup='<i> ZEN Rooms Cipedes Tengah</i>').add_to(m)
folium.Marker([-6.903862, 107.611315], popup='<i> The Luxton Hotel Bandung</i>').add_to(m)
folium.Marker([-6.917120, 107.608284], popup='<i> Aston Braga Hotel & Residence</i>').add_to(m)
folium.Marker([-6.902840, 107.605419], popup='<i> Hotel Sakura Bandung</i>').add_to(m)
folium.Marker([-6.899853, 107.596132], popup='<i> ibis Bandung Pasteur</i>').add_to(m)
folium.Marker([-6.912913, 107.597538], popup='<i> Hilton Bandung</i>').add_to(m)

folium.Marker([-6.861026, 107.583457], popup='<i> Masjid Babussalam  </i>').add_to(m)
folium.Marker([-6.862379, 107.586933], popup='<i> Masjid Nurul Falah</i>').add_to(m)
folium.Marker([-6.859921, 107.571905], popup='<i> Masjid Al Ikhwan </i>').add_to(m)
folium.Marker([-6.861299, 107.569228], popup='<i> Masjid Al Aniyah</i>').add_to(m)
folium.Marker([-6.866835, 107.561462], popup='<i> Masjid Nurul Hikmah </i>').add_to(m)
folium.Marker([-6.873112, 107.560255], popup='<i> Masjid Al-Fajri </i>').add_to(m)
folium.Marker([-6.875357, 107.557508], popup='<i> Masjid Mutiara Hikmah </i>').add_to(m)
folium.Marker([-6.888678, 107.574214], popup='<i> Masjid Al Mujahirin Gerbang Tol Pasteur </i>').add_to(m)
folium.Marker([-6.877835, 107.576456], popup='<i> Masjid Jami Al Ishlah</i>').add_to(m)
folium.Marker([-6.880924, 107.577411], popup='<i> Masjid Jami Al-Muqimin</i>').add_to(m)

folium.Marker([-6.901455, 107.604385], popup='<i> Warunk Upnormal Cihampelas 2</i>').add_to(m)
folium.Marker([-6.898203, 107.613418], popup='<i> Warunk Upnormal Dipatiukur</i>').add_to(m)
folium.Marker([-6.910410, 107.625964], popup='<i> Warunk Upnormal Riau Bandung</i>').add_to(m)
folium.Marker([-6.941915, 107.628024], popup='<i> Warunk Upnormal buah batu bandung</i>').add_to(m)
folium.Marker([-6.924635, 107.619950], popup='<i> UPNORMAL BURANGRANG</i>').add_to(m)
folium.Marker([-6.926318, 107.619655], popup='<i> De Fred Barber & Shop</i>').add_to(m)
folium.Marker([-6.925109, 107.618646], popup='<i> Holako Barbershop</i>').add_to(m)
folium.Marker([-6.934975, 107.621189], popup='<i> Barber Pop Hairmechanic </i>').add_to(m)
folium.Marker([-6.935718, 107.621715], popup='<i> Jims Barbershop</i>').add_to(m)
folium.Marker([-6.932676, 107.622198], popup='<i> Barber Sixx </i>').add_to(m)



folium.Marker([-6.863278, 107.579878], popup='<i> Joglo Sentir Klasikan</i>').add_to(m)
folium.Marker([-6.858751, 107.591631], popup='<i> Asrama Mahasiswa PPG Pasca SM-3T UPI</i>').add_to(m)
folium.Marker([-6.860728, 107.593522], popup='<i> Gedung FPBS UPI</i>').add_to(m)
folium.Marker([-6.860542, 107.594960], popup='<i> The Heritage Kitchen & Gallery BDG</i>').add_to(m)
folium.Marker([-6.859839, 107.594139], popup='<i> Museum Pendidikan Nasional UPI</i>').add_to(m)
folium.Marker([-6.863264, 107.599117], popup='<i> SDN 204 CIDADAP</i>').add_to(m)
folium.Marker([-6.861224, 107.600126], popup='<i> TravelDay Bandung</i>').add_to(m)
folium.Marker([-6.885387, 107.580790], popup='<i> Gereja Jemaat Kristen Indonesia</i>').add_to(m)
folium.Marker([-6.892407, 107.586461], popup='<i> Gereja Kristen Protestan Simalungun</i>').add_to(m)
folium.Marker([-6.973988, 107.630407], popup='<i> Telkom University</i>').add_to(m)

folium.Marker([-6.907451, 107.606047], popup='<i> Kimia Farma Trading & Distribution Unit Bandung</i>').add_to(m)
folium.Marker([-6.897701, 107.597576], popup='<i> Dr. Hasan Sadikin General Hospital</i>').add_to(m)
folium.Marker([-6.895744, 107.598971], popup='<i> Rumah Sakit Pendidikan Universitas Padjajaran</i>').add_to(m)
folium.Marker([-6.895748, 107.588856], popup='<i> Hermina Pasteur Hospital</i>').add_to(m)
folium.Marker([-6.915956, 107.596484], popup='<i> Rumah Sakit Kebon Jati</i>').add_to(m)
folium.Marker([-6.929213, 107.600677], popup='<i> Rumah Sakit Khusus Ibu dan Anak Kota Bandung</i>').add_to(m)
folium.Marker([-6.898247, 107.615030], popup='<i> Bandung Medical Center</i>').add_to(m)
folium.Marker([-6.906235, 107.598419], popup='<i> Rumah Sakit Melinda 2</i>').add_to(m)
folium.Marker([-6.915239, 107.600329], popup='<i> Santosa Hospital Bandung Central</i>').add_to(m)
folium.Marker([-6.906775, 107.603324], popup='<i> Melinda Hospital</i>').add_to(m)

folium.Marker([-6.887511, 107.581079], popup='<i> Rumah Sakit Gigi & Mulut Maranatha</i>').add_to(m)
folium.Marker([-6.885414, 107.620386], popup='<i> RS Khusus Ginjal Ny. R.A. Habbie</i>').add_to(m)
folium.Marker([-6.887511, 107.581079], popup='<i> Rumah Sakit Gigi & Mulut Maranatha</i>').add_to(m)
folium.Marker([-6.894148, 107.613800], popup='<i> Saint Borromeus Hospital</i>').add_to(m)
folium.Marker([-6.933643, 107.623193], popup='<i> Muhammadiyah Hospital of Bandung</i>').add_to(m)
folium.Marker([-6.884101, 107.594896], popup='<i> RS Jiwa Hurip Waluya</i>').add_to(m)
folium.Marker([-6.912367, 107.573167], popup='<i> Rumah Sakit Rajawali</i>').add_to(m)
folium.Marker([-6.884286, 107.552698], popup='<i> RS Mitra Kasih</i>').add_to(m)
folium.Marker([-6.879120, 107.550891], popup='<i> Cibabat Hospital</i>').add_to(m)
folium.Marker([-6.906058, 107.613617], popup='<i> Limijati Women And Children Hospital</i>').add_to(m)

folium.Marker([-6.866732, 107.515163], popup='<i> PT Ultra Jaya Milk Industry</i>').add_to(m)
folium.Marker([-6.866795, 107.514119], popup='<i> Kraft Ultra Jaya Indonesia</i>').add_to(m)
folium.Marker([-6.867954, 107.516474], popup='<i> PT. SUMBER MEKAR TEKSTIL INDONESIA</i>').add_to(m)
folium.Marker([-6.868412, 107.518041], popup='<i> Ateja Multi Industri</i>').add_to(m)
folium.Marker([-6.869689, 107.533422], popup='<i> Transmart - Carrefour Cimahi</i>').add_to(m)
folium.Marker([-6.949636, 107.619582], popup='<i> PT LEN Industri(Persero)</i>').add_to(m)
folium.Marker([-6.969417, 107.616699], popup='<i> Alena Textile Industries. PT</i>').add_to(m)
folium.Marker([-6.970482, 107.617144], popup='<i> PT Industri Telekomunikasi Indonesia/i>').add_to(m)
folium.Marker([-6.971182, 107.616000], popup='<i> PT. Perusahaan Industri Ceres</i>').add_to(m)
folium.Marker([-6.970722, 107.616241], popup='<i> PT Papandayan Cocoa Industries - Barry Callebaut</i>').add_to(m)

folium.Marker([-6.859808, 107.594408], popup='<i> Museum Pendidikan Nasional UPI</i>').add_to(m)
folium.Marker([-6.878243, 107.587576], popup='<i> Museum Barli</i>').add_to(m)
folium.Marker([-6.917653, 107.611379], popup='<i> Museum Mandala Wangsit Siliwangi</i>').add_to(m)
folium.Marker([-6.921209, 107.609536], popup='<i> Museum Konferensi Asia Afrika</i>').add_to(m)
folium.Marker([-6.914497, 107.609287], popup='<i> Museum Bank Indonesia Jawa Barat</i>').add_to(m)
folium.Marker([-6.926197, 107.633011], popup='<i> Museum Virajati Seskoad</i>').add_to(m)
folium.Marker([-6.900709, 107.622797], popup='<i> Museum Perbendaharaan</i>').add_to(m)
folium.Marker([-6.894539, 107.608242], popup='<i> Museum Zoologi</i>').add_to(m)
folium.Marker([-6.937768, 107.603480], popup='<i> Museum Sri Baduga</i>').add_to(m)
folium.Marker([-6.904938, 107.610579], popup='<i> Dewan Kerajinan Nasional Provinsi Jawa Barat</i>').add_to(m)

folium.Marker([-6.914953, 107.610653], popup='<i> Gereja Katedral Santo Petrus Bandung</i>').add_to(m)
folium.Marker([-6.896849, 107.604726], popup='<i> Gereja Mawar Sharon Bandung</i>').add_to(m)
folium.Marker([-6.911895, 107.610692], popup='<i> Gereja Kristen Jawa Bandung</i>').add_to(m)
folium.Marker([-6.910259, 107.597581], popup='<i> Gereja Kristen Immanuel</i>').add_to(m)
folium.Marker([-6.910293, 107.597516], popup='<i> GKIm Ka Im Tong</i>').add_to(m)
folium.Marker([-6.930979, 107.598182], popup='<i> Gereja Bethel Indonesia Bethany Bandung</i>').add_to(m)
folium.Marker([-6.929350, 107.607183], popup='<i> Gereja Katolik Santo Paulus</i>').add_to(m)
folium.Marker([-6.926943, 107.608691], popup='<i> Kalam Kudus Pasundan Christian Church</i>').add_to(m)
folium.Marker([-6.900821, 107.613776], popup='<i> Gereja Kristen Indonesia Maulana Yusuf</i>').add_to(m)
folium.Marker([-6.907047, 107.626432], popup='<i> GPIB Maranatha</i>').add_to(m)


folium.Marker(
    location=[-6.970981, 107.617771],
    popup='PT Inti Global Optical Communication',
    icon=folium.Icon(icon='cloud')
).add_to(m)

folium.Marker(
    location=[-6.856086, 107.497845],
    popup='PT Indofood CBP Sukses Makmur',
    icon=folium.Icon(icon='cloud')
).add_to(m)

folium.Marker(
    location=[-6.867954, 107.516474],
    popup='PT. SUMBER MEKAR TEKSTIL INDONESIA',
    icon=folium.Icon(icon='cloud')
).add_to(m)

folium.Marker(
    location=[-6.853039, 107.496860],
    popup='PT Combiphar',
    icon=folium.Icon(icon='cloud')
).add_to(m)

folium.Marker(
    location=[-6.854288, 107.498216],
    popup='PT. Tempo Scan Pacific Tbk - Bandung 2',
    icon=folium.Icon(icon='cloud')
).add_to(m)

folium.Marker(
    location=[-6.857845, 107.496532],
    popup='PT. Sugih Instrumendo Abadi',
    icon=folium.Icon(icon='cloud')
).add_to(m)

folium.Marker(
    location=[-6.888550, 107.497037],
    popup='PT. Ateja Tritunggal',
    icon=folium.Icon(icon='cloud')
).add_to(m)

folium.Marker(
    location=[-6.887177, 107.497118],
    popup='Gani Arta Dwitunggal. PT',
    icon=folium.Icon(icon='cloud')
).add_to(m)

folium.Marker(
    location=[-6.891079, 107.502072],
    popup='PT Central Texindo',
    icon=folium.Icon(color='red', icon='cloud')
).add_to(m)

folium.Marker(
    location=[-6.895683, 107.503161],
    popup='PT San Central Indah',
    icon=folium.Icon(color='red', icon='cloud')
).add_to(m)




folium.Marker(
    location=[-6.902738, 107.620261],
    popup='PT Pos Indonnesia(Persero)',
    icon=folium.Icon(color='orange')
).add_to(m)

folium.Marker(
    location=[-6.887305, 107.601740],
    popup='Kantorpos Bandung Cipaganti',
    icon=folium.Icon(color='orange')
).add_to(m)

folium.Marker(
    location=[-6.894076, 107.590135],
    popup='Kantor Pos Cipedes',
    icon=folium.Icon(color='orange')
).add_to(m)

folium.Marker(
    location=[-6.904451, 107.580766],
    popup='Kantor Pos Bandung Husein',
    icon=folium.Icon(color='orange')
).add_to(m)

folium.Marker(
    location=[-6.920838, 107.606213],
    popup='Kantor Pos Bandung',
    icon=folium.Icon(color='orange')
).add_to(m)

folium.Marker(
    location=[-6.909418, 107.595143],
    popup='Kantorpos Bandung Arjuna',
    icon=folium.Icon(color='orange')
).add_to(m)

folium.Marker(
    location=[-6.907094, 107.617232],
    popup='Kantor Pos - Banda',
    icon=folium.Icon(color='orange')
).add_to(m)

folium.Marker(
    location=[-6.906936, 107.617403],
    popup='Kantorpos Bandung Cihapit',
    icon=folium.Icon(color='orange')
).add_to(m)

folium.Marker(
    location=[-6.906933, 107.617380],
    popup='Graha Pos Indonesia Bandung',
    icon=folium.Icon(color='orange')
).add_to(m)

folium.Marker(
    location=[-6.904321, 107.604205],
    popup='Kantor Pos Ujung Berung',
    icon=folium.Icon(color='orange')
).add_to(m)


m

