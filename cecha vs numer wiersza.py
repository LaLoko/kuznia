#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import time
from pandas.api.types import is_numeric_dtype
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv("diabetic_data.csv",sep=',', header=0, error_bad_lines=False, low_memory=False, decimal='.')
#ograniczenie liczby wierszy do co setnego
df = df[df.index % 100 == 0]


# In[3]:


df


# In[16]:


def string_to_value(column):
    dict = {}
    k = 1
    unique = df[column].unique()
    unique = sorted(set(unique))
    for unique_value in unique:
        if (unique_value == "nan" or unique_value == "NaN" or unique_value == "NULL" or unique_value == "?" ):
            #nadanie skrajnej liczby latwo widocznej do wyznaczania nulli na wykresie
            dict[unique_value] = 0
        else:
            dict[unique_value] = k
            k+=1
    print(dict)
    return dict


# In[5]:


def plot_column(df,column):
    if (is_numeric_dtype(df[column]) == True):
        plt.interactive(True)
        df.plot(y=column, use_index=True)
        plt.show(block=True)
    else:
        dict = string_to_value(column)
        df = df.replace({column: dict})
        plt.interactive(True)
        df.plot(y=column, use_index=True)
        plt.show(block=True)


# In[6]:


def plot_everything(df):
    i=0
    colnames = df.columns.get_values()
    colnames.tolist()
    for j in colnames:
        column_name = colnames[i]
        plot_column(df,column_name)
        i+=1


# In[17]:


plot_everything(df)


# In[8]:


plot_column(df,'weight')


# In[14]:


plot_column(df,'gender')


# In[ ]:




