
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import pandas as pd
import sys 

dataset = pd.read_csv('Iris.csv')
x = dataset.iloc[:, [1, 2, 5]].values

for i in range(len(x)):
    if x[i][2] == 'Iris-setosa': x[i][2] = 0
    elif x[i][2] == 'Iris-versicolor': x[i][2] = 1
    elif x[i][2] == 'Iris-virginica': x[i][2] = 2


plt.scatter(x[:, 0], x[:, 1], s = 50, c = x[:,2])
plt.xlabel('SepalLengthCm')
plt.ylabel('SepalWidthCm')
plt.legend()
plt.show()

x = dataset.iloc[:, [1, 2]].values

kmeans = KMeans(n_clusters=3, init='random', n_init=2, max_iter=3, precompute_distances='auto', verbose=0, random_state=None, copy_x=True, n_jobs=None, algorithm='auto')
y_kmeans = kmeans.fit_predict(x)

plt.scatter(x[y_kmeans == 0, 0], x[y_kmeans == 0, 1], s = 50, c = 'red', label = 'Iris-setosa')
plt.scatter(x[y_kmeans == 1, 0], x[y_kmeans == 1, 1], s = 50, c = 'blue', label = 'Iris-versicolour')
plt.scatter(x[y_kmeans == 2, 0], x[y_kmeans == 2, 1], s = 50, c = 'green', label = 'Iris-virginica')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:,1], s = 100, c = 'black',marker = 'x', label = 'Centroids')
plt.xlabel('SepalLengthCm')
plt.ylabel('SepalWidthCm')
plt.legend()
plt.show()