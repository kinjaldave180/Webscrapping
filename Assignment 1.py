#!/usr/bin/env python
# coding: utf-8

# In[3]:


pip install requests


# In[4]:


pip install bs4


# In[39]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[40]:


url ="http://quotes.toscrape.com/"


# In[41]:


response = requests.get(url)


# In[42]:


response.content


# In[43]:


soup = BeautifulSoup(response.content,"html.parser")


# In[44]:


print(soup.prettify())


# In[45]:


soup.title


# In[46]:


soup.title.name


# In[47]:


soup.title.string


# In[48]:


soup.title.parent.name


# In[49]:


soup.a


# In[50]:


soup.span.text


# In[51]:


quotes = soup.find_all('div',{'class':'quote'})


# In[52]:


for i in quotes:
    print((i.find('span',{'class':'text'})).text)
    
    


# In[53]:


for i in soup.findAll('div',{'class':'quote'}):
    print((i.find('small',{'class':'author'})).text)
    


# In[54]:


for i in soup.findAll('div',{'class':'tags'}):
    print((i.find("meta"))['content'])
    


# In[55]:


root = 'http://quotes.toscrape.com/page/'


# In[62]:


quotes=[]
authors=[]
tags=[]


# In[65]:


for pages in range(1,10):
    
    html = requests.get(root + str(pages))
    soup = BeautifulSoup(html.text)
    
    for i in soup.findAll('div',{'class':'quote'}):
            quotes.append((i.find('span',{'class':'text'})).text)
                          
    for j in soup.findAll('div',{'class':'quote'}):
            quotes.append((j.find('small',{'class':'author'})).text)
            
    for k in soup.findAll('div',{'class':'tags'}):
            quotes.append((k.find('meta'))['content'])
                          
                          


# In[64]:


df = pd.DataFrame(
     {'Quotes':quotes,
      'Authors':authors,
      'Tags':tags
      })


# In[ ]:




