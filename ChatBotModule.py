# -*- coding: utf-8 -*-
import meteo
import news
import itineraire


def affichehelp():
    """
    Affiche une liste de commandes disponibles
    :return:
    """
    print("Commandes disponibles :\n!meteo\n!news\n!itineraire\n")


if __name__ == "__main__":

    choix = ""

    while choix != '0':

        # Récupération des entrées utilisateurs
        choix = input()

        # Différents choix possibles
        if choix.find('!help') == 0:
            affichehelp()

        elif choix.find('!meteo') == 0:

            try:
                ville = choix.split(' ')[1]
                meteo.meteo(ville)
            except (ValueError, IndexError, KeyError):
                print("Ville manquante ou incorrecte (Ex: !meteo Paris)")

        elif choix.find('!news') == 0:

            subject = ""
            nbr = 0
            try:
                array_nbr = [int(nbr) for nbr in choix.split() if nbr.isdigit()]
                nbr = int(array_nbr[len(array_nbr)-1])
            except (ValueError, IndexError, KeyError):
                nbr = 0

            try:
                subject = choix[5:len(choix)-1]
                if subject == " " or len(subject) == 0:
                    print("Sujet invalide (Ex :!news IT 2)")
            except (ValueError, IndexError, KeyError):
                print("Sujet invalide (Ex :!news IT 2)")

            else:
                if nbr > 0 and nbr is not None and subject is not None:
                    news.news(subject, nbr)
                else:
                    news.news(subject)

        elif choix.find("!itineraire") == 0:

            itineraire.itineraire()

