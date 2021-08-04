## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Details](#details)

## General info

A term plotter for the data of the US presidential speeches that was webscraped
by Artur. This is a part of assignment 3 in the course Advanced programming
for language technologists.

## Technologies
Language:
* Python3

Project is created with the following libraries:
* numpy
* pandas
* seaborn
* os
* json
* sklearn
* argparse
* matplotlib


## Setup
To run this project, make sure you have the libraries listed
in the previous chapter installed.

Variable names used in example:

* some_terms = 1 to 5 terms in quotations, separated by whitespace. Each term \
can consist of three tokens. (ex: "america" "united states")
* plot_title = An optional argument that adds a title to the plot. \
(ex: "america v.s united states")
* output_filename = An optional argument that saves the plot to the specified \
output filename. (ex: "my_output_file")
* directory = An optional argument that specified where the directory of the \
speeches is. (ex: "/us_presidential_speeches/")

```
$ python3 term_plotter.py --terms some_terms --title plot_title --output output_filename --path

```
## Details

When scoring the terms in vectorize() we firstly create a TfidfVectorizer-object
and we fit the corpus into it. If the terms are found in our data, this
information is extracted at put into lists which are later used for our pandas
dataframe. By using seaborn, we create a plot with the desired terms based
on the data from the pandas dataframe.

If one of the terms is not in the corpus, the program prints information about
this, and a plot is created without this term.
If none of the terms is in the corpus, an error is printed and no plot is made.
If the specified path is not correct/does not exist an error message is printed.
