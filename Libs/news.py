# -*- coding: utf-8 -*-

from googlesearch import search             #import google
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

        # Recuperation des recherches
        for url in search(str(query), tld='com', lang='fr', num=nbr_query, stop=nbr_query, pause=2):
            domain = urlparse(url).netloc
            if domain not in site:
                site.append(domain)
                response += '\n' + url
                link_increment += 1

        return response
