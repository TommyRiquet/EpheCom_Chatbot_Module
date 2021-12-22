from chatbot import Chatbot
from src.meteo import Meteo
from src.command import Commande
from src.news import News
from src.itineraire import Itineraire
from src.itineraire import Addresse
import unittest
from urllib.parse import urlparse


class Test_ChatBot_help(unittest.TestCase):
    """
       Classe de test pour la méthode get_help de la classe Commande utilisé par la classe Chatbot

       Author: T. Riquet
       Date: November 2021
    """

    def setUp(self):
        self.chatbot = Chatbot()

    def test_chatbot_instance(self):
        self.assertIsInstance(self.chatbot, Chatbot, 'Test si chatbot est une instance de Chatbot()')

    def test_chatbot_no_message(self):
        # Test si le module commande renvoie la liste des commandes lorsqu'il ne recoit pas de message
        self.assertEqual(self.chatbot.get_command('!help'), Commande().get_help(''))

    def test_chatbot_message(self):

        # Test si le module commande renvoie la liste des commandes lorsqu'il recoit un message quelconque
        self.assertEqual(self.chatbot.get_command('!help'), Commande().get_help('help'))
        self.assertEqual(self.chatbot.get_command('!help'), Commande().get_help('test'))
        self.assertEqual(self.chatbot.get_command('!help'), Commande().get_help('123'))
        self.assertEqual(self.chatbot.get_command('!help'), Commande().get_help(0))
        self.assertEqual(self.chatbot.get_command('!help'), Commande().get_help(None))


class Test_ChatBot_add(unittest.TestCase):
    """
       Classe de test pour la méthode add_command de la classe Commande utilisé par la classe Chatbot

        Author: T. Riquet
        Date: December 2021
    """

    def setUp(self):
        self.chatbot = Chatbot()

    def test_chatbot_add_no_command(self):
        # Test si le chatbot n'envoie pas d'arguments à la méthode add_command du Chatbot
        self.assertEqual(self.chatbot.get_command('!add'), 'add (Nom de la commande) (attribut de la commande/Site '
                                                           'web à ouvrir)')

        # Test si la méthode ne recois pas d'arguments du Chatbot
        self.assertEqual(self.chatbot.get_command('!add'), Commande().add_command(""))

    def test_chatbot_add_no_attribut(self):
        # Test si l'on envoie une commande sans attribut
        self.assertEqual(self.chatbot.get_command('!add SansAttribut'), 'Veuillez entrer un attribut')
        self.assertEqual(self.chatbot.get_command('!add SansAttribut'), Commande().add_command("add SansAttribut"))

    def test_chatbot_add(self):
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


class Test_ChatBot_rem(unittest.TestCase):
    """
         Classe de test pour la méthode rem_command de la classe Commande utilisé par la classe Chatbot

        Author: T. Riquet
        Date: December 2021
    """

    def setUp(self):
        self.chatbot = Chatbot()

    def test_chatbot_rem_no_argument(self):
        # Test si le chatbot envoie la commande rem sans argument
        self.assertEqual(self.chatbot.get_command('!rem'), 'rem (Nom de la commande)')

        # Test si la méthode rem_command ne recoit pas d'argument
        self.assertEqual(self.chatbot.get_command('!rem'), Commande().rem_command(''))

    def test_chatbot_rem(self):

        # Test si l'on supprime une commande
        self.assertEqual(self.chatbot.get_command('!rem ephec'), 'Commande "ephec" supprimé avec succès')
        self.assertEqual(self.chatbot.get_command('!rem tlca'), 'Commande "tlca" supprimé avec succès')

        # Test si l'on supprime une commande personnalisé
        self.chatbot.get_command('!add test testAttribut')
        self.assertEqual(self.chatbot.get_command('!rem test'), 'Commande "test" supprimé avec succès')

        # Test si l'on supprime une commande qui n'existe pas
        self.assertEqual(self.chatbot.get_command('!rem commandeQuiNexistePas'), 'Commande "commandeQuiNexistePas" '
                                                                                 'Introuvable')


class Test_ChatBot_meteo(unittest.TestCase):
    """
        Classe de test pour la méthode get_meteo de la classe Météo utilisé par la classe Chatbot

        Author: T. Riquet
        Date: December 2021
    """

    def setUp(self):
        self.chatbot = Chatbot()

    def test_chatbot_meteo_no_argument(self):

        # Test si le chatbot n'envoie pas d'argument au module Meteo
        self.assertEqual(self.chatbot.get_command('!meteo'), '\nmeteo (Nom de la Ville)\n')

        # Test si le module Meteo ne recoit pas d'argument
        self.assertEqual(self.chatbot.get_command('!meteo'), Meteo().get_meteo(""))

    def test_chatbot_meteo_API(self):

        # Test si le module trouve les villes passées en argument
        self.assertNotEqual(self.chatbot.get_command('!meteo Paris'), 'Je ne connais pas cette ville :/')
        self.assertNotEqual(self.chatbot.get_command('!meteo Bruxelles'), 'Je ne connais pas cette ville :/')
        self.assertNotEqual(self.chatbot.get_command('!meteo Perwez'), 'Je ne connais pas cette ville :/')

        # Test si le module recoit un code postal
        self.assertNotEqual(self.chatbot.get_command('!meteo 1360'), 'Je ne connais pas cette ville :/')
        self.assertNotEqual(self.chatbot.get_command('!meteo 1000'), 'Je ne connais pas cette ville :/')


    def test_chatbot_meteo_API(self):


        # Test si le module recoit une ville qui n'existe pas
        self.assertEqual(self.chatbot.get_command('!meteo VilleQuiNexistePas'), 'Je ne connais pas cette ville :/')
        self.assertEqual(self.chatbot.get_command('!meteo JeTestCeModule'), 'Je ne connais pas cette ville :/')
        self.assertEqual(self.chatbot.get_command('!meteo Paru'), 'Je ne connais pas cette ville :/')




class Test_ChatBot_itineraire(unittest.TestCase):

    def setUp(self):
        self.chatbot = Chatbot()

    def test_chatbot_itineraire(self):
        """
        Cette méthode teste la commande !itineraire du chatbot

        Author: Q. Laruelle
        Date: december 2021
        """
        """
                clefs utilisation normale: 9744eec549f1c82b18af8a10f26d1489 ou 143323c5ab5dfe15ec89b2bbb320bea7
                clefs API de test: 3bbc0c5c02b03a7e43723288f3de55fe ou bb19b66d645ba9c738d69f239b2808ec
        """

        # Test de l'appel d'itineraire sans lui passer d'addresses
        self.assertEqual(self.chatbot.get_command('!itineraire'),
                         '\nitineraire (Adresse 1) / (Adresse 2) /route\n\n')

        # Test de l'appel d'itineraire sans lui mettre de point d'exclamation ni d'adresse
        self.assertEqual(self.chatbot.get_command('itineraire'), None)

        # Test de l'appel d'itineraire sans lui mettre de point d'exclamation
        self.assertEqual(self.chatbot.get_command('itineraire rue de chaumont 41 1325 Longueville / '
                                                  'rue notre dame 65 Perwez'), None)

        # Test de l'appel d'itineraire sans lui mettre de point d'exclamation et avec des virgules en place des slashs
        self.assertEqual(self.chatbot.get_command('itineraire rue de chaumont 41 1325 Longueville , '
                                                  'rue notre dame 65 Perwez ,route'), None)

        # Test de l'appel d'itineraire en utilisant des virgules plutôt que des slashs
        self.assertEqual(
            self.chatbot.get_command('!itineraire rue de chaumont 41 1325 Longueville, rue notre dame 65 Perwez'),
            '\nitineraire (Adresse 1) / (Adresse 2) /route\n\n')

    def test_chatbot_itineraire_get_argument(self):
        """
        Cette méthode teste la méthode get_argument de la classe Itineraire

        Author: Q. Laruelle
        Date: december 2021
        """

        # Test si get_argument ne recoit pas d'argument
        self.assertEqual(Itineraire().get_argument('itineraire '), '\nitineraire (Adresse 1) / (Adresse 2) /route\n\n')

        # Test si la méthode renvoie bien la doc
        self.assertEqual(Itineraire().get_argument('itineraire '), Itineraire().__doc__)

        # Test quand la méthode ne reçoit pas d'argument "/route"
        self.assertEqual(Itineraire().get_argument('itineraire Palais12 / rue de notre dame 65 Perwez'),
                         ['Palais12 ', ' rue de notre dame 65 Perwez', ' '])

        # Test quand la méthode reçoit un argument /route
        self.assertEqual(Itineraire().get_argument('itineraire Palais12 / rue de notre dame 65 Perwez /route'),
                         ['Palais12 ', ' rue de notre dame 65 Perwez ', 'route'])

        # Test quand la méthode reçoit un tuple en place d'une string
        self.assertRaises(TypeError, Addresse().get_addresse, 32)

    def test_chatbot_Addresse_get_addresse(self):
        """
        Cette méthode teste la méthode get_addresse de la classe Addresse

        Author: Q.laruelle
        date: december 2021
        !!!CE TEST UTILISE UNE API
        """
        """
        # Test quand la méthode reçoit une adresse normale
        self.assertEqual(Addresse().get_addresse('rue de chaumont 41 Longueville'), [50.6966469, 4.7367989])
        
        # Test quand la méthode reçoit un point d'interêt plutôt qu'une addresse
        self.assertEqual(Addresse().get_addresse('Palais12'), [50.9012565, 4.3418378])
        
        # Test quand la méthode reçoit une string sans adresse
        self.assertEqual(Addresse().get_addresse('fkdjsfkdjskfjdksjfds'), 0)
        
        # Test quand la méthode ne reçoit rien 
        self.assertEqual(Addresse().get_addresse(''), 0)
        
        # Test quand la méthode recçoit un tuple en place d'une string 
        self.assertRaises(TypeError, Addresse().get_addresse, 56)
        """


class Test_ChatBot_news(unittest.TestCase):

    def setUp(self):
        self.chatbot = Chatbot()

    def test_chatbot_news(self):
        """
        Cette methode test le module !news du chatbot

        Author: S. Dziemianko
        Date: December 2021
        """
        self.assertEqual(self.chatbot.get_command('!news'), '\nnews (Sujet) (Nombre de Sujet(min 1, max 10))\n')
        self.assertEqual(self.chatbot.get_command('!news'), News().get_news(""))

        """
        self.assertEqual(self.chatbot.get_command('!news IT 1'), self.chatbot.get_command('!news IT 1'))
        self.assertEqual(self.chatbot.get_command('!news IT 3'), self.chatbot.get_command('!news IT 3'))
        self.assertEqual(self.chatbot.get_command('!news IT 10'), self.chatbot.get_command('!news IT 10'))
        self.assertEqual(self.chatbot.get_command('!news IT 15'), self.chatbot.get_command('!news IT 10'))
        self.assertEqual(self.chatbot.get_command('!news IT -1'), self.chatbot.get_command('!news IT 1'))
        self.assertEqual(self.chatbot.get_command('!news IT 0'), self.chatbot.get_command('!news IT 1'))
        """


    def test_domain_parse(self):
        """
        cette methode test que les liens sont bien parsé pour la gestion des doublons

        Author: S. Dziemianko
        Date: December 2021
        """

        self.assertEqual(urlparse('https://fr.wikipedia.org/wiki/Informatique').netloc, 'fr.wikipedia.org')
        self.assertEqual(urlparse('https://www.youtube.com/watch?v=7no56Zw1e20').netloc, 'www.youtube.com')
        self.assertEqual(urlparse('https://realpython.com/python-mock-library/').netloc, 'realpython.com')
        self.assertEqual(urlparse('https://docs.python.org/3/library/unittest.mock.html').netloc, 'docs.python.org')
        self.assertEqual(urlparse('https://cmcdocs.gwabbit.com:8443/cmc/').netloc, 'cmcdocs.gwabbit.com:8443')
        self.assertEqual(urlparse('https://square.github.io/okhttp/4.x/okhttp/okhttp3/-http-url/').netloc,
                         'square.github.io')

    def test_domain_in_site(self):
        """
        Cette methode vérifie que l'array site compose des domaines deja utilisé est parcouru pour vérifier les doublons

        Author: S. Dziemianko
        Date: Decembre 2021
        """
        self.site = ['fr.wikipedia.org', 'www.youtube.com', 'realpython.com', 'docs.python.org',
                     'cmcdocs.gwabbit.com:8443', 'square.github.io']

        self.assertIn(urlparse('https://fr.wikipedia.org/wiki/Informatique').netloc, self.site)
        self.assertIn(urlparse('https://www.youtube.com/watch?v=y0lg_-8vr5w&list=RDGMEM6ijAnFTG9').netloc, self.site)
        self.assertIn(urlparse('https://docs.python.org/3/library/unittest.mock.html').netloc, self.site)
        self.assertNotIn(urlparse('https://twitter.com/home').netloc, self.site)
        self.assertNotIn(urlparse('https://www.facebook.com/').netloc, self.site)
        self.assertNotIn(urlparse('https://portail.ephec.be/').netloc, self.site)


if __name__ == '__main__':
    unittest.main()
