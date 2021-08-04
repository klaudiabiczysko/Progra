## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Details](#details)

## General info
This is a Part Of Speech-tagger model for English text.
The package contains an init-program, pre-processing program, a model program
and a run program. The package also includes a configuration file.
All programs are written in Python3.

The project was written as a part of assignment 3 in Advanced programming for
language technologists. Klaudia and Emma completed the code that was given
for the assignment.

Klaudia Biczysko and Emma Wallerö.	Date: 11.3.2021

## Technologies
Language:
* Python3

Project is created with the following libraries:
* pickle
* yaml
* scikit-learn
* spacy
* numpy
* os
* argparse
* re

## Setup
To run this project, make sure you have the libraries listed
in the previous chapter installed.

Mode: train.
To train a file use mode "train" (see below). A configuration file specifying
a train file and a model file is needed.

Mode: tag
To tag a file or text you need to specify text string or txt-document in the
text-argument, see below. If text is document, the output will be saved in
a file in the same directory with the extension "txt.tag".

Mode: eval
To evaluate your model you need a gold standard. The gold standard should be in
either txt or conllu format. For script command, see example below.

Variable names used in examples:
config_file = a configuration file. File extension is needed (ex: config.yaml)
some_text = a text string or a text-file. (ex: "I love dogs" or macbeth.txt)
gold_standard = a gold standard in either txt or conllu format (ex: gold_standard.conllu)

Call the scripts as follows:
```
$ python3 run.py --mode train --config config_file
$ python3 run.py --mode tag --text some_text --config config_file
$ python3 run.py --mode eval --gold gold_standard.conllu --config config_file

```
## Details

For our model we decided on using the linearSVC model as suggested,
along with the DictVectorizer which was also suggested. We also trained our tagger
with the DecisionTreeClassifier and CountVectorizer. However, the results were
slightly worse and so we settled on the original model and vectorizer.

The features we added resulted in a slight improvement of performance. For unknown words,
the improvement is especially improved by the added features. While the original features
gained a precision on 0.71 and a recall on 0.52 for unknown words, our added features resulted in
a precision on 0.82 and a recall on 0.59. The average recall and precision was raised by 1 percent.

When it comes to our code, we added:
In run.py:
- code for tagging whole files in run()
- code for evaluation mode

In pre_process.py:
- added 8 new features (see pre_process.py)

In model.py:
- added method tag_document() inside POSTagger class.
- added method evaluate() inside POSTagger class.
- (While evaluating different models we assigned variables differently
   in init-method of POSTagger class, see comments in model.py)
