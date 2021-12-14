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
            Cette méthode test la commande !meteo du chatbot

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
            Cette méthode test la commande !add du chatbot

            Author: T. Riquet
            Date: December 2021
        """
        self.assertEqual(chatbot.get_command('!add'), 'add (Nom de la commande) (attribut de la commande/Site web à '
                                                      'ouvrir)')
        self.assertEqual(chatbot.get_command('!add test test.com'), 'Commande "test" ajoutée avec succès')
        self.assertEqual(chatbot.get_command('!add bonjour salut'), 'Commande "bonjour" ajoutée avec succès')

    def test_chatbot_rem(self):
        """
            Cette méthode test la commande !rem du chatbot

            Author: T. Riquet
            Date: December 2021
        """
        self.assertEqual(chatbot.get_command('!rem'), 'rem (Nom de la commande)')
        self.assertEqual(chatbot.get_command('!rem ephec'), 'Commande "ephec" supprimé avec succès')
        self.assertEqual(chatbot.get_command('!rem tlca'), 'Commande "tlca" supprimé avec succès')



if __name__ == '__main__':

    chatbot = Chatbot()
    unittest.main()
