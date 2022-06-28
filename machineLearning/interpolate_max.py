import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate

A = np.zeros([1000, 2])
A[:, 0] = np.linspace(0, 1, 1000)
A[:, 1] = np.sin(A[:, 0]*4*np.pi)**2

px = A[[0, 99, 199, 299, 399, 499, 599, 699, 799, 899, 999], 0]
py = A[[0, 99, 199, 299, 399, 499, 599, 699, 799, 899, 999], 1]

p10 = interpolate.lagrange(px, py)
x_new = A[:, 0]
y_new = p10(x_new)

plt.plot(A[:, 0], A[:, 1], color='k', label='sin²(4*pi*x)')
plt.plot(x_new, y_new, color='r', linestyle='--', label='P10')
plt.scatter(px, py, color='b')

plt.legend()
plt.show()
