import phonenumbers
from phonenumbers import geocoder
from opencage.geocoder import OpenCageGeocode
import folium

#usuario entra com o numero de telefone no formato string
num_phone = input("Digite o número de telefone (ex: +5521954845152): ")

#cria um objeto phone
phone = phonenumbers.parse(num_phone)

#gera a localização do numero no idioma pt
geoloc = geocoder.description_for_number(phone, "pt")

print(geoloc)

#Agora vamos precisar da chave que foi gerada ao realizar o cadastro no site
key = 'sua_chave_aqui'
geocoder = OpenCageGeocode(key)

#Criamos uma pesquisa com a nossa regiao, obtida atraves da biblioteca phonenumber
query = geoloc
results = geocoder.geocode(query)

#A variavel results, retorna um objeto Json, como isso podemos acessar apenas aquilo que queremos 
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

#Crie o mapa com a localidade de seu interesse.
map_phone = folium.Map(location=[lat, lng], zoom_start=11)

#Cria um marcador no mapa com as coodenadas inseridas pelo usuario
folium.Marker([lat,lng], popup=geoloc).add_to((map_phone))

#Salva o mapa
map_phone.save("map_phone.html")