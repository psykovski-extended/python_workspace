import numpy as np
import matplotlib.pyplot as plt

# Konstantstromquelle

PT100 = 100
vu = 20
vo = 250

Rvmax = PT100 + 0.4 * (vo - 0)
Rvmin = PT100 + 0.4 * (vu - 0)
Uz = 5.1

Ipt = 4 / Rvmax

R1 = Uz / Ipt
Rz1 = 8 / 0.005

# Gewählte Widerstandswerte
# OPV TL084
Rz1 = 2700
R1 = 560

# Unt = f(v)

Nt_temp = [23, 40, 60, 80, 100, 120, 140, 160, 180, 200, 210]
Nt_res = np.array([96.6, 46.6, 22.2, 11.64, 6.3, 3.6, 2.2, 1.38, 0.88, 0.582, 0.472])  # k
Nt_volt = [1.04, 1.066, 1.108, 1.156, 1.209, 1.265, 1.322, 1.38, 1.447, 1.52, 1.558]

t_new = np.linspace(-5, 200, 400)
f = np.polyfit(Nt_temp, Nt_volt, 1)
f = np.poly1d(f)
u_new = f(t_new)

fig = plt.figure()
ax = fig.add_subplot(111)

ax.scatter([20], [f(20)], color="purple")
ax.text(15, 0.97, r"N(20°C/{0:.1f}V)".format(f(20)))
ax.plot(t_new, u_new, label="Spannung: interpoliert")
ax.plot([100, 150], [f(100), f(100)], color="r")
ax.plot([150, 150], [f(100), f(150)], color="r")
ax.text(155, f(130), r'$k=${0:.3f}'.format((f(150) - f(100)) / (150 - 100)))
ax.scatter(Nt_temp, Nt_volt, color="orange", label="Spannung: Messwerte")

print(f(150), f(100))

ax.set_ylabel("$[U] V$")
ax.set_xlabel("$[\\vartheta] °C$")

ax.grid(True)  # fig. ?
axT = ax.twinx()
axT.scatter(Nt_temp, Nt_res, color="#77dd77", label="Widerstand: Messwerte")

f = np.polyfit(Nt_temp, Nt_res, 6)
f = np.poly1d(f)
res_new = f(t_new)

axT.plot(t_new, res_new, color="#48c072", label="Widerstand: interpoliert")
axT.set_ylabel("$[R] \\Omega$")

lines, labels = ax.get_legend_handles_labels()
lines2, labels2 = axT.get_legend_handles_labels()
axT.legend(lines + lines2, labels + labels2, loc="upper left")

fig.tight_layout()
plt.show()

#  ########################################## vollständige Schaltung

Nt_temp1 = [25, 40, 60]
Nt_volt1 = [-0.136, 2.447, 5.5]
Nt_res = [91.1, 48.6, 21.9]  # k

k = np.diff(Nt_volt1) / np.diff(Nt_temp1)
k = sum(k) / len(k)
d = Nt_volt1[0] - Nt_temp1[0] * k
u_new = k * np.array(t_new[:200]) + d

plt.scatter(Nt_temp1, Nt_volt1, label="Messwerte")

plt.plot([25, 200], [0, 10], color="#888888", label="ideale Kurve")
plt.plot(t_new[:200], u_new, label="reale Kurve", color="orange")
plt.grid(True)
plt.ylabel("$[U] V$")
plt.xlabel("$[\\vartheta] °C$")
plt.ylim([-0.5, 10.5])
plt.xlim([20, 210])
plt.legend(loc="best")

plt.show()
