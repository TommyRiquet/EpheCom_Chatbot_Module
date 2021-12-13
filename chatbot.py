# -*- coding: utf-8 -*-
# Python 3.10

import Libs.command as command
from Libs.meteo import Meteo
from Libs.news import News
from Libs.itineraire import Itineraire


class Chatbot:
    """
    Cette classe représente un module de Chatbot pour l'application Ephecom

    Author : T. Riquet, Q. Laruelle, S. Dziemianko
    Date : December 2021
    """

    def __init__(self):
        """
        PRE : /
        POST : /
        """
        self.__list_command = ['help', 'meteo', 'news', 'itineraire', 'add', 'rem']
        self.__command = ''
        self.__attribut1 = ''
        self.__attribut2 = ''
        self.__attribut3 = ''

    def mod_meteo(self, message):
        try:
            self.__attribut1 = message.split(' ')[1]
            return Meteo().get_meteo(self.__attribut1)
        except (ValueError, IndexError, KeyError):
            return "Ville manquante ou incorrecte (Ex: !meteo Paris)"

    def mod_news(self, message):
        try:
            self.__attribut1 = message[5:len(message) - 2]
            if self.__attribut1 == " " or len(self.__attribut1) == 0:
                return "Sujet invalide (Ex :!news IT 2)"
        except (ValueError, IndexError, KeyError):
            return "Sujet invalide (Ex :!news IT 2)"

        try:
            array_nbr = [int(nbr) for nbr in message.split() if nbr.isdigit()]
            self.__attribut2 = int(array_nbr[len(array_nbr) - 1])
        except (ValueError, IndexError, KeyError):
            self.__attribut2 = 0

        else:
            if self.__attribut2 > 0 and self.__attribut2 is not None and self.__attribut1 is not None:
                return News().get_news(self.__attribut1, self.__attribut2)
            else:
                return News().get_news(self.__attribut1)

    def mod_itineraire(self, message):
        try:
            self.__attribut1 = message.split("/")[0]
            self.__attribut1 = self.__attribut1[12:]
            self.__attribut2 = message.split("/")[1]
            try:
                self.__attribut3 = message.split("/")[2]
            except (ValueError, IndexError, KeyError):
                self.__attribut3 = 0

            return Itineraire().get_itineraire(self.__attribut1, self.__attribut2, self.__attribut3)
        except (ValueError, IndexError, KeyError):
            return "adresse incorrecte (Ex:!itineraire Rue de l'example 123 / Rue de l'HTML 456 /route )"

    def mod_commande(self, message):
        # HELP

        if message.find('help') == 0:
            try:
                self.__attribut1 = message.split(' ')[1]
                return command.get_help(self.__attribut1)
            except IndexError:

                return command.get_help()

        # ADD
        elif message.find('add') == 0:
            try:
                self.__command = message.split(' ')[1]
                self.__attribut1 = message[len(self.__command) + 6:]
                response = command.add_command(self.__command, self.__attribut1)
                self.__list_command = command.get_command()
                return response
            except IndexError:
                return "!add (nom de la commande) (ce qu'elle retourne)"


        # REM
        elif message.find('rem') == 0:
            try:
                self.__attribut1 = message.split(' ')[1]
                return command.rem_command(self.__attribut1)
            except IndexError:
                return "!rem (Nom de la commande)"

    def call_module(self, com, message):
        """
        Cette classe appelle les différents modules et renvoie la réponse

        PRE : com est la commande utilisée par l'utilisateur et message contient les arguments(optionnel)
        POST : renvoie la réponse du module correspondant
        RAISES :
        -ValueError : lorsque l'ont introduit de mauvais arguments
        -IndexError : Lors des splits, si l'argument est manquant
        -KeyError : Lorsque les APIs utilisées ont atteint la limite journalière autorisée
        """

        if com == 'help' or com == 'add' or com == 'rem':

            return self.mod_commande(message)

        elif com == 'meteo':
            return self.mod_meteo(message)

        elif com == 'news':
            return self.mod_news(message)

        elif com == 'itineraire':
            return self.mod_itineraire(message)

        else:
            return command.lien(message[1:])

    def get_command(self, message):
        """
        Cette méthode reçoit les commandes du chat et va appeller les différents modules, en leur passant les arguments

        PRE : message est un str
        POST : retourne la réponse à la commande

        """
        if message.find('!') == 0:
            # Recherche d'une commande dans le message
            message = message[1:]
            for coms in self.__list_command:
                if message.find(coms) == 0:
                    return self.call_module(coms, message)
        else:
            pass
