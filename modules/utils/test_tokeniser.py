from unittest import TestCase


class TestTokeniser(TestCase):
    """A test class for Tokeniser"""

    def test_tokenise(self):
        """
        Test method for tokenise method
        Uses a file for testing named as test_file.txt
        :return: None
        """
        # Local import for testing
        from modules.utils.tokeniser import Tokeniser
        test_instance = Tokeniser('test_file.txt')
        test_instance.tokenise()
        # Using sort since pack is shuffled by the method
        self.assertEqual(test_instance.pack.sort(), ['A', 'test', 'file.'].sort()
                         , 'Tokeniser class is working fine.')
