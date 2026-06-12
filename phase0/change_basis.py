import numpy as np
A = np.array([[1, -1], [1, 1]])
her = np.array([2, 0])          # she says her vector is [2, 0]
print("our coords:", A @ her)   # predict first!  what's 2·b1 + 0·b2 ?


ours = np.array([2, 0])         # in standard coords
A_inv = np.linalg.inv(A)
print("her coords:", A_inv @ ours)   # predict: what combo of b1,b2 makes [2,0]?


ours = np.array([2, 0])         # in standard coords
A_inv = np.linalg.inv(A)
print("her coords:", A_inv @ ours)   # predict: what combo of b1,b2 makes [2,0]?
