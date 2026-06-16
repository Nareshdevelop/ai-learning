import numpy as np

def f(x):
    return (3*x + 1)**2

def numerical_derivative(f, x, h=1e-6):
    return (f(x + h) - f(x)) / h

x = 2.0
print("numerical   :", numerical_derivative(f, x))
print("chain rule  :", 6*(3*x + 1))      # your hand answer