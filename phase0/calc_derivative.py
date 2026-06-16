import numpy as np

def f(x):
    return x**2

def numerical_derivative(f, x, h):
    return (f(x + h) - f(x)) / h          # rise over run

x = 3.0
for h in [1, 0.1, 0.01, 0.001, 0.0001, 0.00001, 0.000001] :
    print(f"h={h:<8}: slope ≈ {numerical_derivative(f, x, h)}")

print("exact (2x):", 2 * x)
