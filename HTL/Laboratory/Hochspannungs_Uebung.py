import numpy as np
import matplotlib.pyplot as plt

# Messung 1: Kugel - Kugel # Deckel auf Widerstand fehlte # Spannungsteiler vl in Messung schon berücksichtigt -> Spilka
a1 = [5, 6, 7, 8, 9, 10, 15, 20]  # mm
Ukk1 = np.array([4.8, 7.5, 5, 7, 10, 14, 2, 2])  # kV nach Überschlag
Ukk12 = np.array([11, 13, 15, 17, 22, 25, 40, 52])  # Spannung vor Überschlag
Ukk2 = np.array([6, 5, 7.5, 6, 7.5, 7, 2, 1.8])
Ukk22 = np.array([10, 14, 16.5, 20, 22, 24.7, 38.5, 52])
Ukk3 = np.array([5, 6.5, 7.5, 6, 6, 7.5, 2, 2])
Ukk32 = np.array([9.5, 14.5, 17, 20, 22.6, 25, 37.5, 50])

u1 = (Ukk1 + Ukk2 + Ukk3) / 3
u2 = (Ukk12 + Ukk22 + Ukk32) / 3

# 75 kV --> zu viel bei Kugel Kugel --> Sicherung gefolgen (30 mm)

# plt.figure(1)
plt.plot(a1, u1)
plt.scatter(a1, u1, label='Vor Lichtbogen')
plt.plot(a1, u2)
plt.scatter(a1, u2, label='Nach Lichtbogen')
plt.legend()
plt.xlabel('[a] mm')
plt.ylabel('[U] kV')
plt.show()

# Messung 2: Platte - Spitze
a2 = [5, 6, 7, 8, 9, 10, 15, 20]
Usp1 = np.array([10, 11.5, 13, 15, 14, 16, 27.5, 33.5])  # kV vor Überschlag
Usp12 = np.array([10, 10, 11, 12, 13, 11.5, 25, 27])  # Spannung nach Überschlag
Usp2 = np.array([11, 11.5, 10.5, 13, 14.5, 15, 28.5, 35])
Usp22 = np.array([9, 11.5, 12.5, 12.5, 11, 12.5, 10, 30])
Usp3 = np.array([10, 11.5, 12.5, 13.5, 13.5, 15, 26, 32])
Usp32 = np.array([9, 11, 10, 10.5, 12, 12, 12.5, 5])

u12 = (Usp1 + Usp2 + Usp3) / 3
u22 = (Usp12 + Usp22 + Usp32) / 3

# Messung 3 aus Zeitgründen übersprungen
# Messung 4 Isolation trocken 100 - 110 kV; nass: 90 - 100kV
# Messung 5 Funkenlöschstrecke

plt.figure(2)
plt.plot(a2, u12)
plt.scatter(a2, u12, label='Vor Lichtbogen')
plt.plot(a2, u22)
plt.scatter(a2, u22, label='Nach Lichtbogen')
plt.legend()
plt.xlabel('[a] mm')
plt.ylabel('[U] kV')
plt.show()

"""with open("C:\\Users\\Dominik Lovetinsky\\HTBLuVA St. Pölten\\c.freudenthaler@htlstp.at - "
          "4AHET\\11_GS-Hochspannung\\data\\Messwerte.csv", "w") as export:
    export.write("[a] mm,$[U_{kk1}] kV$,$[U_{kk12}] kV$,$[U_{kk2}] kV$,$[U_{kk22}] kV$,$[U_{kk3}] kV$,$[U_{kk32}] kV$,"
                 "$[U_{m1}] kV$,$[U_{m2}] kV$\n")
    for i in range(len(a1)):
        export.write(str(a1[i]) + "," + str(Ukk1[i]) + "," + str(Ukk12[i]) + "," + str(Ukk2[i]) + "," + str(Ukk22[i]) + "," + str(Ukk3[i]) + ","
                     + str(Ukk32[i]) + "," + str(u1[i]) + "," + str(u2[i]) + "\n")
    export.write("[a] mm,$[U_{sp1}] kV$,$[U_{sp12}] kV$,$[U_{sp2}] kV$,$[U_{sp22}] kV$,$[U_{sp3}] kV$,$[U_{sp32}] kV$,"
                 "$[U_m] kV,$[U_{m2}] kV$\n")
    for i in range(len(a2)):
        export.write(str(a2[i]) + "," + str(Usp1[i]) + "," + str(Usp12[i]) + "," + str(Usp2[i]) + "," + str(Usp22[i]) + "," + str(Usp3[i]) + ","
                     + str(Usp32[i]) + "," + str(u12[i]) + "," + str(u22[i]) + "\n")
"""
