import pandas as pd
import numpy as np
import collections

data = pd.read_csv("RPL.csv", encoding = 'cp1251', delimiter=';')
tL = pd.array(['Анжи', 'Ахмат', 'Зенит', 'Краснодар', 'Локомотив', 'Ростов', 'Рубин', 'Спартак', 'Урал', 'Уфа', 'ЦСКА'])
print(tL)

deleteTeam = [x for x in pd.unique(data['Соперник']) if x not in tL]
for name in deleteTeam:
    data = data[data['Команда'] != name]
    data = data[data['Соперник'] != name]
data = data.reset_index(drop=True)