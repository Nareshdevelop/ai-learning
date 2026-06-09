import numpy as np
import matplotlib.pyplot as plt

i = np.array([1,0])
j = np.array([0,1])
v = np.array([1,2])
w = np.array([2,4])
print(3*i + 4*j)

def lin_comb(a,b) : return a*v + b*w
xs,ys = [],[]
linespace = np.linspace(-5, 5, 21)


for a in linespace:
    for b in linespace:
        p = lin_comb(a, b)
        xs.append(p[0])
        ys.append(p[1])
plt.scatter(xs, ys)
plt.grid()
plt.gca().set_aspect('equal')
plt.show()
