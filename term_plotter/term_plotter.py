import numpy as np
import sklearn
import pandas as pd
import seaborn as sns
import os, json
from sklearn.feature_extraction.text import TfidfVectorizer
import argparse
import matplotlib.pyplot as plt

def score_terms(directory):
    speech_dir = directory
    files = os.listdir(speech_dir)
    corpus = []
    dates = []
    for file in files:
        with open(speech_dir+file, "r") as infile:
            speech = json.load(infile)
            dates.append(pd.to_datetime(speech["Date"]))
            corpus.append(speech["Speech"])
    return corpus, dates

def vectorize(corpus,dates,terms, title, output):
    vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1,3))
    vectors = vectorizer.fit_transform(corpus)
    vectors_array = vectorizer.fit_transform(corpus).toarray()
    feature_names = vectorizer.get_feature_names()
    total_scores = []
    total_dates = []
    total_terms = []
    for term in terms:

        try:
            ind_e = feature_names.index(term)
            term_scores = []
            for doc in vectors_array:
                term_scores.append(doc[ind_e])
            term = [term]* len(term_scores)
            total_scores.extend(term_scores)
            total_dates.extend(dates)
            total_terms.extend(term)
        except ValueError:
            if len(term.split()) > 3:
                print (f"The term \"{term}\" cannot be found in the data because it contains more than 3 tokens", "\n")
            else:
                print (f"The term \"{term}\" cannot be found in the data","\n")

    df2 = pd.DataFrame({'Date': total_dates,
                       'Score': total_scores,
                       'Term': total_terms})

    if len (total_terms) >= 1:
        g = sns.relplot(x="Date", y="Score", kind="line", data=df2, hue="Term")
        plt.title(title)
        if output == None:
            filename = (' '.join(terms)).replace(' ','_')
        else:
            filename = output[0]
        filename = filename + '.png'
        plt.savefig(filename, dpi=300, bbox_inches="tight")
    else:
        print ("None of the terms are present in the data", "\n")
        print ("Plot can therefore not be created", "\n")


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--terms', type=str, nargs='+',
                        help='a list of up to five terms, in quotations,  \
                        separated by white space. Each “term” can consist of  \
                        three tokens' )
    parser.add_argument('--title', type=str, default= '', help= 'an optional string argument \
                        that adds a title to the plot. If not provided, the \
                        program outputs the plot without a title.')
    parser.add_argument('--path', nargs=1,
                        default= [os.getcwd() + "/us_presidential_speeches/"],
                        help= 'an optional string argument that specifies \
                        where the speech directory is. If not provided, \
                        the program should assume to look at the folder in the \
                        current directory, e.g.: ./us_presidential_speeches.')
    parser.add_argument('--output',nargs=1, type=str, default=None, help= 'An \
                        optional string argument that saves the plot under \
                        the specified name. If not provided, saves the plot as \
                        the concatenation of all terms, separated by an \
                        underscore token. e.g.: america_united_states.png.')
    args = parser.parse_args()
    if len(args.terms) > 5:
        pass
    else:
        terms_new = args.terms
    try:
        scores = score_terms(directory=args.path[0])
        vectorize(corpus=scores[0],dates=scores[1], terms=terms_new, title=args.title, output=args.output)
    except FileNotFoundError:
        print ("Path not in directory", "\n")
    except NameError:
        print ("You can only use up to five terms", "\n")
