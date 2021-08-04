## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Details](#details)

## General info
This project prints the content of the English Wikipedia page for a search term.
You can search for terms with non-ASCII characters.

## Technologies
Language:
* Python3

Project is created with the following libraries:
* BeautifulSoup
* urllib.request
* requests

## Setup

To run this project, make sure you have the libraries listed
in the previous chapter installed.

To search for the term, open the command prompt, open the directory, where the code is saved and run below command:
To look for multiword terms, use underscore.

Variable names used in example:
term = a term inside quotes.

 Call the script as follows:
```
$ python3 wiki_query.py term
$ python3 wiki_query.py "Ankylosaurus"
$ python3 wiki_query.py "Miloš_Zeman"

```
## Details

There are two error messages which you may get while running the script.

* "The page does not exist." means that there is no wikipedia article for the
   search term.
* "You need to be more specific. Your search term seems to have several meanings."
   is perhaps self-explanatory.

In the code we are looking for text inside "\<p>" and "\</p>" in the HTML code
of the wikipedia page for the search term.

When there is no corresponding page for the search term wikipedia does not give
an error, but returns a page with information about there being no article.
Instead of displaying this page, we decided to set variable soup to None in order
to get an AttributeError and print an error message.

When a search term is underspecified, we set a variable "several" to True, and set
variable "soup" to None. When both these conditions are true, we print an
error message addressing the problem.
