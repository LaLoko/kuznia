import pandas as pd
import numpy as np
from tkinter import *

#import danych do DF
data = pd.read_csv("diabetic_data_initial.csv")
df = pd.DataFrame(data)

pd.set_option('display.max_columns',50)#dzięki temu wyświetla wszystkie kolumny
col = df.columns
df[col] = df[col].replace({'?': np.nan})

col_names_list = df.columns
stats = []
#to wypluwa tabelkę nazwa, ilosć kolumn, ilość nanów (pierwotnie miałbyć procent ważnych danych w kolumnie)
#nie do końca mi się podoba wynika ale chyba dobrze
for i in col_names_list:
    name = i
    n_val = len(df[i])
    count = 0
    for j in df[i]:
        #print(j)
        if pd.isna(j):
            count=+1
    stats.append([name,count,n_val])

print(stats)

#GUI
app = Tk()
app.geometry('800x600')
app.title('simple test GUI')
app.mainloop() #to wyświetla okienko, można wykomentować
