# -*- coding: utf-8 -*-

from googlesearch import search
from urllib.parse import urlparse


class News:
    """
news (Sujet) (Nombre de Sujet(min 1, max 10))
"""

    def get_news(self, message):
        """
        Cette methode recherche des résultats sur le web avec l'aide de la librairie Google

        PRE : query est un str, nbr_query est un entier optionnel
        POST : retourne les résultats de la recherche Google
        RAISES : ValueError: erreur lors de la récuperation du nombre de resultats attendu

        """
        link_increment = 0
        site = []
        response = ''
        a = 10
        b = 25

        # Récupération du sujet
        try:
            query = message[5:len(message) - 2]
            if query == " " or len(query) == 0:
                return self.__doc__
        except (ValueError, IndexError, KeyError):
            return self.__doc__
        # Récupération du nombre d'articles demandés
        try:
            nbr_query = [int(nbr) for nbr in message.split() if nbr.isdigit()][-2]
            if nbr_query <= 0:
                raise ValueError('Impossible de générer un nombre négatif de réponses')
        except (ValueError, IndexError, KeyError):
            nbr_query = 1

        if nbr_query > a:
            nbr_query = a

        # Recuperation des recherches
        for url in search(str(query), tld='com', lang='fr', num=b, stop=b, pause=1):
            domain = urlparse(url).netloc
            if domain not in site:
                site.append(domain)
                response += '\n' + url
                link_increment += 1

            if link_increment == nbr_query:
                return response
        if response != nbr_query:
            message = "Le temps alloué à la recherche à été excédé sans obtenir tout les resultats attendus. Possible" \
                      " qu'un nombre important de doublons se soit générés "
        return response + '\n' + message
