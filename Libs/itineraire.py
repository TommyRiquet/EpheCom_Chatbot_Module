# -*- coding: utf-8 -*-

import openrouteservice

def itineraire():
    coords = ((4.72628927230835,50.69315719604492),(4.6121757,50.6658724))#(long,lat)départ, (long,lat)arrivée
    client = openrouteservice.Client(key='5b3ce3597851110001cf624842459ea605184a62ac2aa7283c08ccbf') # Clef personnelle
    routes = client.directions(coords)

    print(routes)
