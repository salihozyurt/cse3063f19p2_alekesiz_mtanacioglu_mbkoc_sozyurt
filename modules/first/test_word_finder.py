from unittest import TestCase


class TestWord(TestCase):
    """Test class for Word"""

    def test_get_word(self):
        """Test method for get_word method"""
        from modules.first.word_finder import Word  # Local import of Word class
        test_corpus_filename = 'corpus_test.txt'
        word_object = Word({'b': 1, 'e': 2, 'l': 3, 'o': 4, 'w': 5, 'm': -5})  # Init a word object
        self.assertEqual(word_object.get_word(15, test_corpus_filename), 'elbow')
        self.assertEqual(word_object.get_word(0, test_corpus_filename), 'elm')

    def test_get_word_value(self):
        """Test method for get_word_value method"""
        from modules.first.word_finder import Word  # Local import of Word class
        word_object = Word({'b': 1, 'e': 2, 'l': 3, 'o': 4, 'w': 5, 'm': -5})  # Init a word object
        self.assertEqual(word_object.get_word_value('bee'), 5)
        self.assertEqual(word_object.get_word_value('low'), 12)
        self.assertEqual(word_object.get_word_value('meme'), -6)
