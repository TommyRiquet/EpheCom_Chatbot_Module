# -*- coding: utf-8 -*-
# Python 3.9

import Libs.command as command
from Libs.meteo import Meteo
from Libs.news import News
from Libs.itineraire import Itineraire


def send_message(reponse):
    """
    Renvoie la valeur de retour
    """
    print(reponse)


class Chatbot:
    """
    Cette classe représente un module de Chatbot pour l'application Ephecom

    Author : T. Riquet,Q. Laruelle,S. Dziemianko
    Date : December 2021
    """

    def __init__(self):
        self.__command = ''
        self.__attribut1 = ''
        self.__attribut2 = ''
        self.__attribut3 = ''

    def get_command(self, message):
        """
        Cette méthode reçois les commandes du chat et va appeller les différents modules, en leurs passant les arguments

        PRE : message est un str
        POST : retourne la réponse à la commande
        RAISES :
        -ValueError : lorsque l'ont introduit de mauvais arguments
        -IndexError : Lors des splits , si l'argument est manquant
        -KeyError : Lorsque les APIs utilisées ont atteint la limite journalière autorisée

        """

        # HELP
        if message.find('!help') == 0:
            try:
                self.__attribut1 = message.split(' ')[1]
                return command.get_help(self.__attribut1)
            except(ValueError, IndexError, KeyError):
                return command.get_help()

        # METEO
        if message.find('!meteo') == 0:
            try:
                self.__attribut1 = message.split(' ')[1]
                return Meteo().get_meteo(self.__attribut1)
            except (ValueError, IndexError, KeyError):
                return "Ville manquante ou incorrecte (Ex: !meteo Paris)"

        # NEWS
        elif message.find('!news') == 0:

            try:
                self.__attribut1 = message[5:len(message) - 1]
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

        # ITINERAIRE
        elif message.find("!itineraire") == 0:
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
                return "adresse incorecte (Ex:!itineraire Rue de l'example 123 / Rue de l'HTML 456 /route )"

        # ADD
        elif message.find("!add") == 0:
            try:
                self.__command = message.split(' ')[1]
                self.__attribut1 = message[len(self.__command) + 6:]
                return command.add_lien(self.__command, self.__attribut1)
            except IndexError:
                return "Commande incorrecte => !add (nom de la commande) (ce qu'elle retourne)"

        # REM
        elif message.find("!rem") == 0:
            try:
                self.__command = message.split(' ')[1]
                return command.rem_lien(self.__command)
            except IndexError:
                return "Commande incorrecte => !rem (nom de la commande)"

        # OTHER COMMAND
        else:
            command.lien(message[1:])


chatbot = Chatbot()

message = '!'

if message[0] == '!':
    response = chatbot.get_command(message)
    if response is not None:
        send_message(response)
        
