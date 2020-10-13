from modules.first.word_finder import Word
from modules.second.sentence_build import SentenceBuild


def main():
    if __name__ == '__main__':
        word_instance = Word()
        #first module
        print(word_instance.get_word(100))
        #second module
        sentence_instance = SentenceBuild()
        print(sentence_instance.get_sentence(400)+"\n")

main()