import nltk
import deprecation

__version__ = '1.0.1'


@deprecation.deprecated(deprecated_in=__version__, current_version=__version__,
                        details='Use Tokeniser class instead of Scraper.')
class Scraper:
    """ A class to access some scraping functionality"""

    def __init__(self):
        """
        Constructor for Scraper

        corpus list is a list type

        file numbers is the number of file for each asset file type.
        We have two of them one for pure number other is in form Kopyas_ then number
        """
        self.corpus_list = []

    def scrape(self, path_format_set=('assets/{}.txt', 'assets/Kopyas_ {}.txt'),
               is_single_file=False, file_numbers=(750, 400)):
        """
        Using nltk library it converts batch of characters into word packs.
        Method uses a closure to detect redundant data

        :param path_format_set: A set which holds the available file paths for scraping
        :param is_single_file: Indicates if input file is only one. It should be also purified
        :param file_numbers: A set to hold the number of files in each index
        :return None: Since it stores all text clusters in corpus_list
        """

        if is_single_file:
            with open(path_format_set, 'r') as content_file:
                self.corpus_list = nltk.word_tokenize(content_file.read())
                return

        def purify(data):
            return data.isalpha()

        def to_lowercase(data):
            return data.lower()

        for i in range(len(path_format_set)):
            for j in range(file_numbers[i]):
                with open(path_format_set[i].format(j + 1), 'r') as content_file:
                    content = content_file.read()
                    self.corpus_list += list(map(to_lowercase, filter(purify, nltk.word_tokenize(content))))
