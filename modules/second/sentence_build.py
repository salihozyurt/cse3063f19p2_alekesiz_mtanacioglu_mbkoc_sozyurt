import random
from modules.first.word_finder import Word


class SentenceBuild:
    """ A class for generate sentence """

    sentence = ""
    word_instance = Word()
    adjectives = []
    adverbs = []
    conjunctions = []
    determiner = []
    duplicators = []
    interjections = []
    nouns = []
    numerals = []
    postpositive = []
    pronouns = []
    questions = []
    verbs = []

    """Open the files which includes the classified words."""

    def __init__(self):
        with open('../../ClassifiedVerbs//Adjective.txt', 'r', encoding="UTF-8") as f:
            for line in f:
                for word in line.split():
                    self.adjectives.append(word)
        with open('../../ClassifiedVerbs/Adverb.txt', 'r', encoding="UTF-8") as f:
            for line in f:
                for word in line.split():
                    self.adverbs.append(word)
        with open('../../ClassifiedVerbs/Conjunction.txt', 'r', encoding="UTF-8") as f:
            for line in f:
                for word in line.split():
                    self.conjunctions.append(word)
        with open('../../ClassifiedVerbs/Determiner.txt', 'r', encoding="UTF-8") as f:
            for line in f:
                for word in line.split():
                    self.determiner.append(word)
        with open('../../ClassifiedVerbs/Duplicator.txt', 'r', encoding="UTF-8") as f:
            for line in f:
                for word in line.split():
                    self.duplicators.append(word)
        with open('../../ClassifiedVerbs/Interjection.txt', 'r', encoding="UTF-8") as f:
            for line in f:
                for word in line.split():
                    self.interjections.append(word)
        with open('../../ClassifiedVerbs/Noun.txt', 'r', encoding="UTF-8") as f:
            for line in f:
                for word in line.split():
                    self.nouns.append(word)
        with open('../../ClassifiedVerbs/Numeral.txt', 'r', encoding="UTF-8") as f:
            for line in f:
                for word in line.split():
                    self.numerals.append(word)
        with open('../../ClassifiedVerbs/PostPositive.txt', 'r', encoding="UTF-8") as f:
            for line in f:
                for word in line.split():
                    self.postpositive.append(word)
        with open('../../ClassifiedVerbs/Pronoun.txt', 'r', encoding="UTF-8") as f:
            for line in f:
                for word in line.split():
                    self.pronouns.append(word)
        with open('../../ClassifiedVerbs/Question.txt', 'r', encoding="UTF-8") as f:
            for line in f:
                for word in line.split():
                    self.questions.append(word)
        with open('../../ClassifiedVerbs/Verb.txt', 'r', encoding="UTF-8") as f:
            for line in f:
                for word in line.split():
                    self.verbs.append(word)

    def get_sentence(self, value):
        """
                Generates a random sentence.
                :param value: an integer which shows the value of the sentence wanted to be returned
                :return: sentence
        """
        adjc = random.randrange(0, len(self.adjectives))
        advrb = random.randrange(0, len(self.adverbs))
        cnjctn = random.randrange(0, len(self.conjunctions))
        dtrmnr = random.randrange(0, len(self.determiner))
        dplctr = random.randrange(0, len(self.duplicators))
        intrjctn = random.randrange(0, len(self.interjections))
        noun = random.randrange(0, len(self.nouns))
        nmrl = random.randrange(0, len(self.numerals))
        ppstv = random.randrange(0, len(self.postpositive))
        prnon = random.randrange(0, len(self.pronouns))
        qustn = random.randrange(0, len(self.questions))
        verb = random.randrange(0, len(self.verbs))

        while True:
            if (value < 200):
                sentence = self.nouns[noun] + " " + self.verbs[verb]
            elif (value > 200 and value < 350):
                sentence = self.nouns[noun] + " " + self.conjunctions[cnjctn] + " " + self.verbs[verb]
            elif (value >= 350 and value < 450):
                sentence = self.adjectives[adjc] + " " + self.nouns[noun] + " " + self.conjunctions[cnjctn] + " " + \
                           self.verbs[verb]
            elif (value >= 450 and value < 600):
                sentence = self.adjectives[adjc] + " " + self.nouns[noun] + " " + self.conjunctions[cnjctn] + " " + \
                           self.adverbs[advrb] + " " + \
                           self.verbs[verb]
            elif (value >= 600 and value < 750):
                sentence = self.adjectives[adjc] + " " + self.nouns[noun] + " " + self.conjunctions[cnjctn] + " " + \
                           self.adverbs[advrb] + " " + \
                           self.verbs[verb] + " " + self.conjunctions[cnjctn % 8 + 1] + " " + self.pronouns[
                               prnon] + " " + self.verbs[
                               verb % 5 + 1]
            else:
                sentence = self.adjectives[adjc] + " " + self.nouns[noun] + " " + self.conjunctions[cnjctn] + " " + \
                           self.adverbs[advrb] + " " + \
                           self.verbs[verb] + " " + self.conjunctions[cnjctn % 8 + 1] + " " + self.pronouns[
                               prnon] + " " + self.interjections[intrjctn] + " " + self.verbs[
                               verb % 5 + 1]
            sentence = sentence + "."

            if (self.word_instance.get_word_value(sentence) == value):
                return (sentence)
            else:
                adjc = random.randrange(0, len(self.adjectives))
                advrb = random.randrange(0, len(self.adverbs))
                cnjctn = random.randrange(0, len(self.conjunctions))
                dtrmnr = random.randrange(0, len(self.determiner))
                dplctr = random.randrange(0, len(self.duplicators))
                intrjctn = random.randrange(0, len(self.interjections))
                noun = random.randrange(0, len(self.nouns))
                nmrl = random.randrange(0, len(self.numerals))
                ppstv = random.randrange(0, len(self.postpositive))
                prnon = random.randrange(0, len(self.pronouns))
                qustn = random.randrange(0, len(self.questions))
                verb = random.randrange(0, len(self.verbs))
