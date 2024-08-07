from nltk.tokenize import word_tokenize
from gensim import downloader
from gensim.models import KeyedVectors
from nltk.data import find
import nltk
import numpy as np
import spacy
import os

pos_weights = {
    "ADJ": 1.5,
    "ADP": 0.8,
    "ADV": 1.2,
    "AUX": 0.5,
    "CONJ": 0.9,
    "CCONJ": 0.9,
    "DET": 1.0,
    "INTJ": 1.1,
    "NOUN": 1.7,
    "NUM": 1.3,
    "PART": 0.7,
    "PRON": 1.0,
    "PROPN": 1.6,
    "PUNCT": 0.2,
    "SCONJ": 0.8,
    "SYM": 0.9,
    "VERB": 1.4,
    "X": 0.1
}


def ensure_nltk_data():
    try:
        find('tokenizers/punkt')
    except LookupError:
        nltk.download('punkt')


ensure_nltk_data()


nlp = spacy.load("en_core_web_sm")

WOED2VEC_FILE_PATH = os.path.join(os.path.dirname(__file__),
                                  'GoogleNews-vectors-negative300.bin.gz')


def load_word2vec() -> KeyedVectors:
    """
        Tries to load the pre-trained Word2Vec embeddings from
        the binary file 'GoogleNews-vectors-negative300.bin.gz'
        located at the path 'DATASET_PATH'.
        If loading fails the function falls back to downalding
        and loading the  'word2vec-google-news-300' model using
        the 'gensim.downloader.load()' function.

        Return :
            word2vec: A variable which contains the loaded
            Word2Vec embeddings as a 'KeyedVectors' instance
    """

    word2vec = None

    try:
        word2vec = KeyedVectors.load_word2vec_format(WOED2VEC_FILE_PATH,
                                                     binary=True)
        print("Loaded Word2Vec model from local file.")

    except (FileNotFoundError, ValueError) as e:
        print(f"Failed to load Word2Vec model from local file: {e}")
        print("Falling back to downloading the model...")
        word2vec = downloader.load('word2vec-google-news-300')
        print("Successfully downloaded and loaded Word2Vec model.")

    return word2vec


word2vec_google_news = load_word2vec()


def generate_embedding(sentence: str) -> np.array:
    vectors = []
    sentence_tokens = word_tokenize(sentence)
    for token in sentence_tokens:
        try:
            token = token.lower()
            vector = word2vec_google_news[token]
            vectors.append(vector)
        except Exception:
            vectors.append(np.zeros(300))

    vectors = np.mean(vectors, axis=0)
    return vectors
