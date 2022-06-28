import matplotlib.pyplot as plt
import numpy as np

U = [2.01, 4.01, 6.01, 8.01, 10.01, 12.01, 14.01, 16.01, 18.01, 20.01, 22.01, 23.01, 24.01, 25.01, 26.01, 27, 28,
     29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]  # Spannungsquelle
Ur = [1.09, 3.079, 5.052, 7.02, 8.99, 10.93, 12.91, 14.88, 16.83, 18.77, 20.68, 21.63, 22.58, 23.53, 24.48, 25.44, 26.4,
      27.42, 28.4, 29.41, 30.45, 31.47, 32.53, 33.53, 34.53, 35.6, 36.64, 37.67, 38.72]  # Voltmeter
Ud = [0.9, 0.9001, 0.908, 0.922, 0.939, 0.948, 0.977, 0.994, 1.021, 1.07, 1.131, 1.177, 1.22, 1.259, 1.29, 1.33, 1.33001,
      1.32, 1.43, 1.33, 1.29, 1.24, 1.2, 1.17, 1.12, 1.1, 1.03, 1, 0.94]  # Diode Spannung
Irz = np.array([32, 70.4, 110, 150, 188, 232, 268, 312, 380, 388, 428, 456, 480, 496, 512, 536, 552, 576, 592, 616,
                632, 656, 672, 696, 720, 744, 760, 784, 800]) / 100  # Strommesszange, Strom in A
T = [20, 22.4, 23.7, 24.3, 27, 32.9, 82, 99.5, 133, 142, 151, 174, 191, 212, 216, 225, 245, 250, 252, 262,
     253, 211, 236, 234, 239, 231, 231, 212, 232]  # Termperatur

x = np.linspace(Ud[0], Ud[19], 300)
f = np.poly1d(np.polyfit(Ud[:18], T[:18], 6))

plt.figure(1)
plt.scatter(Ud[:18], T[:18], label='Zustand: intakt', color='#ffa500', marker='o', s=20)
plt.plot(Ud[17:], T[17:], label='Zustand: überlastet')
plt.plot(x, f(x), color='red')
plt.ylabel('[T] °C', size=15)
plt.xlabel('[Ud] V', size=15)
plt.legend(prop={'size': 15})

x = np.linspace(Irz[0], Irz[18], 300)
f = np.poly1d(np.polyfit(Irz[:18], T[:18], 6))

plt.figure(2)
plt.scatter(Irz[:18], T[:18], label='Zustand: intakt', color='#ffa500', marker='o', s=20)
plt.plot(Irz[17:], T[17:], label='Zustand: überlastet')
plt.plot(x, f(x), color='red')
plt.ylabel('[T] °C', size=15)
plt.xlabel('[Id] A', size=15)
plt.legend(prop={'size': 15})

# Glasdiode
U1 = [2, 4, 6, 6.5, 7, 7.5, 8, 8.5, 9]  # Spannungsquelle
Ur1 = [1.052, 2.789, 4.29, 4.737, 5.3, 5.815, 6.33, 6.89, 7.3]  # Voltmeter
Ud1 = [0.942, 1.193, 1.66, 1.709, 1.64, 1.632, 1.622, 1.54, 1.67]  # Diode Spannung
Irz1 = np.array([32.4, 68, 100, 108, 120, 128, 140, 152, 164]) / 100  # Strommesszange, Strom in A
T1 = [31, 52, 103, 136, 167, 178, 186, 194, 218]  # Termperatur

x = np.linspace(Ud1[0], Ud1[2], 30)
f = np.poly1d(np.polyfit(Ud1[:3], T1[:3], 3))

plt.figure(3)
plt.scatter(Ud1[:3], T1[:3], label='Zustand: intakt', color='#ffa500', marker='o', s=20)
plt.plot(Ud1[2:], T1[2:], label='Zustand: überlastet')
plt.plot(x, f(x), color='red')
plt.ylabel('[T] °C', size=15)
plt.xlabel('[Ud] V', size=15)
plt.legend(prop={'size': 15})

x = np.linspace(Irz1[0], Irz1[2], 30)
f = np.poly1d(np.polyfit(Irz1[:3], T1[:3], 3))

plt.figure(4)
plt.scatter(Irz1[:3], T1[:3], label='Zustand: intakt', color='#ffa500', marker='o', s=20)
plt.plot(Irz1[2:], T1[2:], label='Zustand: überlastet')
plt.plot(x, f(x), color='red')
plt.ylabel('[T] °C', size=15)
plt.xlabel('[Id] A', size=15)
plt.legend(prop={'size': 15})

R = 1e+3
# U = 2V pp bei 0.5V off

R1 = 5

Ir = np.array(U)/R1

plt.figure(5)
plt.plot(U, Ir, label='Strom über Spannungsmessung')
plt.plot(U, Irz, label='Strom über Strommesszange')
plt.ylabel('[I] A', size=15)
plt.xlabel('[U] V', size=15)
plt.legend(prop={'size': 15})

"""with open('C:\\Users\\Dominik Lovetinsky\\Desktop\\1N4007.csv', 'w') as export1:
    for i in range(len(U)):
        export1.write(str(U[i]) + ';' + str(Ur[i]) + ';' + str(Ud[i]) + ';' + str(Irz[i]) + ';' + str(T[i]) + '\n')

with open('C:\\Users\\Dominik Lovetinsky\\Desktop\\1N4148.csv', 'w') as export1:
    for i in range(len(U1)):
        export1.write(str(U1[i]) + ';' + str(Ur1[i]) + ';' + str(Ud1[i]) + ';' + str(Irz1[i]) + ';' + str(T1[i]) + '\n')
"""