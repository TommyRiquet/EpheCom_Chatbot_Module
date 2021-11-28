import webbrowser

liens = {"ephec": "https://portail.ephec.be/",
         "inginious": "https://inginious.ephec.be/",
         "tlca": "https://www.tlca.eu/"}

list_commands = {"!meteo": "(Ville)",
                 "!news": "(Sujet) (Nombre de sujet)",
                 "!itineraire": "(Addresse 1) (Addresse 2)",
                 "!add": "(Nom de le commande) (Retour de la commande)",
                 "!rem": "(Nom de la commande)"}


def get_help(command=''):
    return_command = ''
    if command == '':

        for command in list_commands:
            return_command += '\n'+command + " " + list_commands[command]

        for i in liens:
            return_command += '\n!'+i
        print(return_command)

    else:
        return_command += '!'+command + ' ' + list_commands['!'+command]
        print(return_command)


def add_lien(command,attr):
    if attr.find('http') == 0:
        liens[command] = attr
    else:
        list_commands[command] = attr
    print("Commande '"+command+"' ajouté avec succès")


def rem_lien(command):
    for i in liens:
        if i == command:
            del liens[command]

    for i in list_commands:
        if i == command:
            del list_commands[command]


def lien(command):
    try:
        for i in liens:
            if i == command:
                webbrowser.open(liens[command])
    except KeyError:
        pass

    try:
        for i in list_commands:
            if i == command:
                print(list_commands[command])
    except KeyError:
        pass
