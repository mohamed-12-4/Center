
import numpy as np

def linear(w: int, b: int, x: int) -> int:
    m = x.shape[0]
    fw_b = np.zeros(m)
    for i in range(m):
        fw_b[i] = w*x[i] + b

    return fw_b

x_train = np.array([1.0, 2.0])
y_train = np.array([300.0, 500.0])

print(linear(100, 100, x_train))

