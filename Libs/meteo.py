# -*- coding: utf-8 -*-

import requests


class Meteo:
    def get_meteo(self, ville):
        """
        Utilisation de l'API de OpenWeatherMap
        https://openweathermap.org/current#data
        Récupération des données et affichage
        :return response : la réponse de l'API
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

        # AFFICHAGE
        response = "Station météo de " + ville + " , " + pays + "\ntemperature moyenne:  {}".format(temp) + "° (min :{}" \
            .format(temp_min) + "°/max : {}".format(temp_max) + "°)\nTaux d'humidite : {}".format(humidite) + \
                   "%\nConditions climatiques : {}".format(description_temps)

        return response
