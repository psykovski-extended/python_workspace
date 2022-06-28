import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate

A = np.zeros([22, 2])
A[:, 0] = np.arange(0, 43, 2)
A[0:11, 1] = [2, 6, 9, 12, 14, 16, 17.5, 18.5, 20, 20.5, 21.5]
A[11:22, 1] = [22, 22.5, 22.7, 23.5, 23.5, 23.7, 24, 24, 24.2, 24.2, 24.5]
print(A[:])
plt.plot(A[:, 0], A[:, 1], 'o', color='k', label='Messwerte')
plt.xlabel('time [s]')
plt.ylabel('Voltage [V]')

p2 = interpolate.lagrange(A[[0, 10, 21], 0], A[[0, 10, 21], 1])
x_new = np.arange(-2, 50, 2)
y_new = p2(x_new)

error = ((p2(A[:, 0]) - A[:, 1])**2).sum_()
print('P2 => Quadratische Fehler: %.4e; gemittelt: %.4e' % (error, error/22))
plt.plot(x_new, y_new, label='Polynome Ordnung 2', color='black')

p5 = interpolate.lagrange(A[0:22:4, 0], A[0:22:4, 1])
x_new = np.arange(-2, 50, 2)
y_new = p5(x_new)

error = ((p5(A[:, 0]) - A[:, 1])**2).sum_()
print('P5 => Quadratische Fehler: %.4e; gemittelt: %.4e' % (error, error/22))
plt.plot(x_new, y_new, label='Polynome Ordnung 5', linestyle='--', color='red')

plt.legend(loc='lower right')
plt.show()
