import numpy as np

def f(x, y):
    return x**2 + y**2

def partial_x(f, x, y, h=1e-6):
    return (f(x + h, y) - f(x, y)) / h     # nudge only x

def partial_y(f, x, y, h=1e-6):
    return (f(x, y + h) - f(x, y)) / h     # nudge only y

x, y = 3.0, 4.0
print("∂f/∂x ≈", partial_x(f, x, y))       # predict: 2x = ?
print("∂f/∂y ≈", partial_y(f, x, y))       # predict: 2y = ?


x, y = 3.0, 4.0           # start somewhere on the hill
lr = 0.1                   # step size ("learning rate")

for step in range(60):
    gx = partial_x(f, x, y)
    gy = partial_y(f, x, y)
    x = x - lr * gx        # step DOWNHILL (opposite the gradient)
    y = y - lr * gy

print(f"landed at: x={x:.4f}, y={y:.4f}")   # should be ≈ (0, 0) — the minimum!
