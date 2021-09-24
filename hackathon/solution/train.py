import numpy as np
import pandas as pd
from sklearn.cluster import Birch
import pickle as pkl

train_filename = "train.csv"

columns_to_exclude = ['city', 'floor', 'id', 'osm_city_nearest_name', 'region',
                      'street', 'date', 'realty_type', 'per_square_meter_price', 'price_type']

df = pd.read_csv(train_filename)
df = df.dropna()
pd.set_option('display.max_columns', None)
# print(df.head())
# print(df.describe())
# print(df.columns)

headers = []

for w in df.columns:
    if w not in columns_to_exclude:
        headers.append(w)


a = df[headers].values

M = np.atleast_2d(a).shape[1]

# print(M)
P = df['per_square_meter_price'].values

records = len(P)

model = Birch(threshold=1000, n_clusters=M)
model.fit(a)

yhat = model.predict(a)
clusters = np.unique(yhat)

P1 = np.zeros(M)
a1 = np.zeros((M, M))
i = 0

#усредняем внутри кластера
for cluster in clusters:
    row_ix = np.where(yhat == cluster)
    P1[i] = np.mean(P[row_ix])
    a1[i] = np.mean(a[row_ix], axis=0)
    i += 1

res = np.linalg.solve(a1, P1)
with open('model.pkl', 'wb') as f:
    pkl.dump(res, f)
