import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from utils import dire_bonjour  # Assure-toi que l'importation est correcte

class TestUtils(unittest.TestCase):
    def test_dire_bonjour(self):
        """Teste que la fonction dire_bonjour retourne le bon message."""
        self.assertEqual(dire_bonjour("Alice"), "Bonjour, Alice !")
        self.assertEqual(dire_bonjour("Bob"), "Bonjour, Bob !")

if __name__ == "__main__":
    unittest.main()
