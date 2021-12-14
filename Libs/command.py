import webbrowser
from Libs.meteo import Meteo
from Libs.news import News
from Libs.itineraire import Itineraire

"""
    Ce module est utilisé pour les commandes du chatbot

    Author : T. Riquet
    Date : December 2021
"""

list_commands = {"ephec": "https://portail.ephec.be/",
         "inginious": "https://inginious.ephec.be/",
         "tlca": "https://www.tlca.eu/"}


class Commande:
    def get_help(self, message):

        # Get Modules Docstrings
        return_string = Meteo().__doc__ + News().__doc__ + Itineraire().__doc__
        return_string += 'add (Nom de la commande) (Ce quelle retourne)\n'\
                         'addweb (Nom de la commande) (Site Web)\n'\
                         'rem (Nom de la commande)\n'
        # Get List of commands
        if len(list_commands) > 0:
            return_string += '\nCommandes Personnalisées:\n'
            for command in list_commands:
                return_string += command + ' : ' + list_commands[command] + '\n'

        return return_string

    def add_command(self, message):
        command = message.split(' ')[1]
        attribut = ' '.join(message.split(' ')[2:])
        list_commands[command] = attribut
        return 'Commande "'+command+'" ajoutée avec succès'

    def rem_command(self, message):
        command = message.split(" ")[1]

        for i in list_commands:
            if i == command:
                del list_commands[command]
                return 'Commande "' +command+'" supprimé avec succès'

    def commande_perso(self, command):

        try:
            for i in list_commands:
                if i == command:
                    if list_commands[command].find('http') == 0:
                        webbrowser.open(list_commands[command])
                    else:
                        return list_commands[command]
        except KeyError:
            pass
