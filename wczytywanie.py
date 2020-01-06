import pandas as pd
import os

headers = []
dane = []
if os.path.isfile('diabetic_data_initial.csv'):
    with open('diabetic_data_initial.csv', "r") as zawartosc:
        count = 0

        for linia in zawartosc:
            if (count == 0):
                linia = linia.replace("\n", "")
                linia = linia.replace("\"", "")
                headers = linia.split(",")
                count += 1
            else:
                linia = linia.replace("\n", "")
                linia = linia.replace("\"", "")
                dane.append(tuple(linia.split(",")))

data = pd.DataFrame(dane)
data.columns = headers