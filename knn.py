import matplotlib.pyplot as plt
import numpy as np
import math

x = [7, 1, 3, 1, 0, 3, 8, 4, 5, 8, 2, 3, 3, 4]
y = [1, 0, 2, 5, 3, 2, 2, 7, 9, 3, 0, 2, 4, 1]
z = [1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1]
point = [3, 3]

k = 3
a = []
for i in range(len(x)):
    distance = math.sqrt((point[0] - x[i])**2 + (point[1] - y[i])**2)
    a.append([distance, z[i]])
for i in range(len(x)):
    a = sorted(a, key=lambda c: c[0])
i = 0
j = 0
l = 0
while(i < k ) and (j < k):
    if(a[l][1] == 0): i=i+1
    else:  j = j+1
    l = l+1
if(i == k): print('red')
else: print('blue')


for i in range(len(x)):
    if z[i] == 0:
        plt.scatter(x[i], y[i], color='red', s=40, marker='o')
    else:
        plt.scatter(x[i], y[i], color='blue', s=40, marker='o')        
plt.scatter(point[0], point[1], color='green', s=30, marker='o')        

t = np.arange(min(x)-1,max(x)+1,0.1)
plt.show()