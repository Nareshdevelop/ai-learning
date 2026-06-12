import numpy as np

def f(x):
    return x          # the line y = x

# area under y=x from 0 to 1 is a TRIANGLE

for N in [1, 10, 100, 1000, 100000]:
    dx = 1 / N                                   # width of each thin slice
    xs = np.linspace(0, 1, N, endpoint=False)    # left edge of each slice
    area = np.sum(f(xs) * dx)                     # add up (height * width) for all slices
    print(f"N={N:6d}:  area ≈ {area}")
def g(x):
    return np.sqrt(1 - x**2)     # top edge of a unit circle (radius 1)

N = 1000000
dx = 1 / N
xs = np.linspace(0, 1, N, endpoint=False)
quarter = np.sum(g(xs) * dx)     # area under it = a QUARTER of the circle = pi/4
print("pi ≈", 4 * quarter)        # so 4x the quarter-area ≈ pi

