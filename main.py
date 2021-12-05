# -*- coding: utf-8 -*-
# Python 3.9

import Libs.command as command
from Libs.meteo import Meteo
import Libs.news as news
import Libs.itineraire as itineraire


def send_message(reponse):
    """
    Renvoie la valeur de retour
    """
    print(reponse)


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
        Cette méthode reçois les commandes du chat et va appeller les différents modules, en leurs passant les arguments
        :param message: la commande de l'utilisateur
        :return response : la réponse à la commande de l'utilisateur
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
                meteo = Meteo()
                return meteo.get_meteo(self.__attribut1)
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
                    return news.news(self.__attribut1, self.__attribut2)
                else:
                    return news.news(self.__attribut1)

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

                return itineraire.get_itineraire(self.__attribut1, self.__attribut2, self.__attribut3)
            except (ValueError, IndexError, KeyError):
                return "adresse incorecte (Ex:!itineraire 38 rue de chaumont 1325 Longueville / 16 rue de basse-biez " \
                       "1390 grez-doiceau /route) "

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
    send_message(chatbot.get_command(message))