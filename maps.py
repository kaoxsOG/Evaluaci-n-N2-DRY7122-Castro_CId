import requests
import urllib

api_url = "https://www.mapquestapi.com/directions/v2/route?"
key = "lmLD5bdxddaGqq0kedbGOlwst2LY56JU"


while True:
    origin = input ("Ingresar el Punto de Origen: ")
    if origin == 'q':
        break
    destination = input ("Ingresa el destino: ")
    if destination == 'q':
        break