import numpy as np


M = np.array([[2, 1], [1, 2]])

v1 = np.array([1,  1])
v2 = np.array([1, -1])

eigenvalues, eigenvectors = np.linalg.eig(M)
print("eigenvalues:", eigenvalues)
print("eigenvectors (as columns):\n", eigenvectors)
