# -*- coding: utf-8 -*-

import openrouteservice

coords = ((4.72628927230835,50.69315719604492),(4.3831406,50.8385492))#(long,lat)départ, (long,lat)arrivée, coordonées présentes à titre d'exemple, toujours spécifier le numéro dans la rue

client = openrouteservice.Client(key='5b3ce3597851110001cf624842459ea605184a62ac2aa7283c08ccbf') # Clef personnelle
routes = client.directions(coords)

print(routes)
