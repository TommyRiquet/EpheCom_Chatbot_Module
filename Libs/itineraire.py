# -*- coding: utf-8 -*-

import openrouteservice
import openrouteservice.exceptions
import requests


class Addresse:
    """
        Cette classe représente une addresse utilisé dans la classe Itineraire

        Author : T. Riquet,Q. Laruelle
        Date : December 2021
    """
    def get_addresse(self, addresse):
        """
                Cette méthode renvoie les coordonnées d'une addresse donnée

                PRE : adresse est un str
                POST : retourne les coordonées de l'addresse
                RAISE :
                -KeyError : lorsque la limite journalière autorisé par la clé API est atteinte
                -openrouteservice.exceptions.ApiError : Erreur API lors d'un calcul d'itinéraire impossible

        """

        lat = 0
        long = 0

        url_addr = "https://maps.open-street.com/api/geocoding/?address=" + addresse + "&sensor=false&key" \
                                                                                       "=143323c5ab5dfe15ec89b2bbb320bea7"
        r_addr = requests.get(url_addr)
        coord = r_addr.json()

        if coord['status'] == 'LIMIT_REACHED':
            return 'LIMIT_REACHED'
        try:
            lat = float(coord['results'][0]['geometry']['location']['lat'])
            long = float(coord['results'][0]['geometry']['location']['lng'])
        except KeyError:
            pass
        return [lat, long]


class Itineraire:
    """
        Cette classe représente un module de calcul d'itinéraire pour le Chatbot

        Author : T. Riquet,Q. Laruelle
        Date : December 2021
        """
    def get_itineraire(self, adresse1, adresse2, arg):
        """
        Cette méthode renvoie calcul le temps et la distance entre deux points.
        Elle peut aussi renvoyer un itinéraire

        PRE : adresse1 , adresse2 et arg sont des str
        POST : retourne le temps ,la distance et/ou l'itinéraire demandé
        RAISE : /
        """

        # ADDRESSE 1
        addr1 = adresse1
        coord1 = Addresse().get_addresse(addr1)
        if coord1 != 'LIMIT_REACHED':
            lat1, long1 = coord1
        else:
            return 'Limite journalière atteinte'

        # ADDRESSE 2
        addr2 = adresse2
        coord2 = Addresse().get_addresse(addr2)
        if coord2 != 'LIMIT_REACHED':
            lat2, long2 = coord2
        else:
            return 'Limite journalière atteinte'

        # CALCUL DE TEMPS ET DE DISTANCE
        # https://maps.open-street.com/api/route/?origin="+coord1x+","+coord1y+"&destination="+coord2x+","+coord2y+"&mode=driving&key=143323c5ab5dfe15ec89b2bbb320bea7
        url_final = "https://maps.open-street.com/api/route/?origin=" + str(lat1) + "," + str(
            long1) + "&destination=" + str(lat2) + "," + str(
            long2) + "&mode=driving&key=143323c5ab5dfe15ec89b2bbb320bea7"
        r_final = requests.get(url_final)
        data = r_final.json()
        distance = data['total_distance']
        time = data['total_time']

        # CREATION DE LA REPONSE
        response = "distance en km : " + str(distance / 1000)
        heure = int(time / 3600)
        minutes = int((time % 3600) / 60)
        secondes = int((time % 3600) % 60)
        response += "\ntemps de trajet : " + str(heure) + "h " + str(minutes) + "m " + str(secondes) + "s"

        # AJOUT DES ETAPES SI /route
        try:
            if arg == "route":
                coords = ((long1, lat1), (long2, lat2))  # (long,lat)départ, (long,lat)arrivée
                client = openrouteservice.Client(
                    key='5b3ce3597851110001cf624842459ea605184a62ac2aa7283c08ccbf')  # Clef personnelle
                routes = client.directions(coords)
                for i in routes["routes"]:
                    for j in i['segments']:
                        for k in j['steps']:
                            response += ("\n" + k['instruction'])
        except openrouteservice.exceptions.ApiError:
            return 'Impossible de calculer l\'itinéraire'

        return response
