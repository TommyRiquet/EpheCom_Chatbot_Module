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
        self.__found_command = False
        self.__attribut1 = ''
        self.__attribut2 = ''
        self.__attribut3 = ''

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

        for commmand in self.__list_command:
            if commmand == com:
                return self.__list_command[commmand](message)

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
                    self.__found_command = True
                    return self.call_module(coms, message)
            return Commande().commande_perso(message)
        else:
            pass


"""
chatbot = Chatbot()

message = ""
reponse = chatbot.get_command(message)
if reponse is not None:
    print(reponse)
"""