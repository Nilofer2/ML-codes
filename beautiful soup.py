#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# stretch Jupyter coding blocks to fit screen
from IPython.core.display import display, HTML
display(HTML("<style>.container { width:90% !important; }</style>")) 
# if 100% it would fit the screen


# In[3]:


# make it run on py2 and py3
from __future__ import division, print_function


# In[4]:


import requests 
import bs4 as bs
import pandas as pd
import re
from collections import Counter


# In[5]:


#source = requests.get("https://lahacks2017.devpost.com/submissions/search?utf8=✓&terms=blockchain&sort=")


# In[6]:


#


# In[7]:


#


# In[8]:


source2 = requests.get("https://lahacks2017.devpost.com/submissions")
hack_links = []


# In[9]:


soup = bs.BeautifulSoup(source2.content, features='html.parser')
links  = soup.find_all('a')



# In[10]:


source2 = requests.get("https://lahacks2017.devpost.com/submissions/search?utf8=✓&terms=machine+learning&sort=recent")


# In[23]:


hack_links2 = []
print('Relevant Links to machine learning:')
for url in links:
    y=url.get('href')
    if "software/" in y:
        print(y)
        hack_links.append(y)
a=len(hack_links)
print(a)


# In[12]:


source3 = requests.get("https://lahacks2017.devpost.com/submissions/search?utf8=✓&terms=ar+vr&sort=recent")


# In[13]:


soup = bs.BeautifulSoup(source3.content, features='html.parser')
links  = soup.find_all('a')


# In[14]:


hack_links3 = []
print('Relevant Links to ar and vr:')
for url in links:
    z=url.get('href')
    if "software/" in z:
        print(z)
        hack_links.append(z)




# In[15]:


source4 = requests.get("https://devpost.com/software/search?query=blockchain")


# In[16]:



soup = bs.BeautifulSoup(source4.content, features='html.parser') 
links = soup.find_all('a')


# In[17]:



hack_links4=[]


# In[18]:



print('Relevant Links to blockchain1 :')
for url in links:
    e=url.get('href')
    if "software/" in e:
        print(e)
        hack_links.append(e)


# In[19]:


source5=requests.get("https://devpost.com/hackathons")


# In[20]:


soup = bs.BeautifulSoup(source5.content, features='html.parser') 
links = soup.find_all('a')


# In[21]:


source5 = requests.get("https://devpost.com/software/search?query=machine+learning")
hacks_links5=[]
print('Relevant Links to machine learning1 :')
for url in links:
    f=url.get('href')
    if "software/" in f:
        print(f)
        hack_links.append(f)


# In[ ]:


import matplotlib.pyplot as plt


# In[ ]:





# In[ ]:





# In[ ]:





# 

# In[21]:


#print(source.content) 

# This is the HTML content of the website,
# as you can see it's quite hard to decipher

