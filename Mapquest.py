import urllib.parse
import requests

api_url = "https://www.mapquestapi.com/directions/v2/route?"
origin = "Santiago, Chile"
destination = "Ovalle, Chile"
key = "lmLD5bdxddaGqq0kedbGOlwst2LY56JU"

while True:
    origin = input("Ciudad de Origen: ")
    if origin == 'q':
        break
    destination = input("Ciudad de Destino: ")
    if destination == 'q':
        break
    url = api_url + urllib.parse.urlencode ({"key":key, "from": origin, "to":destination})
    json_data = requests.get(url).json()
    status_code = json_data["info"]["statuscode"]
    if status_code == 0:
        trip_duration = json_data["route"]["formattedTime"]
        distance = json_data["route"]["distance"] *1.63
        print("-----------------------------------------")
        print(f"Informacion del viaje desde {origin.capitalize()} hasta {destination.capitalize()}.")
        print(f"Duracion Total del Viaje: {trip_duration}.")
        print("Distancia de Kilometros: " + str("{:.3f}".format(distance) + "Kilometros Recorridos"))