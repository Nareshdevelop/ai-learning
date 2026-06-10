import numpy as np

stretch  = np.array([[2, 0], [0, 2]])   # predict det? meaning?
rotation = np.array([[0, -1],[1, 0]])   # predict det? meaning?
shear    = np.array([[1, 1], [0, 1]])   # predict det? meaning?   <- the surprising one
collapse = np.array([[1, 2], [2, 4]])   # predict det? meaning?   <- columns [1,2] and [2,4]=2·[1,2]

for name, M in [("stretch",stretch),("rotation",rotation),("shear",shear),("collapse",collapse)]:
    print(name, "-> det =", np.linalg.det(M))