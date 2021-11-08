# -*- coding: utf-8 -*-
import requests
from googlesearch import search
from pyroutelib3 import Router

def meteo():
    """
    Utilisation de l'API de OpenWeatherMap
    https://openweathermap.org/current#data
    :return:
    """

    ville = input("De quelle ville voulez vous connaitre la meteo ? (Ex : Paris,Londres,Bruxelles)")
    url_weather = "http://api.openweathermap.org/data/2.5/weather?q=" + ville + "&units=metric&lang=fr&APPID=" \
                                                                                "beb97c1ce62559bba4e81e28de8be095"
    r_weather = requests.get(url_weather)
    data = r_weather.json()

    # RECUPERATION DES DONNEES
    temp = data['main']['temp']
    temp_min = data['main']['temp_min']
    temp_max = data['main']['temp_max']
    humidite = data['main']['humidity']
    description_temps = data['weather'][0]['description']

    # AFFICHAGE
    print(
        "temperature moyenne:  {}".format(temp) + "° (min :{}".format(temp_min) + "°/max : {}".format(temp_max) + "°)")
    print("Taux d'humidite : {}".format(humidite) + "%")
    print("Conditions climatiques : {}".format(description_temps))

    input("\n\nAppuyez sur Entrée pour continuer...")

def itineraire():
    lat1 = input("Entrez la latitude de la ville de départ")
    lon1 = input("Entrez la longitude de la ville de départ")
    lat2 = input("Entrez la latitude de la ville d'arrivée")
    lon2 = input("Entrez la longitude de la ville d'arrivée")
    router = Router("car")
    start = router.findNode(lat1, lon1)
    finish = router.findNode(lat2, lon2)
    status, route = router.doRoute(start, finish)
    if status == 'success':
        pathLatLons = list(map(router.nodeLatLon, route))
        print(pathLatLons)
        
        
        
def news():
    query = input('Que souhaitez vous rechercher? ')
    nbr_query = int(input('Combien de résultats ? : '))
    for i in search(query, tld='com', lang='fr', num=nbr_query, stop=nbr_query, pause=2):
        print(i)
    input("\n\nAppuyez sur Entrée pour continuer...")


if __name__ == "__main__":

    choix = -1

    while choix != 0:
        try:
            choix = int(input("1)Meteo\n2)News\n0)Quitter\n\nChoix :"))

        except:
            print("Erreur")

        if choix == 1:
            meteo()

        elif choix == 2:
            news()
