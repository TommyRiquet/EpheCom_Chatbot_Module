# -*- coding: utf-8 -*-
# Python 3.9

import Libs.command as command
import Libs.meteo as meteo
import Libs.news as news
import Libs.itineraire as itineraire


class Chatbot:
    """
    Cette classe est un module de Chatbot pour l'application Ephecom
    """

    def __init__(self):
        self.__command = ''
        self.__attribut1 = ''
        self.__attribut2 = ''
        self.__attribut3 = ''

    def get_command(self, message):
        """
        Cette méthode récupere les entrées du chat et vérifie s'il s'agit de commande
        :param message: le message du chat
        :return:
        """
        if message.find('!help') == 0:
            try:
                self.__attribut1 = message.split(' ')[1]
                command.get_help(self.__attribut1)
            except(ValueError, IndexError, KeyError):
                command.get_help()

        if message.find('!meteo') == 0:
            try:
                self.__attribut1 = message.split(' ')[1]
                meteo.meteo(self.__attribut1)
            except (ValueError, IndexError, KeyError):
                print("Ville manquante ou incorrecte (Ex: !meteo Paris)")

        elif message.find('!news') == 0:

            try:
                self.__attribut1 = message[5:len(message) - 1]
                if self.__attribut1 == " " or len(self.__attribut1) == 0:
                    print("Sujet invalide (Ex :!news IT 2)")
            except (ValueError, IndexError, KeyError):
                print("Sujet invalide (Ex :!news IT 2)")

            try:
                array_nbr = [int(nbr) for nbr in message.split() if nbr.isdigit()]
                self.__attribut2 = int(array_nbr[len(array_nbr) - 1])
            except (ValueError, IndexError, KeyError):
                self.__attribut2 = 0

            else:
                if self.__attribut2 > 0 and self.__attribut2 is not None and self.__attribut1 is not None:
                    news.news(self.__attribut1, self.__attribut2)
                else:
                    news.news(self.__attribut1)

        elif message.find("!itineraire") == 0:
            try:
                self.__attribut1 = message.split(", ")[1].replace(" ","")
                self.__attribut2 = message.split(", ")[2].replace(" ","")
                self.__attribut3 = message.split(", ")[3]
                itineraire.itineraire(self.__attribut1, self.__attribut2, self.__attribut3)
            except (ValueError, IndexError, KeyError):
                print("adresse incorecte (Ex:!itineraire, 38 rue de chaumont 1325 Longueville, 16 rue de basse-biez 1390 grez-doiceau, 1)")

        elif message.find("!add") == 0:
            try:
                self.__command = message.split(' ')[1]
                self.__attribut1 = message[len(self.__command) + 6:]
                command.add_lien(self.__command, self.__attribut1)
            except IndexError:
                print("Commande incorrecte => !add (nom de la commande) (ce qu'elle retourne)")

        elif message.find("!rem") == 0:
            try:
                self.__command = message.split(' ')[1]
                command.rem_lien(self.__command)
            except IndexError:
                print("Commande incorrecte => !rem (nom de la commande)")

        else:
            command.lien(message[1:])


chatbot = Chatbot()
