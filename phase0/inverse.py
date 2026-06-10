import numpy as np

# inverse = np.eye(2)

# print(inverse)

A = np.array([[1, 1], [0, 1]]) 

A_inv  = np.linalg.inv(A)

print("A_inv =\n", A_inv)

print (A @ A_inv)

v     = np.array([2, 1])

moved = A @ v

back = A_inv @ moved

print("v:", v, "| moved:", moved, "| back:", back)

collapse = np.array([[1, 2], [2, 4]])   # det = 0

try : 
    np.linalg.inv(collapse)
except  np.linalg.LinAlgError  as e : 
 print("No inverse! numpy says:", e)
