import webbrowser

"""
    Ce module est utilisé pour les commandes du chatbot

    Author : T. Riquet
    Date : December 2021
"""

liens = {"ephec": "https://portail.ephec.be/",
         "inginious": "https://inginious.ephec.be/",
         "tlca": "https://www.tlca.eu/"}

list_commands = {"meteo": "(Nom de la ville) : Affiche la meteo d'une ville ",
                 "news": "(Sujet recheché) (Nombre d'articles à rechercher) : Recherche des articles sur Google à "
                          "partir d'un sujet et d'un nombre d'articles à rechercher",
                 "itineraire": "(Addresse 1) / (Addresse 2) /route : Calcule la durée et la distance entre deux "
                                "addresses, et peut afficher la route à suivre avec l'argument '/route'",
                 "add": "(Nom de le commande) (Retour de la commande ) : Ex:'!add portail "
                         "https://portail.ephec.com', '!add salut bonjour comment allez vous ?'",
                 "rem": "(Nom de la commande) : Supprime la commande personnalisée en fonction de sa commande"
                 }


def get_help(command=''):
    return_command = ''
    if command == '':

        for command in list_commands:
            return_command += '\n' + command + " " + list_commands[command]

        for i in liens:
            return_command += '\n!' + i
        return return_command

    else:
        return_command += '!' + command + ' ' + list_commands['!' + command]
        return return_command


def get_command():
    return_list=[]
    for i in list_commands:
        return_list.append(i)
    return return_list


def add_lien(command, attr):
    if attr.find('http') == 0:
        liens[command] = attr
        return 'Site Web "' + command + '" ajouté avec succes'
    else:
        list_commands[command] = attr
        return 'Commande "' + command + '" ajoutée avec succes'


def rem_lien(command):
    for i in liens:
        if i == command:
            del liens[command]
            return 'Site Web supprimée avec succes'

    for i in list_commands:
        if i == command:
            del list_commands[command]
            return 'Commande supprimée avec succes'


def lien(command):
    try:
        for i in liens:
            if i == command:
                webbrowser.open(liens[command])
                return 'Site Web ' + i + ' ouvert'
    except KeyError:
        pass

    try:
        for i in list_commands:
            if i == command:
                return list_commands[command]
    except KeyError:
        pass
