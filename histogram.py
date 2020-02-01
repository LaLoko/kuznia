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

#pojedynczy histogram
pd.value_counts(data['race']).plot(kind="bar")
plt.show()

#rysowanie rozrzutu
#rozrzut ma pokazywać ilosć kobiet/mężczyzn w zależności od rasy

def scatter_plot(x, y):
    girls_grades = data[data[y].map(lambda item: 'Female' in item)]
    girls_race = girls_grades[x].value_counts().tolist()

    boys_grades = data[data[y].map(lambda item: 'Male' in item)]
    boys_race = boys_grades[x].value_counts().tolist()

    race = girls_grades[x].value_counts().keys().tolist()

    plt.scatter(race, girls_race, marker='o')
    plt.scatter(race, boys_race, marker='o')
    plt.show()

scatter_plot('race', 'gender')


# usunięcie nieznanych danych
data_hist = data_hist[data_hist.gender != 'Unknown/Invalid']
data_hist = data_hist[data_hist.race != '?']

# histogram
numer = int(input("Numer kolumny: "))
kolumna = data_hist[headers[numer]]

freqs = Counter(kolumna)
xvals = range(len(freqs.values()))
plt.bar(xvals, freqs.values(), color='#37777D')
plt.xticks(xvals, freqs.keys())
plt.suptitle('Histogram dla zmiennej ' + headers[numer])
plt.show()


# krzysiowy bardziej uniwersalny scatter, nadal nie jest idealny ale lepiej nie umiem

def scatter_plot(x, y):
    unique = np.unique(data_hist[y])
    race = data_hist[x].value_counts().keys().tolist()

    for i in range(len(unique)):
        temp = data_hist[data_hist[y].map(lambda item: unique[i] in item)]
        temp1 = temp[x].value_counts().tolist()
        plt.scatter(race, temp1, marker='o', s=[np.sqrt(i) * 15 for i in temp1])

    plt.legend(unique)
    plt.title("Scatter plot dla zmiennych " + x + " oraz " + y)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.show()


scatter_plot('age', 'race')
