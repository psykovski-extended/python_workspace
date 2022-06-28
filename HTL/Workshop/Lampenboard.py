import numpy as np
import matplotlib.pyplot as plt

P0 = 3.8

"""Lampenboard - 3.Uebung"""

"""Strom-Spannungsmessung"""

U = np.array([235.6, 235.6, 235.5, 235.8, 235.7, 236, 236, 236, 235.6, 235.9, 235.7, 235.1])
I = np.array([15.1, 259.9, 27.1, 146.5, 110.1, 69, 35.2, 46.6, 57.2, 24.1, 70.5, 160.5])
Pm = np.array([5.5, 60.8, 6.6, 26.1, 27.9, 13.5, 8.5, 9, 11.5, 6.8, 12.9, 38.5])
Pr = U * (I / 1000)
Pr2 = Pm - P0
width = 0.4

plt.figure(1)

ticks = np.arange(len(Pr)) + 1
plt.bar(ticks - width, Pr, width=width, label='Berechnet')
plt.bar(ticks, Pr2, width=width, label='Gemessen')
plt.ylabel('Leistung in W', size=15)
plt.xlabel('Lampe', size=15)
plt.legend(loc='upper right', fontsize=15)
plt.xticks(size=15)
plt.yticks(size=15)
plt.show()

"""Temperatur"""

T1 = [27.5, 64.5, 32.8, 28.9, 70, 40.5, 29.3, 26.4, 31.6, 25.2, 25.4, 122, 41]  # externes Multimeter
T2 = [28.4, 0, 31.2, 28.9, 71, 35.1, 31.1, 27.8, 28.5, 27, 25.3, 73.2, 37.5]  # 0: Messfehler; internes Messgerät

plt.figure(2)

ticks = np.arange(len(T2)) + 1
plt.bar(ticks - width, T1[:len(T2)], width=width, label='Ext. Messung')
plt.bar(ticks, T2, width=width, label='Int. Messung')
plt.legend(loc='upper left', fontsize=15)
plt.xticks(size=15)
plt.yticks(size=15)
plt.ylabel('[T] °C', size=15)
plt.xlabel('Lampen', size=15)
plt.show()

"""Beleuchtungsstaerke"""

Evo1 = [27000, 11090, 20800, 5610, 3987, 5410, 166400, 5870, 9660, 8140, 8930, 87100]  # oben extern
Evo2 = [21012, 10782.6, 15206.4, 3540, 4078, 3340.8, 112803.8, 3985.6, 6266, 5898.2, 5552.5, 91054]  # oben intern

plt.figure(3)
ticks = np.arange(len(Evo1)) + 1
plt.bar(ticks - width, Evo1, width=width, label='Ext. Messung')
plt.bar(ticks, Evo2, width=width, label='Int. Messung')
plt.legend(loc='upper left', fontsize=15)
plt.xticks(size=15)
plt.yticks(size=15)
plt.ylabel('[Ev] lx', size=15)
plt.xlabel('Lampen', size=15)
plt.show()

Evs1 = [41, 9530, 880, 4009, 4890, 6290, 604, 5120, 684.8, 1923, 6450, 265]  # seite extern
Evs2 = [30, 6912.9, 858.3, 3156.4, 6036, 3985.9, 131.7, 3456, 696, 957, 3916.7, 121.6]  # seite intern

plt.figure(4)
ticks = np.arange(len(Evs1)) + 1
width = 0.4
plt.bar(ticks - width, Evs1, width=width, label='Ext. Messung')
plt.bar(ticks, Evs2, width=width, label='Int. Messung')
plt.legend(loc='upper right', fontsize=15)
plt.xticks(size=15)
plt.yticks(size=15)
plt.ylabel('[Ev] lx', size=15)
plt.xlabel('Lampen', size=15)
plt.show()


# with open('C:\\Users\\Dominik Lovetinsky\\Desktop\\data.csv', 'w') as to:
#    to.write('U;I;Pm;Pr;Pr2;T1;T2;Evo1;Evo2;Evs1;Evs2\n')
#    for i in range(len(U) - 1):
#        to.write(str(U[i]) + ';' + str(I[i]) + ';' + str(Pm[i]) + ';' + str(Pr[i]) + ';' + str(Pr2[i]) + ';' +
#                 str(T1[i]) + ';' + str(T2[i]) + ';' + str(Evo1[i]) + ';' + str(Evo2[i]) + ';' +
#                 str(Evs1[i]) + ';' + str(Evs2[i]) + '\n')
