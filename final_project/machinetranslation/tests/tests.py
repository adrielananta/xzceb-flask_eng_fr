"""
Translator unit tests
"""
import unittest
import sys

sys.path.append("../machinetranslation")

from translator import english_to_french, french_to_english

class EnglishToFrenshTest(unittest.TestCase):
    """
    Test cases for English to France translator
    """
    def test_empty(self):
        """
        Empty String input
        """
        self.assertEqual(english_to_french(""), "ApiException")

    def test_null(self):
        """
        Null input
        """
        self.assertEqual(english_to_french(None), "ValueError")

    def test_valid_word(self):
        """
        Valid word String input
        """
        self.assertEqual(english_to_french("Hello"), "Bonjour")

class FrenchToEnglishTest(unittest.TestCase):
    """
    Test cases for French to English translator
    """
    def test_empty(self):
        """
        Empty String input
        """
        self.assertEqual(french_to_english(""), "ApiException")

    def test_null(self):
        """
        Null input
        """
        self.assertEqual(french_to_english(None), "ValueError")

    def test_valid(self):
        """
        Valid word String input
        """
        self.assertEqual(french_to_english("Bonjour"), "Hello")

if __name__ == '__main__':
    unittest.main()
