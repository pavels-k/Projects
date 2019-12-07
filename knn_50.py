import matplotlib.pyplot as plt
import numpy as np
import math
from sklearn.model_selection import train_test_split

def evk(X_test, X_train, i, j):
    distance = math.sqrt((X_test[i][0] - X_train[j][0])**2 + (X_test[i][1] - X_train[j][1])**2)
    return distance

def modul_max(X_test, X_train, i, j):
    distance = max(abs(X_test[i][0] - X_train[j][0]), abs(X_test[i][1] - X_train[j][1]))
    return distance

def cosinus(X_test, X_train, i, j):
    distance = (X_test[i][0] * X_train[j][0] + X_test[i][1] * X_train[j][1])/((np.sqrt(X_test[i][0]**2 + X_test[i][1]**2)) * (np.sqrt(X_train[j][0]**2 + X_train[j][1]**2)))
    return distance


x = [[7,1], [1,0],[3,2],[3,5], [1,3],[0,2],[3,2],[8,7],[2,9],[3,3],[3,0],[3,2], [5,6], [6,3]]
z = [1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1]
print(z)
X_train, X_test, y_train, y_test = train_test_split(x, z, test_size=0.5, random_state=10)

k = 2
a = []
y_knn = []
for i in range(len(X_test)):
    a = []
    for j in range(len(X_train)):
        distance = cosinus(X_test, X_train, i, j)
        a.append([distance, y_train[j]])
    
    a = sorted(a, key=lambda c: c[0])
    i = 0
    j = 0
    l = 0
    while(i < k ) and (j < k):
        if(a[l][1] == 0): i=i+1
        else:  j = j+1
        l = l + 1
    if(i == k): y_knn.append(0)
    else: y_knn.append(1)


y_knn = np.array(y_knn)
y_test = np.array(y_test)
accuracy = np.mean(y_knn == y_test)
print(y_test)
print(y_knn)
print(accuracy)

for i in range(len(x)):
    if z[i] == 0:
        plt.scatter(x[i][0], x[i][1], color='red', s=40, marker='o')
    else:
        plt.scatter(x[i][0], x[i][1], color='blue', s=40, marker='o')        


plt.show()
