from unittest import TestCase
from src.translator import PigLatinTranslator

class TestPigLatinTranslator(TestCase):

    def test_get_phrase(self):
        translator = PigLatinTranslator("hello world")
        phrase = translator.get_phrase()
        self.assertEqual("hello world", phrase)

    def test_transalte_empty_phrase(self):
        translator = PigLatinTranslator("")
        translation = translator.translate()
        self.assertEqual("nil", translation)

    def test_transalte_phrase_starts_vowel_ends_y(self):
        translator = PigLatinTranslator("any")
        translation = translator.translate()
        self.assertEqual("anynay", translation)

    def test_transalte_phrase_starts_vowel_e_ends_y(self):
        translator = PigLatinTranslator("enemy")
        translation = translator.translate()
        self.assertEqual("enemynay", translation)

    def test_transalte_phrase_starts_vowel_ends_vowel(self):
        translator = PigLatinTranslator("umbrela")
        translation = translator.translate()
        self.assertEqual("umbrelayay", translation)

    def test_transalte_phrase_starts_vowel_i_ends_vowel_e(self):
        translator = PigLatinTranslator("incruse")
        translation = translator.translate()
        self.assertEqual("incruseyay", translation)

    def test_transalte_phrase_starts_vowel_o_ends_consonant(self):
        translator = PigLatinTranslator("ok")
        translation = translator.translate()
        self.assertEqual("okay", translation)

    def test_transalte_phrase_starts_vowel_a_ends_consonant(self):
        translator = PigLatinTranslator("and")
        translation = translator.translate()
        self.assertEqual("anday", translation)

    def test_transalte_phrase_starts_consonant(self):
        translator = PigLatinTranslator("hello")
        translation = translator.translate()
        self.assertEqual("ellohay", translation)

    def test_transalte_phrase_starts_more_consonants(self):
        translator = PigLatinTranslator("known")
        translation = translator.translate()
        self.assertEqual("ownknay", translation)

    def test_transalte_phrase_starts_more_than_2_consonants_spring(self):
        translator = PigLatinTranslator("spring")
        translation = translator.translate()
        self.assertEqual("ingspray", translation)