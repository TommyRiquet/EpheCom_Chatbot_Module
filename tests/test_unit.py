from chatbot import Chatbot
from src.meteo import Meteo
from src.command import Commande
from src.news import News
import unittest


class ChatBotTest(unittest.TestCase):
    """
       Class de test pour la class Chatbot en utilisant la framework unittest

       Author: T. Riquet
       Date: November 2021
    """
    maxDiff = None

    def setUp(self):
        self.chatbot = Chatbot()

    def test_chatbot_help(self):
        """
            Cette méthode teste la méthode get_help du module Commande

            Author: T. Riquet
            Date: December 2021
        """

        # TEST INSTANCE
        self.assertIsInstance(self.chatbot, Chatbot, 'Test si chatbot est une instance de Chatbot()')

        # Test si le module commande renvoie la liste des commandes lorsqu'il ne recoit pas de message
        self.assertEqual(self.chatbot.get_command('!help'), Commande().get_help(''))

        # Test si le module commande renvoie la liste des commandes lorsqu'il recoit un message quelconque
        self.assertEqual(self.chatbot.get_command('!help'), Commande().get_help('help'))
        self.assertEqual(self.chatbot.get_command('!help'), Commande().get_help('test'))
        self.assertEqual(self.chatbot.get_command('!help'), Commande().get_help('123'))
        self.assertEqual(self.chatbot.get_command('!help'), Commande().get_help(0))
        self.assertEqual(self.chatbot.get_command('!help'), Commande().get_help(None))

    def test_chatbot_add(self):
        """
            Cette méthode teste la méthode add_command du module Commande

            Author: T. Riquet
            Date: December 2021
        """

        # Test si le chatbot n'envoie pas d'arguments à la méthode add_command du Chatbot
        self.assertEqual(self.chatbot.get_command('!add'), 'add (Nom de la commande) (attribut de la commande/Site '
                                                           'web à ouvrir)')

        # Test si la méthode ne recois pas d'arguments du Chatbot
        self.assertEqual(self.chatbot.get_command('!add'), Commande().add_command(""))

        # Test si l'on envoie une commande sans attribut
        self.assertEqual(self.chatbot.get_command('!add SansAttribut'), 'Veuillez entrer un attribut')
        self.assertEqual(self.chatbot.get_command('!add SansAttribut'), Commande().add_command("add SansAttribut"))

        # Test si l'on envoie une commande avec un attribut
        self.assertEqual(self.chatbot.get_command('!add bonjour salut'), 'Commande "bonjour" ajoutée avec succès')

        # Test si on essaie de créer une commande qui existe déja
        self.assertEqual(self.chatbot.get_command('!add bonjour salut'), 'Commande "bonjour" existe déja avec '
                                                                         'l\'attribut "salut"')

        # Test si l'on envoie une commande avec un lien http comme attribut
        self.assertEqual(self.chatbot.get_command('!add youtube https://youtube.com'), 'Commande "youtube" ajoutée '
                                                                                       'avec succès')
        # Test si on essaie de créer une commande qui existe déja avec un lien comme attribut
        self.assertEqual(self.chatbot.get_command('!add youtube https://youtube.com'), 'Commande "youtube" existe '
                                                                                       'déja avec l\'attribut '
                                                                                       '"https://youtube.com"')

    def test_chatbot_rem(self):
        """
            Cette méthode teste la méthode rem_command du module Commande

            Author: T. Riquet
            Date: December 2021
        """

        # Test si le chatbot envoie la commande rem sans argument
        self.assertEqual(self.chatbot.get_command('!rem'), 'rem (Nom de la commande)')

        # Test si la méthode rem_command ne recoit pas d'argument
        self.assertEqual(self.chatbot.get_command('!rem'), Commande().rem_command(''))

        # Test si l'on supprime une commande
        self.assertEqual(self.chatbot.get_command('!rem ephec'), 'Commande "ephec" supprimé avec succès')
        self.assertEqual(self.chatbot.get_command('!rem tlca'), 'Commande "tlca" supprimé avec succès')

        # Test si l'on supprime une commande personnalisé
        self.chatbot.get_command('!add test testAttribut')
        self.assertEqual(self.chatbot.get_command('!rem test'), 'Commande "test" supprimé avec succès')

        # Test si l'on supprime une commande qui n'existe pas
        self.assertEqual(self.chatbot.get_command('!rem commandeQuiNexistePas'), 'Commande "commandeQuiNexistePas" '
                                                                                 'Introuvable')

    def test_chatbot_meteo(self):
        """
            Cette méthode teste le Module Meteo du chatbot

            Author: T. Riquet
            Date: December 2021
        """

        # Test si le chatbot n'envoie pas d'argument au module Meteo
        self.assertEqual(self.chatbot.get_command('!meteo'), '\nmeteo (Nom de la Ville)\n')

        # Test si le module Meteo ne recois pas d'argument
        self.assertEqual(self.chatbot.get_command('!meteo'), Meteo().get_meteo(""))

        # Test Avec API
        """
        # Test si le module trouve les villes passées en argument
        self.assertNotEqual(self.chatbot.get_command('!meteo Paris'), 'Ville Introuvable')
        self.assertNotEqual(self.chatbot.get_command('!meteo Bruxelles'), 'Ville Introuvable')
        self.assertNotEqual(self.chatbot.get_command('!meteo Perwez'), 'Ville Introuvable')

        # Test si le module recoit une ville qui n'existe pas
        self.assertEqual(self.chatbot.get_command('!meteo VilleQuiNexistePas'), 'Ville Introuvable')

        # Test si le module recoit un code postal 
        self.assertNotEqual(self.chatbot.get_command('!meteo 1360'), 'Ville Introuvable')
        self.assertNotEqual(self.chatbot.get_command('!meteo 1000'), 'Ville Introuvable')

        """

    def test_chatbot_itineraire(self):
        """
        Cette méthode teste la commande !itineraire du chatbot

        Author: Q. Laruelle
        Date: december 2021
        """
        """
                clefs utilisation normale: 9744eec549f1c82b18af8a10f26d1489 ou 143323c5ab5dfe15ec89b2bbb320bea7
                clef API de test: 3bbc0c5c02b03a7e43723288f3de55fe ou bb19b66d645ba9c738d69f239b2808ec
        """
        chatbot_itineraire = Chatbot()

        #Test Sans API
        self.assertEqual(chatbot_itineraire.get_command('!itineraire'),'\nitineraire (Adresse 1) / (Adresse 2) /route\n\n')
        self.assertEqual(chatbot_itineraire.get_command('itineraire'), None)
        self.assertEqual(chatbot_itineraire.get_command('!itineraire rue de chaumont 41 1325 Longueville, rue notre dame 65 Perwez'),'\nitineraire (Adresse 1) / (Adresse 2) /route\n\n')

        #Test Avec API
        """
        self.assertEqual(chatbot_itineraire.get_command('!itineraire rue de chaumont 41 1325 Longueville / rue notre-Dame 65 '
                                             'Perwez'),'')
        self.assertEqual(chatbot_itineraire.get_command('!itineraire rue de chaumont 41 1325 Longueville / rue notre-Dame 65 '
                                             'Perwez / route'),'')
        self.assertEqual(chatbot_itineraire.get_command('!itineraire rue de chaumont 41 1325 Longueville / Palais12'),'')
        self.assertEqual(chatbot_itineraire.get_command('!itineraire rue de chaumont 41 1325 Longueville / Palais12 / route'),'')
        self.assertEqual(chatbot_itineraire.get_command('!itineraire ahfdohvosn / jean'),'')
        self.assertEqual(chatbot_itineraire.get_command('!itineraire ahfdohvosn / jean / route'),'')
        self.assertEqual(chatbot_itineraire.get_command('!itineraire ahfdohvosn / rue de chaumont 41 1325 Longueville'),'')
        self.assertEqual(chatbot_itineraire.get_command('!itineraire ahfdohvosn / rue de chaumont 41 1325 Longueville / route'),'')
        self.assertEqual(chatbot_itineraire.get_command('!itineraire ahfdohvosn 42 jacques / rue de chaumont 41 1325 Longueville'),)
        self.assertEqual(chatbot_itineraire.get_command('!itineraire ahfdohvosn 42 jacques / rue de chaumont 41 1325 Longueville '
                                             '/ route'),)
        self.assertEqual(chatbot_itineraire.get_command('!itineraire ahfdohvosn / Palais12'),)
        self.assertEqual(chatbot_itineraire.get_command('!itineraire ahfdohvosn / Palais12 / route'),)
        self.assertEqual(chatbot_itineraire.get_command('!itineraire rue de chaumont 41 1325 Longueville '
                                             '/ 145 Brooklyn Ave, Brooklyn, NY 11213, États-Unis / route'),)
        self.assertEqual(chatbot.get_command('!itineraire rue de chaumont 41 1325 Longueville '
                                             '/ 145 Brooklyn Ave, Brooklyn, NY 11213, États-Unis'),)
        self.assertEqual(chatbot.get_command('!itineraire 125489632145 / Palais12'),)
        self.assertEqual(chatbot.get_command('!itineraire 125489632145 / Palais12 / route'),)
        """

    def test_chatbot_news(self):
        """
        Cette methode test le module !news du chatbot

        Author : S. Dziemianko
        Date : December 2021
        """
        self.assertEqual(self.chatbot.get_command('!news'), 'news (Sujet) (Nombre de Sujet)')
        self.assertEqual(self.chatbot.get_command('!news'), News().get_news(""))

        self.assertEqual(self.chatbot.get_command('!news IT 3'), 3)
        self.assertEqual(self.chatbot.get_command('!news IT 15'), 10)

        with self.assertRaises(ValueError):
            self.chatbot.get_command('!news IT 0'), 0
        with self.assertRaises(IndexError):
            self.chatbot.get_command('!news IT 0'), 0
        with self.assertRaises(KeyError):
            self.chatbot.get_command('!news IT 0'), 0


if __name__ == '__main__':

    unittest.main()
