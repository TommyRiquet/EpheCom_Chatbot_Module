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
        self.assertEqual(chatbot.get_command('!meteo'), 'Ville manquante ou incorrecte (Ex: !meteo Paris)')

    def test_chatbot_add(self):
        """
            Cette méthode test la commande !add du chatbot

            Author: T. Riquet
            Date: December 2021
        """
        self.assertEqual(chatbot.get_command('!add'), "!add (nom de la commande) (ce qu'elle retourne)")
        self.assertEqual(chatbot.get_command('!add test test.com'), 'Commande "test" ajoutée avec succès')
        self.assertEqual(chatbot.get_command('!add bonjour salut'), 'Commande "bonjour" ajoutée avec succès')

    def test_chatbot_rem(self):
        """
            Cette méthode test la commande !rem du chatbot

            Author: T. Riquet
            Date: December 2021
        """
        self.assertEqual(chatbot.get_command('!rem'), '!rem (Nom de la commande)')
        self.assertEqual(chatbot.get_command('!rem ephec'), 'Site Web supprimé avec succès')
        self.assertEqual(chatbot.get_command('!rem tlca'), 'Site Web supprimé avec succès')

    """A Completer"""


if __name__ == '__main__':

    chatbot = Chatbot()
    unittest.main()
