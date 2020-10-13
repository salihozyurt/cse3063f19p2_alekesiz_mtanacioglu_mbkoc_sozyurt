from modules.utils.tokeniser import Tokeniser


class Word:
    word_set=None
    """
    A class for basic word operations

    Contains one predefined variable for Turkish character set using a dictionary
    """

    DEFAULT_SET = frozenset(
        {'’̇': 0," ":0, 'a': 1, 'b': 2, 'c': 3, 'ç': 4, 'd': 5, 'e': 6, 'f': 7, 'g': 8, 'ğ': 9, 'h': 10, 'ı': 11, 'i': 12,
         'j': 13, 'k': 14, 'l': 15, 'm': 16, 'n': 17, 'o': 18, 'ö': 19, 'p': 20, 'r': 21, 's': 22, 'ş': 23,
         't': 24, 'u': 25, 'ü': 26, 'v': 27, 'y': 28, 'z': 29, 'q': 30, 'w': 31, 'x': 32, 'â': 33, 'û': 34}.items())

    def __init__(self, word_set=DEFAULT_SET):
        """
        Word class Constructor

        :param word_set: A given word set as a parameter to be used in word methods
        """
        self.word_set = dict(word_set)  # A class attribute which holds the given set
        self.word_set.setdefault("",0)
    def get_word(self, value, corpus_file="../../assets/corpus_file.txt"):
        """
        Gets a random word from the given value
        :param corpus_file: A file which contains information to be tokenised
        :param value: an integer which shows the value of the word wanted to be returned
        :return: The word with the given value
        """
        tokeniser = Tokeniser(filename=corpus_file)  # A variable which is an object for Tokeniser class
        tokeniser.tokenise()  # Calls the tokenise method and builds the pack
        for word in tokeniser.pack:  # Loops through each word in pack
            if self.get_word_value(word) == value:
                # Using the get_word_value() method detects if the current word's value
                # is equal to the given value
                return word  # Returns the word in this case

    def get_word_value(self, word):
        """
        A method to find a given word's value

        How can we decide the value of a word? The answer is quite simple.
        We use the word_set to decide the value of the each character.
        Then we add them up to find the total value.

        :type: word: string
        :param word: A word to find its value
        :type: value: int
        :return: value: A value that indicates the numeric value of the current word
        """
        value = 0  # Value is initially zero
        for char in word:  # For loop through word for each character
            if self.word_set.get(char) is None:
                self.word_set.setdefault(char, 0)
            value += self.word_set.get(char)  # We add the current char value using the word_set
        return value  # We return the result value