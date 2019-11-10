import pickle
from nltk.tokenize import word_tokenize

def load_model(file_path): 
    classifier_f = open(file_path, "rb")
    classifier = pickle.load(classifier_f)
    classifier_f.close()
    return classifier

word_features = load_model('word_features.pickle')

def find_features(document):
    words = word_tokenize(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)
    return features

ensemble_clf = load_model('pickled_algos/ensemble_clf.pickle')

def score(text):
    feats = find_features(text)
    return ensemble_clf.classify(feats), ensemble_clf.confidence(feats)