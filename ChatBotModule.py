# -*- coding: utf-8 -*-
import requests


def meteo():
    """
    Utilisation de l'API de OpenWeatherMap
    https://openweathermap.org/current#data
    :return:
    """

    ville = input("De quelle ville voulez vous connaitre la meteo ? (Ex : Paris,London)")
    url_weather = "http://api.openweathermap.org/data/2.5/weather?q=" + ville + "&units=metric&APPID=" \
                                                                                "230b261060b9d52c56139e41ae47cf77"
    r_weather = requests.get(url_weather)
    data = r_weather.json()

    # RECUPERATION DES DONNEES
    temp = data['main']['temp']
    temp_min = data['main']['temp_min']
    temp_max = data['main']['temp_max']
    humidite = data['main']['humidity']
    description_temps = data['weather'][0]['description']

    # AFFICHAGE
    print("La temperature moyenne est de {} degres Celsius".format(temp))
    print("Les temperatures varient entre {}".format(temp_min) + " a {} degres Celsius".format(temp_max))
    print("Taux d'humidite de {}".format(humidite) + "%")
    print("Conditions climatiques : {}".format(description_temps))



if __name__ == "__main__":

    choix = -1

    while choix != 0:
        choix = int(input("1)Meteo\n0)Quitter\n\nChoix :"))

        if choix == 1:
            meteo()
