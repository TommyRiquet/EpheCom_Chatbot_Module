import webbrowser


def lien():
    site = input('Quel site souhaitez vous ouvrir? ')
    if(site.lower() == "ephec"):
        webbrowser.open("https://portail.ephec.be/")
    elif(site.lower() == "tlca"):
        webbrowser.open("https://www.tlca.eu/courses")
    elif(site.lower() == "inginious"):
        webbrowser.open("https://inginious.ephec.be/courselist")


lien()
