import numpy as np
import matplotlib.pyplot as plt


a = np.array([[0, -1], [1, 0]])
b = np.array([[1,  1], [0, 1]]) 
v = np.array([2, 1])

transform1 = b @ v

transform2 = a @ transform1 
print("step by step:", transform1)
print("step by step:", transform2)

print("A @ B @ v :", (a @ b) @ v)    # shear, then rotate
print("B @ A @ v :", (b @ a) @ v)    # rotate, then shear