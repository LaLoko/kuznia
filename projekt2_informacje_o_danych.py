import pandas as pd
import numpy as np
from tabulate import tabulate
import matplotlib.pyplot as plt
from collections import Counter
from tkinter import *

#import danych do DF
data = pd.read_csv("diabetic_data_initial.csv")
df = pd.DataFrame(data)

pd.set_option('display.max_columns',50)#dzięki temu wyświetla wszystkie kolumny
col_names_list = df.columns
df[col_names_list] = df[col_names_list].replace({'?': np.nan})

stats = []

#tabela NaNów w kolumnach posortowanych rosnąco
nans = []
for i in col_names_list:
    stats.append(df[i].value_counts())
    l = list(df[i])
    if l.count(np.nan) > 0:
        nans.append([i,round((l.count(np.nan)/df.shape[0])*100,2)])

nans.sort()

#zapis danych do pliku
plik = open('wyniki.txt','w')
plik.write('COLUMN STATISTICS\n\n\n')
plik.write(str(df.describe().round()))
plik.write('\n\nINFORMATION ABOUT COLUMNS VALUES\n\n')

for i in stats:
    unique = 0
    if len(i) <= 10:
        arr = str(i).splitlines()
        head = arr[len(arr)-1].split(',')[0]
        arr.pop()
        arr.insert(0,head)
        for j in arr:
            plik.write(j+'\n')
        plik.write('\n')
    else:
        arr = str(i).splitlines()
        head = arr[len(arr) - 1].split(',')[0]
        arr.pop()
        for j in arr:
            if j[0] not in arr: unique+=1
        plik.write(head+'\n')
        plik.write('number of values :'+str(len(arr))+'\n')
        plik.write('number of uniques:'+str(unique)+'\n\n')

plik.write("INFORMATION ABOUT NaN VALUES\n\n")
for i in nans :
    plik.write('column name :'+i[0]+'\n')
    plik.write('percent of NaNs : '+str(i[1])+'%\n\n')





#robienie tabelki ascii ze statystyk
# statystyki_podstawowe = pd.DataFrame(statystyki_podstawowe)
# cols = list()
# pom_tab = pd.DataFrame
# col_nr = 0
# for j in range(1,5):
#     pom_col = list()
#     pom_tab = []
#     for i in range(1,9):
#         pom_col.append(col_names_list[col_nr])
#         pom_tab.append(df[pom_col].describe())
#         col_nr+=1
#     pom_col.insert(0,'stats')
#     pom_tab.append(statystyki_podstawowe[col_nr])
#     plik.write(str(tabulate(pom_tab, headers=pom_col, tablefmt='psql')))


#plik.write(str(tabulate(statystyki_podstawowe, headers=pom_col, tablefmt='psql')))

