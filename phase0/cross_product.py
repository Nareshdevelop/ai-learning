import numpy as np
pairs = [
    (np.array([2, 0]), np.array([0, 3])),   # 1  clean 2×3 rectangle 
    (np.array([2, 1]), np.array([1, 2])),   # 2 3
    (np.array([1, 2]), np.array([2, 1])),   # -3  <- pair 2 with the order SWAPPED  0
    (np.array([1, 2]), np.array([2, 4])),   # 0  <- parallel ([2,4]=2·[1,2]) -
]

for v, w in pairs:
    print(v, "x", w, "=", np.cross(v, w))

    v, w = np.array([2,1]), np.array([1,2])
print(np.cross(v, w))                              # 3
print(np.linalg.det(np.column_stack([v, w])))      # 3  -> same number


v, w = np.array([2,1]), np.array([1,2])
d = np.dot(v, w)        # 4
c = v[0]*w[1] - v[1]*w[0]    # the cross product, by hand — no np.cross, no warning

print("dot:", d, "cross:", c)
print("dot² + cross² =", d**2 + c**2)              # 25
print("(|v||w|)²     =", (np.linalg.norm(v)*np.linalg.norm(w))**2)   # 25
