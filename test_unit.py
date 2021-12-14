from chatbot import Chatbot
import unittest


class ChatBotTest(unittest.TestCase):
    """
       Class de test pour la class Chatbot en utilisant la framework unittest

       Author: T. Riquet
       Date: November 2021
    """
    maxDiff = None

    def test_chatbot_meteo(self):
        """
            Cette méthode teste la commande !meteo du chatbot

            Author: T. Riquet
            Date: December 2021
        """
        # Test sans API
        self.assertEqual(chatbot.get_command('!meteo'), '\nmeteo (Nom de la Ville)\n')

        # Test Avec API
        """
        self.assertEqual(chatbot.get_command('!meteo VilleQuiNexistePas'), 'Ville Introuvable')
        """

    def test_chatbot_add(self):
        """
            Cette méthode teste la commande !add du chatbot

            Author: T. Riquet
            Date: December 2021
        """
        self.assertEqual(chatbot.get_command('!add'), 'add (Nom de la commande) (attribut de la commande/Site web à '
                                                      'ouvrir)')
        self.assertEqual(chatbot.get_command('!add test test.com'), 'Commande "test" ajoutée avec succès')
        self.assertEqual(chatbot.get_command('!add bonjour salut'), 'Commande "bonjour" ajoutée avec succès')

    def test_chatbot_rem(self):
        """
            Cette méthode teste la commande !rem du chatbot

            Author: T. Riquet
            Date: December 2021
        """
        self.assertEqual(chatbot.get_command('!rem'), 'rem (Nom de la commande)')
        self.assertEqual(chatbot.get_command('!rem ephec'), 'Commande "ephec" supprimé avec succès')
        self.assertEqual(chatbot.get_command('!rem tlca'), 'Commande "tlca" supprimé avec succès')

    def test_chatbot_itineraire(self):
        """
        Cette méthode teste la commande !itineraire du chatbot

        Author: Q. Laruelle
        Date: december 2021
        """

        """
        clefs utilisation normale: 9744eec549f1c82b18af8a10f26d1489 ou 143323c5ab5dfe15ec89b2bbb320bea7
        """

        self.assertEqual(chatbot.get_command('!itineraire'),'\nitineraire (Adresse 1) / (Adresse 2) /route\n\n')
        self.assertEqual(chatbot.get_command('itineraire'), None)
        self.assertEqual(chatbot.get_command('!itineraire rue de chaumont 41 1325 Longueville, rue notre dame 65 Perwez'),'\nitineraire (Adresse 1) / (Adresse 2) /route\n\n')
        """
        A partir de la ligne suivante utiliser une clef API de test: 3bbc0c5c02b03a7e43723288f3de55fe ou bb19b66d645ba9c738d69f239b2808ec
        """
        """
        self.assertEqual(chatbot.get_command('!itineraire rue de chaumont 41 1325 Longueville / rue notre-Dame 65 '
                                             'Perwez'),'')
        self.assertEqual(chatbot.get_command('!itineraire rue de chaumont 41 1325 Longueville / rue notre-Dame 65 '
                                             'Perwez / route'),'')
        self.assertEqual(chatbot.get_command('!itineraire rue de chaumont 41 1325 Longueville / Palais12'),'')
        self.assertEqual(chatbot.get_command('!itineraire rue de chaumont 41 1325 Longueville / Palais12 / route'),'')
        self.assertEqual(chatbot.get_command('!itineraire ahfdohvosn / jean'),'')
        self.assertEqual(chatbot.get_command('!itineraire ahfdohvosn / jean / route'),'')
        self.assertEqual(chatbot.get_command('!itineraire ahfdohvosn / rue de chaumont 41 1325 Longueville'),'')
        self.assertEqual(chatbot.get_command('!itineraire ahfdohvosn / rue de chaumont 41 1325 Longueville / route'),'')
        self.assertEqual(chatbot.get_command('!itineraire ahfdohvosn 42 jacques / rue de chaumont 41 1325 Longueville'),)
        self.assertEqual(chatbot.get_command('!itineraire ahfdohvosn 42 jacques / rue de chaumont 41 1325 Longueville '
                                             '/ route'),)
        self.assertEqual(chatbot.get_command('!itineraire ahfdohvosn / Palais12'),)
        self.assertEqual(chatbot.get_command('!itineraire ahfdohvosn / Palais12 / route'),)
        self.assertEqual(chatbot.get_command('!itineraire rue de chaumont 41 1325 Longueville '
                                             '/ 145 Brooklyn Ave, Brooklyn, NY 11213, États-Unis / route'),)
        self.assertEqual(chatbot.get_command('!itineraire rue de chaumont 41 1325 Longueville '
                                             '/ 145 Brooklyn Ave, Brooklyn, NY 11213, États-Unis'),)
        self.assertEqual(chatbot.get_command('!itineraire 125489632145 / Palais12'),)
        self.assertEqual(chatbot.get_command('!itineraire 125489632145 / Palais12 / route'),)
        """


    """A Completer"""


if __name__ == '__main__':

    chatbot = Chatbot()
    unittest.main()
