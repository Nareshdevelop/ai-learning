import numpy as np

pairs = [
    (np.array([2, 1]), np.array([ 1,  2])),   # 1  4
    (np.array([2, 1]), np.array([-1,  2])),   # 2  <- look familiar?  0
    (np.array([2, 1]), np.array([-2, -1])),   # 3  -5 
    (np.array([1, 0]), np.array([ 0,  1])),   # 4  <- the basis vectors î, ĵ  0
    (np.array([3, 4]), np.array([ 3,  4])),   # 5  <- a vector with itself 25
]

for v, w in pairs:
    print(v, "·", w, "=", np.dot(v, w))

    v = np.array([3, 4])
print(np.dot(v, v))               # 25
print(np.linalg.norm(v)**2)       # 25  -> same!
def angle_deg(v, w):
    cos_t = np.dot(v, w) / (np.linalg.norm(v) * np.linalg.norm(w))
    return np.degrees(np.arccos(cos_t))
for v, w in pairs:
    print(v, "·", w, "=", angle_deg(v, w))



