# -*- coding: utf-8 -*-
# Python 3.10

from Libs.command import Commande
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
        self.__list_command = {'help': Commande().get_help, 'meteo': Meteo().get_meteo, 'news': News().get_news,
                               'itineraire': Itineraire().get_itineraire, 'add': Commande().add_command,
                               'rem': Commande().rem_command}
        self.__attribut1 = ''
        self.__attribut2 = ''
        self.__attribut3 = ''

    def get_command(self, message):
        """
        Cette classe appelle les différents modules et renvoie la réponse

        PRE : message est une chaine de caractères
        POST : renvoie la réponse du module correspondant à la commande
        RAISES : /
        """
        if message.find('!') == 0:
            message = message[1:]
            for command in self.__list_command:
                if message.find(command) == 0:
                    return self.__list_command[command](message)
            return Commande().commande_perso(message)
        else:
            pass


"""
chatbot = Chatbot()

message = "!"
reponse = chatbot.get_command(message)
if reponse is not None:
    print(reponse)
"""
