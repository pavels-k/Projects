from sympy import symbols, diff, solve
import matplotlib.pyplot as plt
import numpy as np

x = [7, 1, -3, -1, 0, 8, 4]
y = [-1, 0, 2, 5, 4, 8, 11]


n = int(input("Введети степень полинома "))
teta = []
for i in range(n+1):
        teta.append(symbols(chr(65+i).lower()))

poly = 0
t = symbols('t')
for i in range(n+1):
        poly = poly + teta[i]*t**i

F = []
for z in y: 
        F.append(poly.subs(t,z))

sum = 0
for i in range(len(x)):
        sum += (x[i]-F[i])**2

dx = []
for i in range(n+1):
        dx.append(diff(sum, (chr(65+i).lower())))

sol = solve(dx)

answers = []
for i in range(n+1):
        answers.append(sol.get(symbols(chr(65+i).lower())))

plt.scatter(x, y, color='red', s=40, marker='o')

tt = np.arange(min(x)-1,max(x)+1,0.1)
z = 0
for i in range(n+1):
        z = z + answers[i]*tt**i
plt.plot(tt, z)
plt.show()