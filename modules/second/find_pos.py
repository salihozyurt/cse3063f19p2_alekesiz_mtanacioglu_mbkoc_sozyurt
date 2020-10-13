"""
Zemberek: Finding POS Tag Example
Documentation: https://bit.ly/32WCfyi
Java Code Example: https://bit.ly/2Nn7hse
"""
import random
from os.path import join
from typing import List

import jpype

if __name__ == '__main__':

    nouns =[]
    verb =[]

    ZEMBEREK_PATH: str = join('../../..', '..', 'bin', 'C:\\Users\\Co\\PycharmProjects\\cse3063f19p2_alekesiz_mtanacioglu_mbkoc_sozyurt\\zemberek-full.jar')

    jpype.startJVM(
        jpype.getDefaultJVMPath(),
        '-ea',
        f'-Djava.class.path={ZEMBEREK_PATH}',
        convertStrings=False
    )

    TurkishMorphology: jpype.JClass = jpype.JClass('zemberek.morphology.TurkishMorphology')

    morphology: TurkishMorphology = TurkishMorphology.createWithDefaults()
    with open('../../assets/corpus_file.txt', 'r', encoding="utf-8") as f:
        for line in f:
            for word in line.split():
                sentence: str = word
                analysis: jpype.java.util.ArrayList = (
                    morphology.analyzeAndDisambiguate(sentence).bestAnalysis()
                )
                pos: List[str] = []

                for i, analysis in enumerate(analysis, start=1):
                    with open("ClassifiedVerbs\\" + str(analysis.getPos()) + ".txt", "a", encoding="UTF-8") as myfile:
                        myfile.write(word+"\n")


    jpype.shutdownJVM()

    with open('../../ClassifiedVerbs/Noun.txt', 'r', encoding="UTF-8") as f:
     for line in f:
        for word in line.split():
            nouns.append(word)

    with open('../../ClassifiedVerbs/Verb.txt', 'r', encoding="UTF-8") as f:
     for line in f:
        for word in line.split():
            verb.append(word)

    num = random.randrange(0,len(nouns))
    num2 = random.randrange(0,len(verb))
    print (nouns[num] + ' ' + verb[num2] )
