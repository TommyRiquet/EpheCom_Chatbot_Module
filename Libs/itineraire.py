# -*- coding: utf-8 -*-

from pyroutelib3 import Router


def itineraire():
    """
    Fonction itinéraire qui
    :return:
    """
    lat1 = input("Entrez la latitude de la ville de départ")
    lon1 = input("Entrez la longitude de la ville de départ")
    lat2 = input("Entrez la latitude de la ville d'arrivée")
    lon2 = input("Entrez la longitude de la ville d'arrivée")
    # moyen de transport
    router = Router("car")
    start = router.findNode(lat1, lon1)
    finish = router.findNode(lat2, lon2)
    status, route = router.doRoute(start, finish)
    if status == 'success':
        pathLatLons = list(map(router.nodeLatLon, route))
        #affichage des couples de coordonées jusqu'à la destination
        print(pathLatLons)
