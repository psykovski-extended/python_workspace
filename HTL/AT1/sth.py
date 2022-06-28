import numpy as np
import matplotlib.pyplot as plt

dt = 3e-6
u1 = 1000
u2 = 0

i1 = 0
i2 = 30

f = 2000

t = np.linspace(0, dt, 1000)

f1 = (u2 - u1) / dt * t + u1
f2 = (i2 - i1) / dt * t + i1

p = [f1[i] * f2[i] for i in range(len(t))]

plt.figure(0)

plt.plot(t, f1)
plt.plot(t, f2)
plt.plot(t, p)

E = sum(np.array(p) * dt/1000.0)
print(E)

