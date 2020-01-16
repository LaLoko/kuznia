import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt

data=pd.read_csv("C:/Users/Krzysztof/PycharmProjects/kuźnia_zad1/diabetic_data_initial.csv")
# data=pd.read_csv("C:/Users/Krzysztof/PycharmProjects/kuźnia_zad1/diabetic_data_initial.csv", usecols=["race", "gender", "age", "weight", "readmitted"])

#zamiana nieznanych danych na nan
col = data.columns
data[col] = data[col].replace({'?':np.nan})

#obsluga znakow nieliczbowych
data['diabetesMed']=data['diabetesMed'].map(dict(Yes=1, No=0))
data['change']=data['change'].map(dict(Ch=1, No=0))

#rysowanie histogramow
select_col = ["race", "gender", "age", "weight", "readmitted"]

fig, axs = plt.subplots(1,(len(select_col)))
axs = axs.ravel()
for i, element in enumerate(data[select_col]):
    data[element].value_counts().plot(kind="bar", ax=axs[i]).set_title(element)

plt.show()

#rysowanie rozrzutu
#rozrzut ma pokazywać ilosć kobiet/mężczyzn w zależności od rasy

girls_grades = data[data['gender'].map(lambda item: 'Female' in item)]
girls_race = girls_grades['race'].value_counts()
boys_grades = data[data['gender'].map(lambda item: 'Male' in item)]
boy_race = boys_grades['race'].value_counts()
