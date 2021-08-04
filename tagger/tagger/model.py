import pickle

import numpy as np
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import cross_val_score
from sklearn.svm import LinearSVC
from spacy.lang.en import English
from .pre_process import token_to_features
import spacy
import re
import itertools
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import classification_report
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier

class POSTagger:

    def __init__(self):
        self.vec = DictVectorizer()
    #    self.vec = CountVectorizer()
        self.model = LinearSVC()
    #    self.model = DecisionTreeClassifier()

    def fit_and_report(self, X, Y, cross_val=True, n_folds=5):
        X = self.vec.fit_transform(X)
        if cross_val:
            from sklearn.model_selection import cross_val_score
            scores = cross_val_score(self.model, X, Y, cv=n_folds)
            print(f"{n_folds}-fold cross-validation results over training set:\n")
            print("Fold\tScore".expandtabs(15))
            for i in range(n_folds):
                print(f"{i + 1}\t{scores[i]}".expandtabs(15))
            print(f"Average\t{np.mean(scores)}".expandtabs(15))

        self.model.fit(X, Y)

    def save_model(self, output_file):
        with open(output_file, "wb") as outfile:
            pickle.dump(self, outfile)


    def tag_document(self,filename):
        nlp = spacy.load('en_core_web_sm')
        with open(filename, "r") as file:
            file_txt = file.read()
        # Removing multiple spaces
        fixed_text = re.sub(r'\s+', ' ', file_txt)
        processed_text = nlp(fixed_text)
        sents = [sent for sent in processed_text.sents]
        tagged_doc = []
        for sentence in sents:
            tagged_sent = self.tag_sentence(str(sentence))
            tagged_doc.append(tagged_sent)
        return tagged_doc


    def tag_sentence(self, sentence):
        doc = English().tokenizer(sentence)
        tokenized_sent = [token.text for token in doc]
        featurized_sent = [token_to_features(tokenized_sent, i) \
                           for i in range(len(tokenized_sent))]
        vectorized_sent = self.vec.transform(featurized_sent)
        labels = self.model.predict(vectorized_sent)
        tagged_sent = list(zip(tokenized_sent, labels))
        return tagged_sent


    def evaluate(self, X, Y):
        vectorize = self.vec.transform(X)
        labels = self.model.predict(vectorize)
        return classification_report(Y, labels)
