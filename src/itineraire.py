# -*- coding: utf-8 -*-

import openrouteservice
import openrouteservice.exceptions
import requests
from deep_translator import GoogleTranslator


class Addresse:
    """
        Cette classe représente une addresse utilisé dans la classe Itineraire

        Author : T. Riquet, Q. Laruelle
        Date : December 2021
    """

    def get_addresse(self, addresse):
        """
                Cette méthode renvoie les coordonnées d'une addresse donnée

                PRE : adresse est un str
                POST : retourne les coordonées de l'addresse
                RAISE :
                -KeyError : lorsque la limite journalière autorisée par la clé API est atteinte
                -openrouteservice. Exceptions. ApiError : Erreur API lors d'un calcul d'itinéraire impossible

        """

        lat = 0
        long = 0

        url_addr = "https://maps.open-street.com/api/geocoding/?address=" + addresse + "&sensor=false&key" \
                                                                                       "=9744eec549f1c82b18af8" \
                                                                                       "a10f26d1489"
        r_addr = requests.get(url_addr)
        coord = r_addr.json()

        if coord['status'] == 'LIMIT_REACHED':
            return 'Oops, on dirait que vous avez atteint la limite journalière autorisé :/'
        try:
            lat = float(coord['results'][0]['geometry']['location']['lat'])
            long = float(coord['results'][0]['geometry']['location']['lng'])
        except KeyError:
            return 0
        return [lat, long]

    def get_route(self, long1, lat1, long2, lat2):
        """
        Cette méthode calcul les étapes de l'itinéraire à partir de coordonnés GPS

        PRE : long1,lat1,long2,lat2 sont des entiers
        POST : renvoie les étapes si possibles
        RAISES : openroute. Exceptions. ApiError : Si le calcul de l'itinéraire est impossible : renvoie 0
        """
        response = ""
        try:
            coords = ((long1, lat1), (long2, lat2))  # (long,lat)départ, (long,lat)arrivée
            client = openrouteservice.Client(
                key='5b3ce3597851110001cf624842459ea605184a62ac2aa7283c08ccbf')  # Clef personnelle
            routes = client.directions(coords)
            for i in routes["routes"]:
                for j in i['segments']:
                    for k in j['steps']:
                        response += ("\n" + k['instruction'])

            return response
        except openrouteservice.exceptions.ApiError:
            return 0


class Itineraire:
    """
itineraire (Adresse 1) / (Adresse 2) /route

"""

    def get_itineraire(self, message):
        """
        Cette méthode renvoie calcul le temps et la distance entre deux points.
        Elle peut aussi renvoyer un itinéraire

        PRE : adresse1, adresse2 et arg sont des str
        POST : retourne le temps, la distance et l'itinéraire demandé
        RAISE : /
        """

        try:
            adresse1 = message.split("/")[0][12:]
            adresse2 = message.split("/")[1]
            try:
                arg = message.split("/")[2]
            except (ValueError, IndexError, KeyError):
                arg = ' '
        except (ValueError, IndexError, KeyError):
            return self.__doc__

        # ADDRESSE 1
        addr1 = adresse1
        coord1 = Addresse().get_addresse(addr1)
        if coord1 == 'LIMIT_REACHED':
            return 'Oops, on dirait que vous avez atteint la limite journalière autorisé :/'
        elif coord1 == 0:
            return 'Oops, je ne connais pas l\'addresse 1 :/'
        else:
            lat1, long1 = coord1

        # ADDRESSE 2
        addr2 = adresse2
        coord2 = Addresse().get_addresse(addr2)
        if coord2 == 'LIMIT_REACHED':
            return 'Oops, on dirait que vous avez atteint la limite journalière autorisé :/'
        elif coord2 == 0:
            return 'Oops, je ne connais pas l\'addresse 2 :/'
        else:
            lat2, long2 = coord2

        # CALCUL DE TEMPS ET DE DISTANCE
        # https://maps.open-street.com/api/route/?origin="+coord1x+","+coord1y+"&destination="+coord2x+","+coord2y+"&mode=driving&key=143323c5ab5dfe15ec89b2bbb320bea7
        url_final = "https://maps.open-street.com/api/route/?origin=" + str(lat1) + "," + str(
            long1) + "&destination=" + str(lat2) + "," + str(
            long2) + "&mode=driving&key=9744eec549f1c82b18af8a10f26d1489"
        r_final = requests.get(url_final)
        data = r_final.json()
        try:
            distance = data['total_distance']
            time = data['total_time']
        except (ValueError, IndexError, KeyError):
            return 'Oops , votre trajet a l\'air trop compliqué à calculer :/'

        # CREATION DE LA REPONSE
        response = "distance en km : " + str(round((distance / 1000), 2))
        heure = int(time / 3600)
        minutes = int((time % 3600) / 60)
        secondes = int((time % 3600) % 60)
        response += "\ntemps de trajet : " + str(heure) + "h " + str(minutes) + "m " + str(secondes) + "s"

        if arg == 'route':
            route = Addresse().get_route(long1, lat1, long2, lat2)
            if route != 0:
                try:
                    response += GoogleTranslator(source='en', target='fr').translate(route)
                except requests.exceptions.ConnectionError:
                    response += route
            elif route == 0:
                return 'Oops, L\'itinéraire semble trop compliqué à calculer :/'
        return response
