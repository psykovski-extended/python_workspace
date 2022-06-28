import matplotlib.pyplot as plt
import numpy as np
import math

Lideal = 10e-3
Cideal = 2e-6
U = 10
f = 1000
I = 50e-3

omega0ideal = math.sqrt(1 / (Lideal * Cideal))  # Resonanzkreisfrequenz, ideal
f0ideal = omega0ideal / (2 * math.pi)
R = U / I
Pr = 2  # Leistung an Widerstand

Re = 220  # gewählter Widerstand

# UR = 16.5 / 2
# UL = 17.5 / 2 - UR
UR = 6.79
UL = 1.97
I = UR / Re
XL = UL / I

L = XL / (2 * math.pi * f)
# L = 0.01
# XL = 2 * math.pi * f * L
Ce = 1.93e-6

Xc = - 1 / (2 * math.pi * f * Ce)

X = XL - Xc

omegaR = math.sqrt(1 / (L * Ce))

fR = omegaR / (2 * math.pi)
R3 = 1 / (1 / Re + 1 / Re + 1 / Re)

omegaI1 = omegaR * (math.sqrt(math.pow(Re / 2 * math.sqrt(Ce / L), 2) + 1) - Re / 2 * math.sqrt(Ce / L))
omegaII1 = omegaR * (math.sqrt(math.pow(Re / 2 * math.sqrt(Ce / L), 2) + 1) + Re / 2 * math.sqrt(Ce / L))

omegaI2 = omegaR * (math.sqrt(math.pow(R3 / 2 * math.sqrt(Ce / L), 2) + 1) - R3 / 2 * math.sqrt(Ce / L))
omegaII2 = omegaR * (math.sqrt(math.pow(R3 / 2 * math.sqrt(Ce / L), 2) + 1) + R3 / 2 * math.sqrt(Ce / L))

B1 = omegaII1 - omegaI1
B2 = omegaII2 - omegaI1

Q1 = omegaR / B1
Q2 = omegaR / B2

# Messung bei R = 220 Ohm
Um = [10.6, 10.1, 9.6, 9.2, 9.2, 9, 8.8, 8.8, 8.7, 8.7, 8.7, 8.7, 8.7, 8.7, 8.6, 8.6, 8.7, 8.8, 8.8, 8.8, 8.8, 8.9, 9,
      9, 9, 9.2, 9.3, 9.5, 9.95, 10.3, 10.5]
Umr = [2.9, 4.9, 6.2, 7.05, 7.6, 8, 8.2, 8.4, 8.5, 8.5, 8.5, 8.6, 8.6, 8.5, 8.5, 8.5, 8.4, 8.4, 8.3, 8.2, 8.2, 8.1,
       8.05, 7.9, 7.7, 7.6, 7.2, 6.9, 5.8, 4.6, 3.7]
Im = [4.27, 7.54, 9.68, 11.03, 11.845, 12.36, 12.69, 12.9, 13.03, 13.1, 13.12, 13.13, 13.11, 13.07, 13.04, 12.97, 12.88,
      12.795, 12.705, 12.61, 12.5, 12.39, 12.16, 11.915, 11.66, 11.4, 10.74, 10.08, 7.94, 6.015, 4.08]
fm = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000,
      2100, 2200, 2400, 2600, 2800, 3000, 3500, 4000, 5800, 7900, 11000]

# Messung bei R = 220/3
Um2 = [10.7, 10.5, 10.2, 9.4, 8.8, 8.3, 7.7, 7.2, 6.8, 6.45, 6.4, 6.35, 6.3, 6.3, 6.3, 6.3, 6.3, 6.35, 6.4, 6.6, 6.8,
       6.95, 7.2, 7.35, 7.6, 7.9, 8.4, 8.6, 8.8, 9.1, 9.7, 10.1, 10.4, 10.6]
Umr2 = [1.01, 1.91, 2.75, 3.5, 4.15, 4.7, 5.15, 5.45, 5.7, 5.8, 5.9, 5.9, 5.9, 5.9, 5.9, 5.9, 5.9, 5.9, 5.85, 5.75, 5.6,
        5.5, 5.45, 5.25, 5.15, 4.9, 4.65, 4.4, 4.25, 3.95, 3.2, 2.8, 2, 1.4]
Im2 = [4.455, 8.72, 12.665, 16.22, 19.25, 21.735, 23.75, 25.25, 26.28, 26.94, 27.12, 27.265, 27.34, 27.31, 27.335,
       27.31, 27.25, 27.175, 26.895, 26.49, 26.01, 25.465, 24.85, 24.26, 23.65, 22.42, 21.24, 20.1, 19.04, 18.05, 14.07,
       12.04, 8.11, 4.37]
fm2 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1050, 1100, 1110, 1125.4, 1140, 1200, 1250, 1300, 1400, 1500,
       1600, 1700, 1800, 1900, 2000, 2200, 2400, 2600, 2800, 3000, 4000, 4700, 6800, 11000]

Im = np.array(Im)
Im2 = np.array(Im2)

plt.figure(1, figsize=(12, 6))
plt.style.use('fast')
plt.plot(fm, Im, label='R1')
plt.plot(fm2, Im2, label='R2')
plt.grid(True)
plt.ylabel('[I] in mA', size=20)
plt.xlabel('[f] in Hz', size=20)
plt.xticks(size=20)
plt.yticks(size=20)
plt.legend(prop={'size': 18})
plt.xscale('log')


def movmean(arr, num=2):
    narr = []
    for i in range(len(arr)):
        if i + num < len(arr):
            narr.append(np.sum(arr[i:i + num]) / num)
        else:
            narr.append(arr[i])
    return narr


U = [Um[i] for i in range(4, len(Um)-4)]
U_new = movmean(U, 4)
U = np.array(Um)
U[np.arange(4, len(Um)-4)] = U_new

plt.figure(2, figsize=(12, 6))
plt.style.use('fast')
plt.plot(fm, Um, label='R1')
plt.plot(fm, U, '--g', label='R1, geglättet')
plt.plot(fm2, Um2, label='R2')

plt.grid(True)
plt.ylabel('[U] in V', size=20)
plt.xlabel('[f] in Hz', size=20)
plt.xticks(size=20)
plt.yticks(size=20)
plt.legend(prop={'size': 18})
plt.xscale('log')

# with open('data.csv', 'w') as data:
#     data.write('U;UR;I;f\n')
#     for i in range(len(Um)):
#        data.write(str(Um[i]) + ';' + str(Umr[i]) + ';' + str(Im[i]) + ';' + str(fm[i]) + '\n')
#
# with open('data.csv', 'a') as data:
#     data.write('\n\n\n')
#     data.write('U2;UR2;I2;f2\n')
#     for i in range(len(Um2)):
#         data.write(str(Um2[i]) + ';' + str(Umr2[i]) + ';' + str(Im2[i]) + ';' + str(fm2[i]) + '\n')
