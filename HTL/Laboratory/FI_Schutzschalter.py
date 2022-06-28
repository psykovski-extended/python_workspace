import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from HTL.util import inductor

path = "C:\\Users\\Dominik Lovetinsky\\HTBLuVA St. Pölten\\c.freudenthaler@htlstp.at - 4AHET" \
       "\\07_FI-Schutzschalter\\data\\csv\\"

# =====================================================================

data1 = pd.read_csv(path + "scope_4.csv")

time = np.array(data1[data1.keys()[0]]) - 0.000791353
U = inductor.movmean(np.array(data1[data1.keys()[1]]), 30)
I = inductor.movmean(np.array(data1[data1.keys()[2]]), 30)

fig, ax1 = plt.subplots()

color = 'tab:blue'
ax1.plot(time, U, color=color)  # Unicode subscript q suchen
ax1.tick_params(axis='y', labelcolor=color)
ax1.set_ylabel('[U] V', color=color)

ax2 = ax1.twinx()
color = 'tab:red'
ax2.plot(time, I, color=color)
ax2.tick_params(axis='y', labelcolor=color)
ax2.axvline(x=0, color='g', linestyle='--', label='I\u0394N überschritten')
ax2.set_ylabel('[I\u0394N] A', color=color)
ax2.axvline(x=0.0157, color='k', linestyle='--', label='FI ausgelöst nach 15.7ms')
ax2.axhline(y=-0.1, color='r', linestyle='--', label='I\u0394N')
ax2.axhline(y=0.1, color='r', linestyle='--')
ax1.set_xlabel(r'[t_{inv}] s')

ax2.legend(loc="upper left")

fig.tight_layout()
plt.show()

# =====================================================================

data1 = pd.read_csv(path + "scope_5.csv")
time = np.array(data1[data1.keys()[0]]) * 1e+3
U = inductor.movmean(np.array(data1[data1.keys()[1]]), 30)
Ur = inductor.movmean(np.array(data1[data1.keys()[2]]), 30)
I = inductor.movmean(np.array(data1[data1.keys()[3]]), 30)

fig, ax1 = plt.subplots()

color = 'tab:blue'
ax1.plot(time, U, color=color)  # Unicode subscript q suchen
ax1.tick_params(axis='y', labelcolor=color)
ax1.set_ylabel('[U] V', color=color)

ax1.set_xlabel('[t_inv] ms')

color = 'tab:red'
ax2 = ax1.twinx()
ax2.set_ylim(-0.25, 0.25)
ax2.set_ylabel('[I\u0394N] A', color=color)
ax2.plot(time, I, color=color)
ax2.tick_params(axis='y', labelcolor=color)
ax2.set_ylabel('[I\u0394N] A')
ax2.axvline(x=0, color='g', linestyle='--', label='I\u0394N überschritten')
ax2.axvline(x=4.41644, color='k', linestyle='--', label='FI ausgelöst nach 4.416ms')
ax2.axhline(y=-0.1, color='r', linestyle='--', label='I\u0394N')
ax2.axhline(y=0.1, color='r', linestyle='--')

ax2.legend(loc="upper left")

fig.tight_layout()
plt.show()

# ===================================================================== scope = 9

data1 = pd.read_csv(path + "scope_9.csv")
time = np.array(data1[data1.keys()[0]]) * 1e+3
U = inductor.movmean(np.array(data1[data1.keys()[1]]), 30)
I = inductor.movmean(np.array(data1[data1.keys()[3]]) * (-1), 30)

fig, ax1 = plt.subplots()

ax1.plot(time, U, color='tab:blue')

ax2 = ax1.twinx()
ax1.tick_params(axis='y', labelcolor='tab:blue')
ax1.set_ylabel('[U] V', color='tab:blue')

ax1.set_xlabel('[t_inv] ms')

ax2.plot(time, I, color='tab:red')
ax2.set_ylabel('[I\u0394N] A', color='tab:red')
ax2.plot(time, I, color=color)
ax2.tick_params(axis='y', labelcolor='tab:red')
ax2.set_ylabel('[I\u0394N] A')
ax2.axvline(x=0, color='g', linestyle='--', label='I\u0394N überschritten')
ax2.axvline(x=25, color='k', linestyle='--', label='FI ausgelöst nach 25ms')
ax2.axhline(y=-0.03, color='r', linestyle='--', label='I\u0394N')
ax2.axhline(y=0.03, color='r', linestyle='--')

ax2.legend(loc="upper left")

fig.tight_layout()
plt.show()

# ===================================================================== scope = 10

data1 = pd.read_csv(path + "scope_10.csv")
time = np.array(data1[data1.keys()[0]]) * 1e+3
U = inductor.movmean(np.array(data1[data1.keys()[1]]), 30)
I = inductor.movmean(np.array(data1[data1.keys()[3]]) * (-1), 30)

fig, ax1 = plt.subplots()

ax1.plot(time, U, color='tab:blue')

ax2 = ax1.twinx()
ax1.tick_params(axis='y', labelcolor='tab:blue')
ax1.set_ylabel('[U] V', color='tab:blue')

ax1.set_xlabel('[t_inv] ms')

ax2.plot(time, I, color='tab:red')
ax2.set_ylabel('[I\u0394N] A', color='tab:red')
ax2.plot(time, I, color=color)
ax2.tick_params(axis='y', labelcolor='tab:red')
ax2.set_ylabel('[I\u0394N] A')
ax2.axvline(x=0, color='g', linestyle='--', label='I\u0394N überschritten')
ax2.axvline(x=123.8, color='k', linestyle='--', label='FI ausgelöst nach 123.8ms')
ax2.axhline(y=-0.1, color='r', linestyle='--', label='I\u0394N')
ax2.axhline(y=0.1, color='r', linestyle='--')

ax2.legend(loc="upper left")

fig.tight_layout()
plt.show()

# ===================================================================== scope = 11

data1 = pd.read_csv(path + "scope_11.csv")
time = np.array(data1[data1.keys()[0]]) * 1e+3
U = inductor.movmean(np.array(data1[data1.keys()[1]]), 30)
I = inductor.movmean(np.array(data1[data1.keys()[3]]) * (-1), 30)

fig, ax1 = plt.subplots()

ax1.plot(time, U, color='tab:blue')

ax2 = ax1.twinx()
ax1.tick_params(axis='y', labelcolor='tab:blue')
ax1.set_ylabel('[U] V', color='tab:blue')

ax1.set_xlabel('[t_inv] ms')

ax2.plot(time, I, color='tab:red')
ax2.set_ylabel('[I\u0394N] A', color='tab:red')
ax2.plot(time, I, color=color)
ax2.tick_params(axis='y', labelcolor='tab:red')
ax2.set_ylabel('[I\u0394N] A')
ax2.axvline(x=0, color='g', linestyle='--', label='I\u0394N überschritten')
ax2.axvline(x=39.41, color='k', linestyle='--', label='FI ausgelöst nach 39.41ms')
ax2.axhline(y=-0.03, color='r', linestyle='--', label='I\u0394N')
ax2.axhline(y=0.03, color='r', linestyle='--')

ax2.legend(loc="upper left")

fig.tight_layout()
plt.show()

# ===================================================================== scope = 17

data1 = pd.read_csv(path + "scope_17.csv")
time = (np.array(data1[data1.keys()[0]]) * 1e+3) + 45
U = inductor.movmean(np.array(data1[data1.keys()[2]]), 30)
I = inductor.movmean(np.array(data1[data1.keys()[3]]), 30)

fig, ax1 = plt.subplots()

ax1.plot(time[700:-700], U[700:-700], color='tab:blue')
ax1.set_ylim(0, max(U) + 5)
ax2 = ax1.twinx()
ax1.tick_params(axis='y', labelcolor='tab:blue')
ax1.set_ylabel('[U] V', color='tab:blue')

ax1.set_xlabel('[t_inv] ms')

ax2.plot(time, I, color='tab:red')
ax2.set_ylim(0, 0.25)
ax2.set_ylabel('[I\u0394N] A', color='tab:red')
ax2.plot(time[700:-700], I[700:-700], color=color)
ax2.tick_params(axis='y', labelcolor='tab:red')
ax2.set_ylabel('[I\u0394N] A')
ax2.axvline(x=5.7, color='g', linestyle='--', label='I\u0394N überschritten')
ax2.axvline(x=40, color='k', linestyle='--', label='FI ausgelöst nach 34.3ms')
ax2.axhline(y=0.03, color='r', linestyle='--', label='I\u0394N')

ax2.legend(loc="upper left")

fig.tight_layout()
plt.show()

# ===================================================================== scope = 13

data1 = pd.read_csv(path + "scope_13.csv")
time = (np.array(data1[data1.keys()[0]]) * 1e+3) + 45
U = inductor.movmean(np.array(data1[data1.keys()[2]]), 30)
I = inductor.movmean(np.array(data1[data1.keys()[3]]), 30)

fig, ax1 = plt.subplots()

ax1.plot(time, U, color='tab:blue')

ax2 = ax1.twinx()
ax1.tick_params(axis='y', labelcolor='tab:blue')
ax1.set_ylabel('[U] V', color='tab:blue')
ax1.set_ylim(-15, 45)
ax1.set_xlabel('[t_inv] ms')

ax2.plot(time, I, color='tab:red')

ax2.set_ylabel('[I\u0394N] A', color='tab:red')
ax2.plot(time, I, color=color)
ax2.tick_params(axis='y', labelcolor='tab:red')
ax2.set_ylabel('[I\u0394N] A')
ax2.set_ylim(-0.08, 0.24)

fig.tight_layout()
plt.show()

# ===================================================================== scope = 14

data1 = pd.read_csv(path + "scope_14.csv")
time = (np.array(data1[data1.keys()[0]]) * 1e+3) + 45
U = inductor.movmean(np.array(data1[data1.keys()[2]]), 30)
I = inductor.movmean(np.array(data1[data1.keys()[3]]), 30)

fig, ax1 = plt.subplots()

ax1.plot(time, U, color='tab:blue')

ax2 = ax1.twinx()
ax1.tick_params(axis='y', labelcolor='tab:blue')
ax1.set_ylabel('[U] V', color='tab:blue')
ax1.set_ylim(-15, 45)
ax1.set_xlabel('[t_inv] ms')

ax2.plot(time, I, color='tab:red')

ax2.set_ylabel('[I\u0394N] A', color='tab:red')
ax2.plot(time, I, color=color)
ax2.tick_params(axis='y', labelcolor='tab:red')
ax2.set_ylabel('[I\u0394N] A')
ax2.set_ylim(-0.04, 0.12)

fig.tight_layout()
plt.show()

# =====================================================================  MAX VALUE reading

"""maxData = [6, 7, 8, 12, 13, 14, 16]
maxI = []
maxU = []

for i in maxData:
    data1 = pd.read_csv(path + "scope_" + str(i) + ".csv")
    U = inductor.movmean(np.array(data1[data1.keys()[1]]), 30)
    I = inductor.movmean(np.array(data1[data1.keys()[3]]), 30)
    maxI.append(max(I) if max(I) > abs(min(I)) else abs(min(I)))
    maxU.append(max(U))

with open(path + 'Idn.csv', 'w') as maxV:
    maxV.write('I;U;file\n')
    for i in range(len(maxI)):
        maxV.write(str(maxI[i]) + ';' + str(maxU[i]) + ';scope_' + str(maxData[i]) + '.csv\n')"""

# ===================================================================== done here: 4 5 6 7 8 9 10 11 12 13 14 (15?) 16


