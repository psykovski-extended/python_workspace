import matplotlib.pyplot as plt
import numpy as np

# Messwerte für Rechtlauf
Ur = [10.02, 20.1, 30.2, 40.29, 50.4, 59.8, 70.3, 80, 89.9, 99.8, 110.87, 119.9, 129.9, 140.7, 150]
nr = [88.16, 184.9, 282, 381.4, 481.5, 574.6, 677.6, 772.8, 870.6, 968.9, 1076, 1167, 1266, 1373, 1465]

# Messwerte für Linkslauf
Ul = [10.15, 20.17, 30.05, 40.2, 50.4, 60.3, 70.7, 80.5, 90.3, 100, 110, 120.8, 130.6, 140.7, 150]
nl = [86.18, 182.7, 281.9, 382.6, 485.8, 583.7, 685.9, 784.8, 879.3, 979.2, 1078, 1184, 1283, 1383, 1470]

# Messwerte für Testlauf bei 50V
Itl = [0.35, 0.3, 0.25, 0.22, 0.2, 0.15]
ntl = [482.3, 512.13, 557.7, 598.5, 652, 785.7]

# Graphische Darstellung der Messwerte
fig = plt.figure(1, figsize=(10, 6))

ax = fig.add_subplot(1, 1, 1)
ax.plot(nr[-5:], Ur[-5:], '-r', label='Rechtslauf')
ax.plot(nl[-5:], Ul[-5:], '-b', label='Linkslauf')
ax.set_ylabel('[U] in V')
ax.set_xlabel('[n] in rpm')
# ax.set_title('Spannungs- und Drehzahlkennlinie bei\nRechts- und Linkslauf, letzten fünf Messwerte')
ax.grid(True)

ax.legend()
fig = plt.figure(2, figsize=(10, 6))
ax = fig.add_subplot(1, 1, 1)
ax.plot(nr, Ur, '-r', label='Rechtslauf')
ax.plot(nl, Ul, '-b', label='Linkslauf')
ax.set_ylabel('[U] in V')
ax.set_xlabel('[n] in rpm')
# ax.set_title('Spannungs- und Drehzahlkennlinie bei Rechts- und Linkslauf')
ax.grid(True)

ax.legend()

# Interpolation mittels Polynom 2.Grades
z = np.polyfit(np.array(ntl), np.array(Itl), 2)
f = np.poly1d(z)

n_new = np.linspace(ntl[0], ntl[-1], 1000)
I_new = f(n_new)
fig = plt.figure(3, figsize=(10, 6))
ax = fig.add_subplot(1, 1, 1)
ax.plot(ntl, Itl, '-o', label='Messwerte')
ax.plot(n_new, I_new, '--r', label='Interpolierte Kurve')
ax.set_ylabel('[I] in A')
ax.set_xlabel('[n] in rpm')
# ax.set_title('Testlauf bei 50V')
ax.grid(True)

ax.legend()


plt.show()
