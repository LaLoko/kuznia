#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import time
from pandas.api.types import is_numeric_dtype


# In[2]:


df = pd.read_csv("diabetic_data.csv",sep=',', header=0, error_bad_lines=False, low_memory=False, decimal='.')
df


# In[16]:


def string_to_value(column):
    dict = {}
    k = 0
    unique = df[column].unique()
    for unique_value in unique:
        dict[unique_value] = k
        k+=1
    return dict


# In[17]:

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


# In[18]:

i = input("podaj numer kolumny: ")
i = int(i)
colnames = df.columns.get_values()
colnames.tolist()
column_name = colnames[i]
plot_column(df,column_name)

def plot_everything(df):
    i=0
    colnames = df.columns.get_values()
    colnames.tolist()
    for j in colnames:
        column_name = colnames[i]
        plot_column(df,column_name)
        i+=1

#plot_everything(df)




