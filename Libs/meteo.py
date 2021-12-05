# -*- coding: utf-8 -*-

import requests


class Meteo:
    """
        Cette classe représente un module de Météo pour le Chatbot

        Author : T. Riquet
        Date : December 2021
    """
    def get_meteo(self, ville):
        """
        Cette méthode renvoie les informations sur la météo d'une ville

        PRE : ville est un str
        POST : retourne les informations sur la ville donnée en argument
        RAISES : /
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
        ville = data['name']
        pays = data['sys']['country']

        # CREATION DE LA REPONSE
        response = "Station météo de " + ville + " , " + pays + "\ntemperature moyenne:  {}".format(
            temp) + "° (min :{}".format(temp_min) + "°/max : {}".format(temp_max) + "°)\nTaux d'humidite : {}".format(
            humidite) + "%\nConditions climatiques : {}".format(description_temps)

        return response
