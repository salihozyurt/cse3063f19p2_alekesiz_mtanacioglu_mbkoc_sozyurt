import numpy as np
import re
from nltk.tokenize import sent_tokenize
import matplotlib.pyplot as plt


filepath = '../../assets/input.txt'

book = open(filepath,'r', encoding="UTF-8")
book_string = book.read().lower()

def sentence_to_wordlist(raw):
    clean = re.sub("[^a-zA-Z]"," ",raw)
    words = clean.split()
    return words

list_of_words = list(set(sentence_to_wordlist(book_string)))

length = (len(list_of_words))

list_of_sentences = sent_tokenize(book_string)
cooc = np.zeros((length, length),np.float64)

print(list_of_sentences[20:22])

def process_sentence(sentence):
    words_in_sentence = sentence_to_wordlist(sentence)
    list_of_indeces = [list_of_words.index(word) for word in words_in_sentence]
    for index1 in list_of_indeces:
        for index2 in list_of_indeces:
            if index1 != index2:
                cooc[index1,index2] +=1

for sentence in list_of_sentences:
    process_sentence(sentence)

from numpy.linalg import norm
def cos_dis(u,v):
    dist = 1.0 - np.dot(u, v) / (norm(u) * norm(v))
    return dist

sorted_list = sorted(list_of_words, key = lambda word: cos_dis(cooc[15,:],cooc[list_of_words.index(word),:]))
print(cooc[15,:])
print(sorted_list[:5])

from numpy.linalg import svd
U,S,V = svd(cooc)

#plt.figure(figsize = (10,5))
#plt.plot(S[:40])
#plt.show()

emb = U[:,:40]
emb[15, :]

cos_dis(emb[15,:], emb[list_of_words.index('stage'),:])

print(sorted(list_of_words, key = lambda word: cos_dis(emb[15,:],emb[list_of_words.index(word),:])))



