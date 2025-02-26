import unittest
from utils import dire_bonjour

class TestUtils(unittest.TestCase):
    def test_dire_bonjour_fr(self):
        """Teste la salutation en français."""
        self.assertEqual(dire_bonjour("Alice", "fr"), "Bonjour, Alice !")

    def test_dire_bonjour_en(self):
        """Teste la salutation en anglais."""
        self.assertEqual(dire_bonjour("Bob", "en"), "Hello, Bob !")

    def test_dire_bonjour_es(self):
        """Teste la salutation en espagnol."""
        self.assertEqual(dire_bonjour("Carlos", "es"), "Hola, Carlos !")

    def test_dire_bonjour_langue_invalide(self):
        """Teste le cas où la langue est inconnue."""
        self.assertEqual(dire_bonjour("David", "de"), "Langue non supportée : de")

if __name__ == "__main__":
    unittest.main()
