from chatbot import Chatbot
import unittest

chatbot = Chatbot()

class ChatBotTest(unittest.TestCase):
    """
       Class de test pour la class Chatbot en utilisant la framework unittest

       Author: T. Riquet
       Date: November 2021
    """
    def test_chatbot_help(self):
        self.assertEqual(chatbot.get_command('!help meteo'), "!meteo (Nom de la ville) : Affiche la meteo d'une ville ")
        self.assertEqual(chatbot.get_command('!help news'), "!news (Sujet recheché) (Nombre d'articles à rechercher) "
                                                            ": Recherche des articles sur Google à partir d'un sujet "
                                                            "et d'un nombre d'artciles à rechercher")
        self.assertEqual(chatbot.get_command('!help itineraire'), "!itineraire (Addresse 1) / (Addresse 2) /route : "
                                                                  "Calcul la durée et la distance entre deux "
                                                                  "addresses, et peut afficher la route à suivre avec "
                                                                  "l'argument '/route'")
        self.assertEqual(chatbot.get_command('!help add'), "!add (Nom de le commande) (Retour de la commande ) : "
                                                           "Ex:'!add portail https://portail.ephec.com', '!add salut "
                                                           "bonjour comment allez vous ?'")
        self.assertEqual(chatbot.get_command('!help rem'), "!rem (Nom de la commande) : Supprime la commande "
                                                           "personnalisé en fonction de sa commande")

    def test_chatbot_meteo(self):
        self.assertEqual(chatbot.get_command('!meteo'), 'Ville manquante ou incorrecte (Ex: !meteo Paris)')

    def test_chatbot_news(self):
        self.assertEqual(chatbot.get_command('!news'), 'Sujet invalide (Ex :!news IT 2)')

    def test_chatbot_itineraire(self):
        self.assertEqual(chatbot.get_command('!itineraire'), "adresse incorecte (Ex:!itineraire Rue de l'example 123 "
                                                             "/ Rue de l'HTML 456 /route )")

    def test_chatbot_add(self):
        self.assertEqual(chatbot.get_command('!add'), "Commande incorrecte => !add (nom de la commande) (ce qu'elle "
                                                      "retourne)")
        self.assertEqual(chatbot.get_command('!add test test.com'), 'Commande "test" ajoutée avec succes')
        self.assertEqual(chatbot.get_command('!add bonjour salut'), 'Commande "bonjour" ajoutée avec succes')

    def test_chatbot_rem(self):
        self.assertEqual(chatbot.get_command('!rem'), 'Commande incorrecte => !rem (nom de la commande)')
        self.assertEqual(chatbot.get_command('!rem ephec'), 'Site Web supprimée avec succes')
        self.assertEqual(chatbot.get_command('!rem tlca'), 'Site Web supprimée avec succes')


if __name__ == '__main__':
    unittest.main()
