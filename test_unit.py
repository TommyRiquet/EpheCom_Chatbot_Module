from chatbot import Chatbot
from Libs.meteo import Meteo
from Libs.command import Commande
import unittest


class ChatBotTest(unittest.TestCase):
    """
       Class de test pour la class Chatbot en utilisant la framework unittest

       Author: T. Riquet
       Date: November 2021
    """
    maxDiff = None

    def test_chatbot_help(self):
        """
            Cette méthode teste la commande !help du chatbot

            Author: T. Riquet
            Date: December 2021
        """
        chatbot_help = Chatbot()
        command_help = Commande()

        #TEST INSTANCE
        self.assertIsInstance(chatbot_help,Chatbot,'Test si chatbot_help est une instance de Chatbot()')
        self.assertIsInstance(command_help,Commande,'Test si command_help est une instance de Commande()')

        self.assertEqual(chatbot_help.get_command('!help'), command_help.get_help('help'))

    def test_chatbot_meteo(self):
        """
            Cette méthode teste la commande !meteo du chatbot

            Author: T. Riquet
            Date: December 2021
        """
        chatbot_meteo = Chatbot()

        #TEST INSTANCE
        self.assertIsInstance(chatbot_meteo, Chatbot, 'Test si chatbot_meteo est une instance de Chatbot()')

        # Test sans API
        self.assertEqual(chatbot_meteo.get_command('!meteo'), '\nmeteo (Nom de la Ville)\n')
        self.assertEqual(chatbot_meteo.get_command('!meteo'), Meteo().get_meteo(""))
        self.assertEqual(chatbot_meteo.get_command('!meteo'), Meteo().get_meteo("meteo"))

        # Test Avec API
        """
        self.assertNotEqual(chatbot_meteo.get_command('!meteo Paris'), 'Ville Introuvable')
        self.assertEqual(chatbot_meteo.get_command('!meteo VilleQuiNexistePas'), 'Ville Introuvable')
        """

    def test_chatbot_add(self):
        """
            Cette méthode teste la commande !add du chatbot

            Author: T. Riquet
            Date: December 2021
        """
        chatbot_add = Chatbot()
        command_add = Commande()

        #TEST INSTANCE
        self.assertIsInstance(chatbot_add, Chatbot, 'Test si chatbot_add est une instance de Chatbot()')
        self.assertIsInstance(command_add, Commande, 'Test si command_add est une instance de Commande()')

        self.assertEqual(chatbot_add.get_command('!add'), 'add (Nom de la commande) (attribut de la commande/Site web à '
                                                      'ouvrir)')
        self.assertEqual(chatbot_add.get_command('!add'), command_add.add_command("add"))

        self.assertEqual(chatbot_add.get_command('!add SansAttribut'), 'Veuillez entrer un attribut')
        self.assertEqual(chatbot_add.get_command('!add SansAttribut'), command_add.add_command("add SansAttribut"))

        self.assertEqual(chatbot_add.get_command('!add test test.com'), 'Commande "test" ajoutée avec succès')
        self.assertEqual(chatbot_add.get_command('!add test test.com'), command_add.add_command('add test test.com'))
        self.assertNotEqual(chatbot_add.get_command('!add test test.com'), command_add.add_command('add t test.com'))

        self.assertEqual(chatbot_add.get_command('!add bonjour salut'), 'Commande "bonjour" ajoutée avec succès')
        self.assertEqual(chatbot_add.get_command('!add bonjour salut'), command_add.add_command('add bonjour salut'))
        self.assertNotEqual(chatbot_add.get_command('!add bonjour salut'), command_add.add_command('add bon salut'))


    def test_chatbot_rem(self):
        """
            Cette méthode teste la commande !rem du chatbot

            Author: T. Riquet
            Date: December 2021
        """
        chatbot_rem = Chatbot()
        command_rem = Commande()

        #TEST INSTANCE
        self.assertIsInstance(chatbot_rem, Chatbot, 'Test si chatbot_rem est une instance de Chatbot()')
        self.assertIsInstance(command_rem, Commande, 'Test si command_rem est une instance de Commande()')

        self.assertEqual(chatbot_rem.get_command('!rem'), 'rem (Nom de la commande)')
        self.assertEqual(chatbot_rem.get_command('!rem'), command_rem.rem_command(''))
        self.assertEqual(chatbot_rem.get_command('!rem'), command_rem.rem_command('rem'))

        self.assertEqual(chatbot_rem.get_command('!rem ephec'), 'Commande "ephec" supprimé avec succès')
        self.assertEqual(chatbot_rem.get_command('!rem tlca'), 'Commande "tlca" supprimé avec succès')


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



if __name__ == '__main__':

    unittest.main()
