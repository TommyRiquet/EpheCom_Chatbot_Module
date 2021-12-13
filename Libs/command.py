import webbrowser

"""
    Ce module est utilisé pour les commandes du chatbot

    Author : T. Riquet
    Date : December 2021
"""

liens = {"ephec": "https://portail.ephec.be/",
         "inginious": "https://inginious.ephec.be/",
         "tlca": "https://www.tlca.eu/"}

list_commands = {"meteo": "(Nom de la ville)",
                 "news": "(Sujet recheché) (Nombre d'articles à rechercher (max 10) )",
                 "itineraire": "(Addresse 1) / (Addresse 2) /route",
                 "add": "(Nom de le commande) (Retour de la commande )",
                 "rem": "(Nom de la commande)"
                 }


def get_help(command=''):
    return_command = ''
    # Obtenir l'intégralités des commandes
    if command == '':
        for command in list_commands:
            return_command += command + " " + list_commands[command] + '\n'

        for i in liens:
            return_command += '\n!' + i
        return return_command

    # Obtenir de l'aide pour une commande en particulier
    else:
        print(list_commands)
        return '!' + command + ' ' + list_commands[command]


def get_command():
    return_list = []
    for i in list_commands:
        return_list.append(i)
    return return_list


def add_command(command, attr):
    if attr.find('http') == 0:
        liens[command] = attr
        return 'Site Web "' + command + '" ajouté avec succès'
    else:
        list_commands[command] = attr
        return 'Commande "' + command + '" ajoutée avec succès'


def rem_command(command):
    for i in liens:
        if i == command:
            del liens[command]
            return 'Site Web supprimé avec succès'
    print(command)
    for i in list_commands:
        if i == command:
            del list_commands[command]
            return 'Commande supprimé avec succès'


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
