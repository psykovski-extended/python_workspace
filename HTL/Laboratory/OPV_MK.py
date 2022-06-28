import matplotlib.pyplot as plt
import pandas as pd
import HTL.util.inductor as util
import numpy as np

Utp = 4
Utm = -3

Uamin = -15
Uamax = 15

R1 = 220
Rf = 1e+3

Uref1 = (Utp + Uamin * R1 / Rf) * Rf / (Rf + R1)  # nicht invertierender Verstaerker
Uref2 = (Utp + Uamax * R1 / Rf) * Rf / (Rf + R1)  # nicht invertierender Verstaerker

R1 = 33e+3
Rf = 100e+3

Uref1 = (Utm - Uamin * R1 / (R1 + Rf)) * (R1 + Rf) / Rf  # invertierender Verstaerker
Uref2 = (Utp - Uamax * R1 / (R1 + Rf)) * (R1 + Rf) / Rf  # invertierender Verstaerker

Uoff = 2.1  # OPV schaltet nicht mehr

Utp = 1
Utm = -5
R1zuRf = 6 / 30
R1 = 22e+3
Rf = R1 / R1zuRf
Uref1 = (Utm - Uamin * R1 / (R1 + Rf)) * (R1 + Rf) / Rf
Uref2 = (Utp - Uamax * R1 / (R1 + Rf)) * (R1 + Rf) / Rf

"""for i in [9, 10, 13, 14]:
    data1 = pd.read_csv("C:\\Users\\Dominik Lovetinsky\\HTBLuVA St. Pölten\\c.freudenthaler@htlstp.at - "
                        "4AHET\\15_OPV-MK-Grundschaltung\\data\\csv\\scope_" + str(i) + ".csv")

    time1 = data1[data1.keys()[0]]
    v1 = util.movmean(data1[data1.keys()[1]], 10)
    v2 = util.movmean(data1[data1.keys()[2]], 10)

    plt.plot(v1[:1300], v2[:1300])
    plt.grid(True)

    plt.xlabel('$U_{in}$', size=12)
    plt.ylabel('$U_{out}$', size=12)

    plt.tight_layout()
    plt.show()"""

data = pd.read_csv("C:\\Users\\Dominik Lovetinsky\\HTBLuVA St. Pölten\\c.freudenthaler@htlstp.at - "
                   "4AHET\\15_OPV-MK-Grundschaltung\\data\\csv\\scope_15.csv")

time = np.array(data[data.keys()[0]]) * 1000
v = data[data.keys()[1]]

plt.plot(time, util.movmean(v, 15))
plt.grid(True)
plt.ylabel("[U] V")
plt.xlabel("[t] ms")

plt.tight_layout()
plt.show()
