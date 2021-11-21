# -*- coding: utf-8 -*-
import openrouteservice

coords = ((8.34234,48.23424),(8.34423,48.26424))

client = openrouteservice.Client(key='5b3ce3597851110001cf624842459ea605184a62ac2aa7283c08ccbf') # Specify your personal API key
routes = client.directions(coords)

print(routes)
