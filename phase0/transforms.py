import numpy as np
import matplotlib.pyplot as plt

new_i = np.array([1, 0])
new_j = np.array([1, 1]) 

m = np.column_stack([new_i,new_j])
print(m)
v = np.array([0, 2]) 
moved = m @ v

print("before : " , v)
print("after :" , moved)

plt.quiver(0,0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color='r')
plt.quiver(0,0, moved[0], moved[1], angles='xy', scale_units='xy', scale=1, color='g')
plt.xlim(-5, 5); plt.ylim(-5, 5); plt.grid(); plt.gca().set_aspect('equal')
plt.show()