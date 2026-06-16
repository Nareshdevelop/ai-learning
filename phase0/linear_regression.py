import numpy as np

# 1. THE DATA — the machine sees only these numbers, not the rule behind them
x = np.array([1.0, 2.0, 3.0, 4.0])
y = np.array([2.0, 4.0, 6.0, 8.0])     # hidden pattern: y = 2x  (machine must find this)


# 2. THE KNOBS — start at 0 (a flat, useless line)
w = 0.0
b = 0.0
lr = 0.01                 # learning rate (step size)
n = len(x)

# 3. TRAINING LOOP — gradient descent on the loss
for step in range(1000):
    pred  = w * x + b
    error = pred - y
    loss  = np.mean(error**2)
    grad_w = (2/n) * np.sum(error * x)
    grad_b = (2/n) * np.sum(error)
    w = w - lr * grad_w
    b = b - lr * grad_b
    if step % 100 == 0:
        print(f"step {step:4d}:  loss={loss:8.4f}   w={w:.3f}   b={b:.3f}")

# v---  OUTSIDE the loop: flush-left (no indent), runs ONCE at the end  ---v
print(f"\nLearned:  w={w:.3f},  b={b:.3f}")
print(f"Model says: {np.round(w*x + b, 2)}")
print(f"Truth:      {y}")