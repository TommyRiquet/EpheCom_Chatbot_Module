# -*- coding: utf-8 -*-

from googlesearch import search
from urllib.parse import urlparse


class News:

    def get_news(self, query, nbr_query=1):
        """
        Recherche des résultats sur le web avec l'aide de la librairie Google
        :param query: Le sujet de la recherche
        :param nbr_query: Le nombre de recherche
        :return:
        """
        link_increment = 0
        site = []
        response = ''
        a = 10

        if nbr_query > a:
            nbr_query = a

        # Recuperation des recherches
        for url in search(str(query), tld='com', lang='fr', num=25, stop=25, pause=2):
            domain = urlparse(url).netloc
            if domain not in site:
                site.append(domain)
                response += '\n' + url
                link_increment += 1

            if link_increment == nbr_query:
                return response


        message = "Le temps alloué à la recherche à été excédé sans obtenir tout les resultats attendus. Possible " \
                  "qu'un nombre important de doublons se soit générés "
        return response + '\n' + message
