# -*- coding: utf-8 -*-

import openrouteservice
import requests

class itineraire:
    def get_itineraire(adresse1, adresse2, arg):
        """
        Récupere les coordonneés GPS à partir de deux addresses données
        Calcul le temps de trajet , ainsi que la durée et les affiche
        :return:
        """

        lat1, lat2, long1, long2 = 0, 0, 0, 0
        response = ''
        # ADDR TO COOORD
        # https://maps.open-street.com/api/geocoding/?address="+adr+"&sensor=false&key=143323c5ab5dfe15ec89b2bbb320bea7

        # ADDRESSE 1
        addr1 = adresse1
        url_addr1 = "https://maps.open-street.com/api/geocoding/?address=" + addr1 + "&sensor=false&key" \
                                                                                     "=143323c5ab5dfe15ec89b2bbb320bea7 "
        r_addr1 = requests.get(url_addr1)
        coord1 = r_addr1.json()
        try:
            lat1 = float(coord1['results'][0]['geometry']['location']['lat'])
            long1 = float(coord1['results'][0]['geometry']['location']['lng'])
        except KeyError:
            response ="Erreur lors de la récupération des coordonnées de l'adresse n°1"

        # ADDRESSE 2
        addr2 = adresse2
        url_addr2 = "https://maps.open-street.com/api/geocoding/?address=" + addr2 + "&sensor=false&key=143323c5ab5dfe15ec89b2bbb320bea7"
        r_addr2 = requests.get(url_addr2)
        coord2 = r_addr2.json()
        try:
            lat2 = float(coord2['results'][0]['geometry']['location']['lat'])
            long2 = float(coord2['results'][0]['geometry']['location']['lng'])
        except KeyError:
            response = "Erreur lors de la récupération des coordonnées de l'adresse n°2"

        # COORD TO TIME AND DISTANCE
        # https://maps.open-street.com/api/route/?origin="+coord1x+","+coord1y+"&destination="+coord2x+","+coord2y+"&mode=driving&key=143323c5ab5dfe15ec89b2bbb320bea7
        url_final = "https://maps.open-street.com/api/route/?origin=" + str(lat1) + "," + str(
            long1) + "&destination=" + str(lat2) + "," + str(long2) + "&mode=driving&key=143323c5ab5dfe15ec89b2bbb320bea7"
        r_final = requests.get(url_final)
        data = r_final.json()
        distance = data['total_distance']
        time = data['total_time']

        response = "\ndistance en km : " + str(distance / 1000)

        heure = int(time / 3600)
        minutes = int((time % 3600) / 60)
        secondes = int((time % 3600) % 60)

        response += "\ntemps de trajet : " + str(heure) + "h " + str(minutes) + "m " + str(secondes) + "s"

        # Calculating a route from two coordinates
        if arg == "route":
            coords = ((long1, lat1), (long2, lat2))  # (long,lat)départ, (long,lat)arrivée
            client = openrouteservice.Client(key='5b3ce3597851110001cf624842459ea605184a62ac2aa7283c08ccbf')  # Clef personnelle
            routes = client.directions(coords)
            for i in routes["routes"]:
                for j in i['segments']:
                    for k in j['steps']:
                        response += ("\n"+k['instruction'])

        return response