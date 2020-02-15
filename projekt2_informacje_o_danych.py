import pandas as pd
import numpy as np
import string
from tabulate import tabulate
import matplotlib.pyplot as plt
from collections import Counter
from tkinter import *

#rysowanie ramki ascii
def box_lines(lines, width):
    topBottomRow = "+" + "-" * width + "+"
    middle = "\n".join("|" + x.ljust(width) + "|" for x in lines)
    return "{0}\n{1}\n{0}".format(topBottomRow, middle)
def split_line(line, width):
    return [line[i:i+width] for i in range(0, len(line), width)]

def split_msg(msg, width):
    lines = msg.split("\n")
    split_lines = [split_line(line, width) for line in lines]
    return [item for sublist in split_lines for item in sublist] # flatten
def border_msg(msg, width):
    return(box_lines(split_msg(msg, width), width))


# import danych do DF
data = pd.read_csv("diabetic_data_initial.csv")
df = pd.DataFrame(data)

pd.set_option('display.max_columns', 50)  # dzięki temu wyświetla wszystkie kolumny
#podmiana nanow
col_names_list = df.columns
df[col_names_list] = df[col_names_list].replace({'?': np.nan})

stats = []
# tablica typow kolumn
dtypes = []
for i in col_names_list:
    if str(df[i][1]).isnumeric():
        dtypes.append('numeric column')
    elif str(df[i][1]).isascii():
        dtypes.append('text column')
    else:
        dtypes.append('kategoric column')

# tabela NaNów w kolumnach posortowanych rosnąco
nans = []
for i in col_names_list:
    stats.append(df[i].value_counts())
    l = list(df[i])
    if l.count(np.nan) > 0:
        nans.append([i, round((l.count(np.nan) / df.shape[0]) * 100, 2)])

nans.sort()
# zapis danych do pliku
plik = open('wyniki.txt', 'w')
plik.write('COLUMN STATISTICS\n\n\n')
plik.write(str(df.describe().round()))
plik.write('\n\nINFORMATION ABOUT COLUMNS VALUES\n\n')

c_nr = 0
for i in stats:
    unique = 0
    c = 1
    hd = ''
    if len(i) <= 20:
        arr = str(i).splitlines()
        head = arr[len(arr) - 1].split(',')[0]
        arr.append(dtypes[c_nr])
        arr.append('Column number : '+str(c_nr))
        arr.append(head)
        arr.reverse()
        for j in arr:
            if c > 4:
                    plik.write(j)
                    plik.write('   '+str(((int(j.split()[1]) / df.shape[0])*100).__round__(2))+' %  of total')
                    plik.write('\n')

            elif c == 4:
                plik.write(border_msg(hd,30)+'\n')
            else :
                hd +=j+'\n'
            c+=1
        for i in nans:
            if head.split()[1] == i[0]:
                plik.write('\n'+str(i[1])+' % of NaNs\n')
        plik.write('\n')
    else:
        arr = str(i).splitlines()
        head = arr[len(arr) - 1].split(',')[0]
        arr.pop()
        for j in arr:
            if j[0] not in arr: unique += 1
        hd +=head + '\n'
        hd+='Column number : '+str(c_nr)+'\n'
        hd+=dtypes[c_nr]+'\n'
        plik.write(border_msg(hd,30)+'\n')
        plik.write('number of values :' + str(len(arr)) + '\n')
        plik.write('number of uniques:' + str(unique) + '\n\n')
        for i in nans:
            if head.split()[1] == i[0]:
                plik.write('\n'+str(i[1])+' % of NaNs\n')
    c_nr += 1

# plik.write("INFORMATION ABOUT NaN VALUES\n\n")
# for i in nans:
#     plik.write('column name :' + i[0] + '\n')
#     plik.write('percent of NaNs : ' + str(i[1]) + '%\n\n')



