# -*- coding: utf-8 -*-

from googlesearch import search


def news(query, nbr_query=1):
    """
    Recherche des résultats sur le web avec l'aide de la librairie Google
    :param query: Le sujet de la recherche
    :param nbr_query: Le nombre de recherche
    :return:
    """
    response = ''

    # Recuperation des recherches
    for liens in search(query, tld='com', lang='fr', num=nbr_query, stop=nbr_query, pause=2):
        response += '\n'+liens

    return response
