# Text Analysis of Reddit Posts on the Russia-Ukraine War
## Summary
The goal of this project is to use natural language processing tools to visualize differences in the topics and sentiments of posts about the Ukraine conflict, broken down by the subreddits of various countries. The countries range in GDP, system of government, level of support for Ukraine as expressed by votes at the United Nations or in pledges of military or humanitarian aid. Valuable insight could be gained by probing sentiments on social media forums like Reddit rather than get information filtered through government officials. Governments can also use an analysis of Reddit to inform their responses to the conflict. Outlined in this project is a method for extracting topics and sentiments from Reddit data, broken down by country and key terms.

## Design
The data come from Reddit posts made between Feb 23 and April 2, starting at one day prior to the invasion for a total of about 5 weeks of data. Posts are categorized by country with the subreddit title as a replacement for country name. Data on the posters' countries of origin were unavailable. The final data set contained each country's GDP, democracy index (a measure of how democratic a government is), and features that indicate a country's level of support for Ukraine or Russia. Text analysis reveals sentiments for each country broken down by key terms such as world leaders, as well as topic modeling. The presence of absence of any relationship between sentiment towards particular terms and factors such GDP or democracy index are shown in pair-plots.

## Data
The data come from Reddit via "PushshiftAPI," a third-party service that stores a repository of all Reddit posts and permits scraping of historical Reddit data. Posts were scraped if they contained at least one of a number of terms related to the Ukraine conflict such as `Ukraine`, `Putin`, `Zelensky`, etc. The final data set contained 14,399,110 non-unique terms across 257,562 posts. English posts make up 84% of the data and is the only language for which sentiment analysis was readily available. Therefore, the analysis was restricted to English posts only. Translation from other languages to English proved beyond the scope of this project. The data set contains the following features:
* post_number (a unique identifier)
* country (the name of the subreddit)
* comments_or_subs (whether the post is a comment or submission)
* democracy_score (an index compiled by the Economist Intelligence Unit and scraped from Wikipedia
* GDP (gross domestic product)
* abstained (whether the country abstained on United Nations General Assembly Resolution ES-11/1
* provided_aid (whether the country provided aid of any kind
* text (the body of the post)
* language
* spacy_doc (the parsed posts using SpaCy)

Countries were chosen by grouping them by region and selecting the five with the highest GDPs. Countries that abstained on the UN resolution condemning the Russian invasion were added to the data set to avoid a class imbalance, given the small number of countries that voted in that manner.

## Algorithms
### Cleaning
Subreddits with fewer than 1000 posts were eliminated from analysis to avoid misleading results caused by the small number of observations. Posts for sentiment analysis were eliminated if the total count per key term was less than 20 for the same reason. Spell-check was run on all of the posts.

### Pre-processing
The data was word-tokenized and lemmatized.

### Sentiment analysis
Posts were sentence-tokenized and sentiment scores were calculated for each subreddit (country). Sentiment by key terms was calculated by calculating sentiment scores only for posts containing those key terms (e.g. `putin`, `zelensky`, `biden`) for each subreddit of interest.

### Topic modeling
Topic modeling was done with CorEx to help extract topics that would otherwise be dominated by prominent topics such as `Russia`, `Ukraine`, or `Invasion`.

## Tools
* Data acquisition: Python, Pushshift Reddit API
* Analysis: Pandas, NLTK, gensim, langdetect, CorEx, VADER, SpaCy
* Visualization: Matplotlib, Seaborn

## Communication
* Slides, visuals, write-up

