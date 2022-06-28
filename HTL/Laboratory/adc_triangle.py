import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

analogue = pd.read_csv("D:\\HTL\\Labor\\4AHET\\OPV_Dreieck\\data\\analog_export.DAT")
fourier = pd.read_csv("D:\\HTL\\Labor\\4AHET\\OPV_Dreieck\\data\\fourier_export.DAT")

t = np.array(analogue[analogue.keys()[0]]) * 1000
u = np.array(analogue[analogue.keys()[1]])

x = fourier[fourier.keys()[0]]
y = fourier[fourier.keys()[1]]

plt.plot(x, y)
plt.grid()
plt.ylabel("$U_A$ in V")
plt.xlabel("f in Hz")
plt.tight_layout()
plt.show()

plt.plot(t, u)
plt.grid()
plt.ylabel("$U_A$ in V")
plt.xlabel("t in ms")
plt.tight_layout()
plt.show()

