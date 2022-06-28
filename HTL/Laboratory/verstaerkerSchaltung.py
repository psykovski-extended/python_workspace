import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from HTL.util.inductor import movmean, getPeriod

path = "C:\\Users\\Dominik Lovetinsky\\HTBLuVA St. Pölten\\c.freudenthaler@htlstp.at - 4AHET\\" \
       "12_Verstaerkerschaltungen\\data\\"

data18_n_inv = pd.read_csv(path + "Philipp_Dominik\\scope_18.csv")
data19_inv = pd.read_csv(path + "Philipp_Dominik\\scope_19.csv")

data0_n_inv = pd.read_csv(path + "Clemens_Tobias\\Nichtinvertierend_Clemens-Tobias.csv")
data1_inv = pd.read_csv(path + "Clemens_Tobias\\Invertierend_Clemens-Tobias.csv")

# mapping time lines
t1 = np.array(data18_n_inv[data18_n_inv.keys()[0]]) * 1e+3
t2 = np.array(data19_inv[data19_inv.keys()[0]]) * 1e+3
t3 = np.array(data0_n_inv[data0_n_inv.keys()[0]]) * 1e+3
t4 = np.array(data1_inv[data1_inv.keys()[0]]) * 1e+3

# mapping voltage
u11 = movmean(data18_n_inv[data18_n_inv.keys()[1]], 30)
u21 = movmean(data19_inv[data19_inv.keys()[1]], 30)
u31 = movmean(data0_n_inv[data0_n_inv.keys()[1]], 30)
u41 = movmean(data1_inv[data1_inv.keys()[1]], 30)

u12 = movmean(data18_n_inv[data18_n_inv.keys()[2]], 30)
u22 = movmean(data19_inv[data19_inv.keys()[2]], 30)
u32 = movmean(data0_n_inv[data0_n_inv.keys()[2]], 30)
u42 = movmean(data1_inv[data1_inv.keys()[2]], 30)

# scope 18
plt.figure(1)
plt.plot(t1, u11, label="Eingangsspannung")
plt.plot(t1, u12, label="Ausgangsspannung")
plt.xlabel("[t] ms")
plt.ylabel('[U] V')
plt.xlim((t1[0], t1[-1]))
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# scope 19
plt.figure(2)
plt.plot(t2, u21, label="Eingangsspannung")
plt.plot(t2, u22, label="Ausgangsspannung")
plt.xlabel("[t] ms")
plt.ylabel('[U] V')
plt.xlim((t2[0], t2[-1]))
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# scope 0
plt.figure(3)
plt.plot(t3, u31, label="Eingangsspannung")
plt.plot(t3, u32, label="Ausgangsspannung")
plt.xlabel("[t] ms")
plt.ylabel('[U] V')
plt.xlim((t3[0], t3[-1]))
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# scope 1
plt.figure(4)
plt.plot(t4, u41, label="Eingangsspannung")
plt.plot(t4, u42, label="Ausgangsspannung")
plt.xlabel("[t] ms")
plt.ylabel('[U] V')
plt.xlim((t4[0], t4[-1]))
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

e1, e2, n, m = getPeriod(data0_n_inv[data0_n_inv.keys()[1]], data0_n_inv[data0_n_inv.keys()[2]])

f = [1/(data0_n_inv[data0_n_inv.keys()[0]][e2] - data0_n_inv[data0_n_inv.keys()[0]][e1])]
v = [(max(data0_n_inv[data0_n_inv.keys()[2]]) / max(data0_n_inv[data0_n_inv.keys()[1]])) * (-1)]

for i in range(2, 7):
    dat = pd.read_csv(path + "Clemens_Tobias\\scope" + "_" + str(i) + ".csv")
    i1, i2, j1, j2 = getPeriod(dat[dat.keys()[1]], dat[dat.keys()[2]])
    f.append(1/(dat[dat.keys()[0]][i2] - dat[dat.keys()[0]][i1]))
    v.append((max(dat[dat.keys()[2]]) / max(dat[dat.keys()[1]])) * (-1))

p = np.polyfit(np.array(f), np.array(v), 6)
fn = np.linspace(f[0], f[-2], 1000)
func = np.poly1d(p)

vn = func(fn)

plt.figure(5)
plt.plot(fn, vn, label="Interpolierte Kurve")
plt.scatter(f, v, color="#FF4500", label="Messpunkte")
plt.xscale('log')
plt.xlabel('[f] Hz')
plt.ylabel('[vu] 1')
plt.legend()
plt.tight_layout()
plt.show()

# Inverstierender Verstärker - Simulation ================================================================
data_sim_id_ni = pd.read_csv(path + "InvVer_ideal.DAT")
ti_inv = data_sim_id_ni[data_sim_id_ni.keys()[0]]
xi1_inv = data_sim_id_ni[data_sim_id_ni.keys()[1]]
xi2_inv = data_sim_id_ni[data_sim_id_ni.keys()[2]]

data_sim_5_ni = pd.read_csv(path + "InvVer_0-5Vver.DAT")
t_inv = data_sim_5_ni[data_sim_5_ni.keys()[0]]
x1_inv = data_sim_5_ni[data_sim_5_ni.keys()[1]]
x2_inv = data_sim_5_ni[data_sim_5_ni.keys()[2]]

plt.figure(6)
plt.plot(ti_inv, xi2_inv, color="#5d6475", label="Ideale Verstärkung")
plt.plot(t_inv, x1_inv, label="Eingangsspannung")
plt.plot(t_inv, x2_inv, label="Verstärkung bei 0.5V Offset")
plt.legend()
plt.xlabel('[t] s')
plt.ylabel('[U] V')
plt.grid(True)
plt.tight_layout()
plt.show()

# Nichtinvertierender Verstärker - Simulation ================================================================
data_sim_id_ni = pd.read_csv(path + "NichtInvVer_ideal.DAT")
ti_ninv = data_sim_id_ni[data_sim_id_ni.keys()[0]]
xi1_ninv = data_sim_id_ni[data_sim_id_ni.keys()[1]]
xi2_ninv = data_sim_id_ni[data_sim_id_ni.keys()[2]]

data_sim_5_ni = pd.read_csv(path + "NichtInvVer_0-5Vver.DAT")
t_ninv = data_sim_5_ni[data_sim_5_ni.keys()[0]]
x1_ninv = data_sim_5_ni[data_sim_5_ni.keys()[1]]
x2_ninv = data_sim_5_ni[data_sim_5_ni.keys()[2]]

plt.figure(7)
plt.plot(ti_ninv, xi2_ninv, color="#5d6475", label="Ideale Verstärkung")
plt.plot(t_ninv, x1_ninv, label="Eingangsspannung")
plt.plot(t_ninv, x2_ninv, label="Verstärkung bei 0.5V Offset")
plt.legend()
plt.xlabel('[t] s')
plt.ylabel('[U] V')
plt.grid(True)
plt.tight_layout()
plt.show()
