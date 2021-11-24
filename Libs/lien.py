import webbrowser

liens = {"ephec" : "https://portail.ephec.be/",
         "inginious" : "https://inginious.ephec.be/",
         "tlca" : "https://www.tlca.eu/"}


def add_lien(site,attr):
    liens[site] = attr
    print("Commande '"+site+"' ajouté avec succès")

def rem_lien(site):
    del liens[site]

def lien(site):
    try:
        print(liens[site])
    except KeyError:
        pass



