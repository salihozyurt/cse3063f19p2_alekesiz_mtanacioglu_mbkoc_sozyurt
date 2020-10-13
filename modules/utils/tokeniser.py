import random

class Tokeniser:
    """
    A class to tokenise a file and store the tokens
    Since nltk has some problems with Turkish characters
    I created a primitive one for my use
    """

    def __init__(self, filename):
        """
        Constructor for Tokeniser

        pack list is initialised to be used to store tokens

        :param filename: A filename for the file to be tokenised
        """
        self.pack = []
        self.filename = filename

    def tokenise(self):
        """
        Core method for class. It traverse through all words of the given file
        and adds each of them to pack

        :return: None
        """
        with open(self.filename,encoding="UTF-8") as f:
            for line in f:
                for word in line.split():
                    if chr(775) in word:
                        word = word.replace(chr(775), '')
                    self.pack.append(word)
        random.shuffle(self.pack)
