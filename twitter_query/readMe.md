## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Details](#details)

## General info

This program allows you to print recent tweets from a specific twitter user.

## Technologies
Language:
* Python3

Project is created with the following libraries:
* tweepy

## Setup
To run this project, make sure you have the libraries listed
in the previous chapter installed.

Variable names used in example:
* twitter_user = A twitter username. (ex: zaralarsson, beyonce)
* number_of_tweets = Number of recent tweets to be printed. This variable \
is optional. Default value is 1. (ex: 10)

Call the script as follows:
```
$ python3 twitter_query.py twitteruser number_of_tweets
$ python3 twitter_query.py twitteruser

```
## Details

By setting the attribute "include_rts" to False, we do not include retweets.
Emojis are printed. Pictures are visible as links.
A tweet is a reply when it starts with another username. However we do not \
distinguish these from regular tweets.

If number of tweets is not specified we do not want an IndexError interrupting
the query. Therefore we use try, except. When there is an IndexError the
number of tweets is set to the default value 1.
