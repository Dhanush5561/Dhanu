#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# In[3]:


data=pd.read_csv("play.csv")


# In[4]:


data


# In[11]:


concept=np.array(data)[:,0:-1]


# In[6]:


concept


# In[7]:


target=np.array(data)[:,-1]


# In[8]:


target


# In[9]:


def train(c,t):
    for i,val in enumerate(t):
        if val=="yes":
            hypothesis=c[i].copy()
            break
            
    for i,val in enumerate(concept):
        if t[i]=="yes":
            for x in range(len(hypothesis)):
                if val[x]!=hypothesis[x]:
                    hypothesis[x]='?'
                else:
                    pass
                
    return hypothesis


# In[10]:


train(concept,target)


# In[ ]:




