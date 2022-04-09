# Analysis of differences in topics and sentiments on Reddit posts pertaining to the Ukraine-Russia conflict

## Objective
The goal of this project is to visualize any differences in the topics and sentiments of Reddit posts as they relate to the Ukraine conflict. Governments can benefit from a text analysis of social media to gauge their public’s appetite for various ways to respond to the conflict. Governments could also benefit from knowing how the public in allied and adversarial countries are reacting to the conflict.  With this project, I will attempt to generate a model that extracts what topics people in democratic and autocratic countries are discussing as well as associated sentiments.

## Solution path
The data set contains Reddit posts for a range of countries that represent the types of responses countries have taken to the conflict. The categories of responses are represented by countries with the highest GDPs in those categories. Most have condemned the Russian invasion but others have taken a more neutral tone. The final product will contain 
* A VADER sentiment analysis of all English posts.
* A list of top adjectives describing various world leaders for different subreddits (the main comparison being the Russia subreddit which was restricted due to allegations of misinformation and the Ukraine subreddit which is the largest set of data collected so far.)
* A topic analysis for each sentence of each post that will match up with a sentiment score and compared across different countries.

## Current progress
### Work status
Data acquisition is complete. The final data set was broken up by sentence and contains the following features:
* post_number (a unique identifier)
* country (the name of the subreddit)
* comments_or_subs (whether the post is a comment or submission)
* democracy_score (an index compiled by the Economist Intelligence Unit and scraped from [Wikipedia](https://en.wikipedia.org/wiki/Democracy_Index)
* GDP (gross domestic product)
* abstained (whether the country abstained on [United Nations General Assembly Resolution ES-11/1](https://en.wikipedia.org/wiki/United_Nations_General_Assembly_Resolution_ES-11/1)
* text (the body of the post)
* language
* provided_aid (whether the country [provided aid of any kind](https://en.wikipedia.org/wiki/List_of_foreign_aid_to_Ukraine_during_the_Russo-Ukrainian_War)
* spacy_doc (the parsed posts using SpaCy)

### Initial findings
Subreddits with fewer than 1000 English posts were eliminated from analysis. Subsequent sentiment analysis broken up by country does show the Russia subreddit has more positive sentiment than the Ukraine subreddit. There appears to be no relationship between sentiment and GDP or democracy score. This could indicate that countries are not responding to the will of their people although this may not be surprising given the rapid evolution of events.

![countries](https://github.com/sdblass/Metis_coursework/blob/master/5_NLP/MVP/images/countries_sentiment.png)

![GDP](https://github.com/sdblass/Metis_coursework/blob/master/5_NLP/MVP/images/GDP.png)

![democracy](https://github.com/sdblass/Metis_coursework/blob/master/5_NLP/MVP/images/democracy.png)