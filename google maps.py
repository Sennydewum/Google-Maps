import folium

coordonats= [44.397373466281714, 26.069094038901902] #here put your home cordonats
map = folium.Map(location=coordonats)
map.save("example.html") #put a random name in example