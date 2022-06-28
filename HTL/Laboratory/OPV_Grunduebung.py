import matplotlib.pyplot as plt

# TL084 - OPV
# 1. OPV oben links wurde verwendet

Rp1 = 10e+3
Rp2 = 110e+3
R = 1e+6

Uccp = 15
Uccm = -15

Ue = [-40, -30, -26, -23, -20, -17, -14.4, -11, -9, -6, -3, 0.7, 1.5, 3, 5.5, 6, 8,
      17, 20, 23, 26, 29, 40]  # e-3
Ua = [-13.2, -13.34, -13.2, -13.2, -13.1, -13.05, -13, -13.1, -12.8, -12.2, -4.2, 0.9, 1.4, 3, 8.2, 8.9, 10.85,
      14.45, 14.45, 14.45, 14.45, 14.45, 14.45]  # 14.45 -> max

"""p = np.polyfit(np.array(Ue), np.array(Ua), 6)
Uen = np.linspace(Ue[0], Ue[-1], 1000)
f = np.poly1d(p)

Uan = f(Uen)"""

plt.figure(1)
plt.plot(Ue, Ua)
plt.grid(True)

"""
Measure 1: 5kHz, scope1
Measure 2: 500Hz, scope2

Measure 3: 10kHz, scope5; scope4 = png
Measure 4: 100Hz, scope6, scope7
"""

"""data1 = pd.read_csv('F:\\scope_1.csv')

U1 = data1[data1.keys()[1]]
U2 = data1[data1.keys()[2]]

U1g = inductor.movmean(U1[:140], 10)
U2g = inductor.movmean(U2[:140], 10)

plt.figure(2)
plt.grid(True)
plt.plot(U1g, U2g)"""

with open("C:\\Users\\Dominik Lovetinsky\\Desktop\\TL084Uebertragungskennlinie.csv", 'w') as to:
    to.write('Ue,Ua\n')
    for i in range(len(Ue)):
        to.write(str(Ue[i]) + ',' + str(Ua[i]) + '\n')
