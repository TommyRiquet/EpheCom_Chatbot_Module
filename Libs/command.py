import webbrowser
from Libs.meteo import Meteo
from Libs.news import News
from Libs.itineraire import Itineraire


list_commands = {"ephec": "https://portail.ephec.be/",
         "inginious": "https://inginious.ephec.be/",
         "tlca": "https://www.tlca.eu/"}


class Commande:
    """
        Ce module est utilisé pour les commandes du chatbot

        Author : T. Riquet
        Date : December 2021
    """
    def get_help(self, message):
        """
        Cette méthode renvoie la liste des commandes

        PRE : message est une chaine de caractère
        POST : renvoie les docstrings de chaque module + la liste des commandes + la liste des commandes personnalisées
        RAISES : /
        """

        # Get Modules Docstrings
        return_string = Meteo().__doc__ + News().__doc__ + Itineraire().__doc__
        return_string += 'add (Nom de la commande) (Ce quelle retourne)\n'\
                         'rem (Nom de la commande)\n'
        # Get List of commands
        if len(list_commands) > 0:
            return_string += '\nCommandes Personnalisées:\n'
            for command in list_commands:
                return_string += command + ' : ' + list_commands[command] + '\n'

        return return_string

    def add_command(self, message):
        """add (Nom de la commande) (attribut de la commande/Site web à ouvrir)"""
        try:
            command = message.split(' ')[1]
            attribut = ' '.join(message.split(' ')[2:])
            list_commands[command] = attribut
            return 'Commande "'+command+'" ajoutée avec succès'
        except IndexError:
            return self.add_command.__doc__

    def rem_command(self, message):
        """rem (Nom de la commande)"""
        try:
            command = message.split(" ")[1]
            for i in list_commands:
                if i == command:
                    del list_commands[command]
                    return 'Commande "' +command+'" supprimé avec succès'
        except IndexError:
            return self.rem_command.__doc__

    def commande_perso(self, command):
        """
        Cette méthode est utilisée pour appeler une commande personnalisée

        PRE : command est une chaine de caractères
        POST : Si attribut de command != lien url : renvoie l'attribut, sinon ouvre lien url
        Raises : KeyError : -Commande inconnue
        """
        try:
            for i in list_commands:
                if i == command:
                    if list_commands[command].find('http') == 0:
                        webbrowser.open(list_commands[command])
                    else:
                        return list_commands[command]
        except KeyError:
            pass

