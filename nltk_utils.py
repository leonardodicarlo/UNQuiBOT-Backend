import nltk
import numpy as np
nltk.download('punkt')
from nltk.stem.snowball import SpanishStemmer
stemmer = SpanishStemmer()

def tokenize(sentence):
    # divide una sentencia en un array de palabras/tokens
    return nltk.word_tokenize(sentence)

def stem(word):
    # busca la "palabra raíz" de una palabra
    return stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence, all_words):
    # aplica stem a cada palabra
    sentence_words = [stem(word) for word in tokenized_sentence]
    # initialize bag with 0 for each word
    bag = np.zeros(len(all_words), dtype=np.float32)
    for idx, w in enumerate(all_words):
        if w in sentence_words: 
            bag[idx] = 1
    return bag
