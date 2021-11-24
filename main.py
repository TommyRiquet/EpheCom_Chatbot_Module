# -*- coding: utf-8 -*-
import meteo
import news
import itineraire
import lien


def affichehelp():
    """
    Affiche une liste de commandes disponibles
    :return:
    """
    print("Commandes disponibles :\n!meteo (Ville)\n!news  (Sujet) (Nombre de sujet)\n!itineraire\n!add (nom de la "
          "commande) (retour de la commande)\n!rem  (nom de la commande)")


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

        elif choix.find("!add") == 0:
            name = ""
            attr = ""
            try:
                name = choix.split(' ')[1]
                attr = choix[len(name)+6:]
                lien.add_lien(name, attr)
            except IndexError:
                print("Commande incorrecte => !add (nom de la commande) (ce qu'elle retourne)")

        elif choix.find("!rem") == 0:
            name = ""
            try:
                name = choix.split(' ')[1]
                lien.rem_lien(name)
            except IndexError:
                print("Commande incorrecte => !rem (nom de la commande)")

        else:
            lien.lien(choix[1:])
