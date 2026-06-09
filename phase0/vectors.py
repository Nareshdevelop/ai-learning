import numpy as np
import matplotlib.pyplot as plt
v = np.array([1,2])
w = np.array([1,3])
print(v + w)
print(v + w)
print(2*v)
print(-1*w)
print(np.linalg.norm(v))


v = np.array([2,1])
w = np.array([1,3])
s = v + w
plt.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color='r')
plt.quiver(0, 0, w[0], w[1], angles='xy', scale_units='xy', scale=1, color='b')
plt.quiver(0, 0, s[0], s[1] , angles='xy', scale_units='xy', scale=1, color='g')
plt.xlim(-5, 5); plt.ylim(-5, 5); plt.grid(); plt.gca().set_aspect('equal')
plt.show()