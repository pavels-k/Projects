import numpy as np
import pandas as pd
import pickle as pkl

test_filename = "test.csv"
o_name = "test_submission.csv"

columns_to_exclude = ['city', 'floor', 'id', 'osm_city_nearest_name', 'region',
                      'street', 'date', 'realty_type', 'per_square_meter_price', 'price_type']

headers = []

with open('model.pkl', 'rb') as f:
    res = pkl.load(f)

df1 = pd.read_csv(test_filename)

for w in df1.columns:
    if w not in columns_to_exclude:
        headers.append(w)

vec = df1[headers].values
id_s = df1['id'].values

f = open(o_name, "w")
f.write('id,per_square_meter_price \n')
i = 0
for k in id_s:
    f.write(k+','+np.format_float_positional(np.vdot(res, vec[i]))+'\n')
    i += 1
f.close()
print('done')
