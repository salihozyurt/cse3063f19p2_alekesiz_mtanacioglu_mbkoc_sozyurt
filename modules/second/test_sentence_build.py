from unittest import TestCase


class TestSentence(TestCase):
    """Test class for Sentence"""

    def test_getSentence(self):
        """Test method for get_sentence method"""
        from modules.second.sentence_build import SentenceBuild
        sentence_obj=SentenceBuild()
        self.assertTrue(type(sentence_obj.get_sentence(300)) is str)