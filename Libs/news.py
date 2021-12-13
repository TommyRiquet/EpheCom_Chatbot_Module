# -*- coding: utf-8 -*-

from googlesearch import search             # Import Google
from urllib.parse import urlparse


class News:
    """
        Cette classe représente un module de News pour le Chatbot

        Author : T. Riquet,S. Dziemianko
        Date : December 2021
    """

    def get_news(self, query, nbr_query=1):
        """
        Cette methode recherche des résultats sur le web avec l'aide de la librairie Google

        PRE : query est un str, nbr_query est un entier optionnel
        POST : retourne les résultats de la cherche Google
        RAISES : /

        """
        link_increment = 0
        site = []
        response = ''

        # Recuperation des recherches
        for url in search(str(query), tld='com', lang='fr', num=nbr_query, stop=nbr_query, pause=2):
            domain = urlparse(url).netloc
            if domain not in site:
                site.append(domain)
                response += '\n' + url
                link_increment += 1

        return response
