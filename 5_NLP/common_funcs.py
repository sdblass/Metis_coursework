#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests, re, time, random, math, pickle
from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np
from selenium import webdriver
from urllib.request import urlopen
import urllib.parse
from IPython.display import display
import matplotlib.pyplot as plt
import seaborn as sns
import Levenshtein as lev
from sklearn.model_selection import train_test_split


def get_soup_driver(base_url, driver): # Retrieves soup from website using Selenium
#     driver = webdriver.Chrome()
    driver.get(base_url)
    time.sleep(11 + random.uniform(-1,1))
    r = driver.page_source
    
#     driver.quit()
    return bs(r, 'html.parser')  

# In[ ]:


def print_full(x):
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 2000)
    pd.set_option('display.float_format', '{:20,.2f}'.format)
    pd.set_option('display.max_colwidth', None)
    print(x)
    pd.reset_option('display.max_rows')
    pd.reset_option('display.max_columns')
    pd.reset_option('display.width')
    pd.reset_option('display.float_format')
    pd.reset_option('display.max_colwidth')
    
def full_print(x):
    return print_full(x)

