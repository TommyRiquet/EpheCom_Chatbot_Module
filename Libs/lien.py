import webbrowser


def lien():
    site = input('Quel site souhaitez vous ouvrir? ')
    if(site == "ephec"):
        webbrowser.open("https://portail.ephec.be/")
    elif(site == "tlca"):
        webbrowser.open("https://www.tlca.eu/courses")
    elif(site == "inginious"):
        webbrowser.open("https://inginious.ephec.be/courselist")


lien()
