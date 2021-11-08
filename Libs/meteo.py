# -*- coding: utf-8 -*-

import requests


def meteo(ville):
    """
    Utilisation de l'API de OpenWeatherMap
    https://openweathermap.org/current#data
    Récupération des données et affichage
    :return:
    """

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
