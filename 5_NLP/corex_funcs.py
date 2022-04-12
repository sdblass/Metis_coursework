#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from translate import Translator
from corextopic import corextopic as ct


# In[5]:


def corex(country, data, num_topics=3):
    country = country.lower()
    
    vectorizer = CountVectorizer(max_features=2500,
                             stop_words='english', 
                             token_pattern="\\b[a-z][a-z]+\\b",
                             binary=True)
    
    data = data.loc[data.country==country].spacy_doc_cleaned.copy()

    doc_word = vectorizer.fit_transform(data)
    words = list(np.asarray(vectorizer.get_feature_names_out()))
    
    topic_model = ct.Corex(n_hidden= num_topics , ### YOUR NUMBER OF TOPICS HERE
                       words= words  ,   ### YOUR VOCABULARY HERE
                       seed=1
                       )

    topic_model.fit(  doc_word  ,       ### YOUR DOCUMENT TERM MATRIX HERE
                    words= words   , ### YOUR VOCABULARY HERE
                    docs= data      ### YOUR DOCUMENT SERIES HERE
                    )
    
    topics = topic_model.get_topics()
    for n,topic in enumerate(topics):
        topic_words,_,_ = zip(*topic)
        print(f'{n}: {", ".join(topic_words)}')


# In[6]:


def corex_anchors(country, anchors, data, anchor_strength=5, num_topics=3):
    '''anchors take the form [[anchor1, anchor2, etc.], [anchor3], [anchor4]] if there are 3 topics'''
    country = country.lower()
    
    vectorizer = CountVectorizer(max_features=2500,
                             stop_words='english', 
                             token_pattern="\\b[a-z][a-z]+\\b",
                             binary=True)
    
    data = data.loc[data.country==country].spacy_doc_cleaned.copy()

    doc_word = vectorizer.fit_transform(data)
    words = list(np.asarray(vectorizer.get_feature_names_out()))
    
    topic_model = ct.Corex(n_hidden= num_topics, ### YOUR NUMBER OF TOPICS HERE
                       words= words,  ### YOUR VOCABULARY HERE
                       seed=1
                       )

    topic_model.fit( doc_word ,          ### YOUR DOCUMENT TERM MATRIX HERE
                    words= words ,      ### YOUR VOCABULARY HERE
                    docs= data ,        ### YOUR DOCUMENT SERIES HERE
                    anchors=anchors,          ### YOUR ANCHOR LISTS HERE
                    anchor_strength= anchor_strength  ### YOUR ANCHOR STRENGTH HERE
                    );
    
    topics = topic_model.get_topics()

    for n,topic in enumerate(topics):
        topic_words,_,_ = zip(*topic)
        print(f'{n}: {", ".join(topic_words)}')
        
    topic_colms = ['topic'+str(i) for i in range(topic_model.labels.shape[1])]

    predictions = pd.DataFrame(topic_model.labels, columns=topic_colms)
    
    i = 0
    for topic in topic_colms:
        topic_perc = predictions[topic].sum()/predictions[topic].count()*100
        topic_perc = round(topic_perc, 2)
        print(f'Percent Topic {i} Documents: {topic_perc}%')
        i += 1


# In[10]:


def corex_translate(language, data, num_topics=3):
#     country = country.lower()
    
    vectorizer = CountVectorizer(max_features=2500,
                             stop_words='english', 
                             token_pattern="\\b[a-z][a-z]+\\b",
                             binary=True)
    
    data = data.loc[data.language==language].spacy_doc_cleaned.copy()

    doc_word = vectorizer.fit_transform(data)
    words = list(np.asarray(vectorizer.get_feature_names_out()))
    
    topic_model = ct.Corex(n_hidden= num_topics , ### YOUR NUMBER OF TOPICS HERE
                       words= words  ,   ### YOUR VOCABULARY HERE
                       seed=1
                       )

    topic_model.fit(  doc_word  ,       ### YOUR DOCUMENT TERM MATRIX HERE
                    words= words   , ### YOUR VOCABULARY HERE
                    docs= data      ### YOUR DOCUMENT SERIES HERE
                    )
    
    topics = topic_model.get_topics()
    
    results = {}

    translator= Translator(from_lang=language,to_lang="en")
    
    for n,topic in enumerate(topics):
        topic_words,_,_ = zip(*topic)
        print(f'{n}_{language}: {", ".join(topic_words)}')

        topic_words_en = [translator.translate(word) for word in topic_words]
       
        print(f'{n}_en: {", ".join(topic_words_en)}')
        
        print('\n')
        
        results[n] = topic_words
        results[str(n) + '_en'] = topic_words_en
        
    return results
        


# In[11]:


def corex_anchors_translate(language, anchors, data, anchor_strength=5, num_topics=3):
    '''anchors take the form [[anchor1, anchor2, etc.], [anchor3], [anchor4]] if there are 3 topics'''

    # translate anchors from English to target language

    translator= Translator(from_lang='en',to_lang=language)
  
    for row_index, row in enumerate(anchors):
        for col_index, value in enumerate(row):
            anchors[row_index][col_index] = translator.translate(value).lower()
            
    print(f'Translated anchors from en to {language}: {anchors}')
    
    vectorizer = CountVectorizer(max_features=2500,
                             stop_words='english', 
                             token_pattern="\\b[a-z][a-z]+\\b",
                             binary=True)
    
    data = data.loc[data.language==language].spacy_doc_cleaned.copy()

    doc_word = vectorizer.fit_transform(data)
    words = list(np.asarray(vectorizer.get_feature_names_out()))
    
    topic_model = ct.Corex(n_hidden= num_topics, ### YOUR NUMBER OF TOPICS HERE
                       words= words,  ### YOUR VOCABULARY HERE
                       seed=1
                       )

    topic_model.fit( doc_word ,          ### YOUR DOCUMENT TERM MATRIX HERE
                    words= words ,      ### YOUR VOCABULARY HERE
                    docs= data ,        ### YOUR DOCUMENT SERIES HERE
                    anchors=anchors,          ### YOUR ANCHOR LISTS HERE
                    anchor_strength= anchor_strength  ### YOUR ANCHOR STRENGTH HERE
                    );
    
    topics = topic_model.get_topics()
    
    results = {}

    translator= Translator(from_lang=language,to_lang='en')
    
    for n,topic in enumerate(topics):
        topic_words,_,_ = zip(*topic)
        print(f'{n}: {", ".join(topic_words)}')
        
        topic_words_en = [translator.translate(word) for word in topic_words]
        print(f'{n}_en: {", ".join(topic_words_en)}')
        
        print('\n')
        
        results[n] = topic_words
        results[str(n) + '_en'] = topic_words_en
    
    topic_colms = ['topic'+str(i) for i in range(topic_model.labels.shape[1])]

    
    
    predictions = pd.DataFrame(topic_model.labels, columns=topic_colms)
    
    i = 0
    for topic in topic_colms:
        topic_perc = predictions[topic].sum()/predictions[topic].count()*100
        topic_perc = round(topic_perc, 2)
        print(f'Percent Topic {i} Documents: {topic_perc}%')
        i += 1

