import numpy as np

def f(x):
    return np.exp(x)          # e^x

def numerical_derivative(f, x, h=1e-6):
    return (f(x + h) - f(x)) / h

for x in [0, 1, 2, 3]:
    slope = numerical_derivative(f, x)
    print(f"x={x}:  slope ≈ {slope:.5f}   e^x = {np.exp(x):.5f}")
