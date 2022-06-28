import matplotlib.pyplot as plt
import numpy as np

R_25 = 1000
R_100 = R_25 * 1.696
R_m55 = R_25 * 0.49

print(R_25, R_100, R_m55)

t = [-55, -50, -40, -30, -20, -10, 0, 10, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 125, 130, 140, 150]
r = [490, 515, 567, 624, 684, 747, 815, 886, 961, 1000, 1040, 1122, 1209, 1299, 1392, 1490, 1591, 1696, 1805,
     1915, 1970, 2023, 2124, 2211]

t_new = np.linspace(-55, 150, 100)
f = np.polyfit(t, r, 1)
f = np.poly1d(f)
r_new = f(t_new)
print(f)

plt.plot(t, r)
plt.plot(t_new, r_new)
plt.show()

# ############ Dimensionierung

R_0 = 815
R_120 = 1915

R_spt = 1700
Ue = 5

R_0_ist = R_spt / (Ue / 1.62013 - 1)  # 814.889625
R_120_ist = R_spt / (Ue / 2.64855 - 1)
R_0 = R_0_ist
R_120 = R_120_ist

print(R_0_ist, R_120_ist)

Ua_soll_max = 4.8
Ua_soll_min = 0.2

U_0 = Ue * R_0 / (R_0 + R_spt)
U_120 = Ue * R_120 / (R_120 + R_spt)
print(U_0, U_120, "hi")

U_hys = U_120 - U_0
f_r = (Ua_soll_max - Ua_soll_min) / U_hys

R_1 = 10000
R_2 = R_1
R_3 = 18000

R_4 = (2 * f_r * R_3) - R_3
Un = ((U_0 * f_r) - 0.2) * (R_3 / R_4)

print(R_3, R_4, Un)
