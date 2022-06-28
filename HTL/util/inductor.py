import numpy as np


def movmean(arr, num=2):
    narr = []
    numT = num
    for i in range(len(arr)):
        if i + num < len(arr):
            narr.append(np.sum(arr[i:i + num]) / num)
        else:
            narr.append(np.sum(arr[-numT:i + num]) / num)
    return narr


def getPeriod(l1, l2):
    i = 0
    while l1[i] <= 0:
        i += 1
    i1 = i
    i += 10
    while l1[i] >= 0:
        i += 1
    i += 10
    while l1[i] <= 0:
        i += 1
    i2 = i

    i = 0
    while l2[i] <= 0:
        i += 1
    k1 = i
    i += 10
    while l2[i] >= 0:
        i += 1
    i += 10
    while l2[i] <= 0:
        i += 1
    k2 = i
    return i1, i2, k1, k2


if __name__ == '__main__':
    from matplotlib import pyplot as plt
    import pandas as pd
    from math import *

    data = pd.read_csv('D:\\HTL\\Labor\\Übungen\\ALL0000\\F0000CH1.csv')
    data1 = pd.read_csv('D:\\HTL\\Labor\\Übungen\\ALL0000\\F0000CH2.csv')
    time = data[data.keys()[3]]
    voltage = movmean(data[data.keys()[4]], 11)
    current = movmean(data1[data1.keys()[4]], 11)

    # sum_ of the first full period
    j1, j2, h1, h2 = getPeriod(voltage, current)
    # offsets gets evaluated
    off_v = sum([voltage[i] for i in range(j1, j2, 1)]) / (j2 - j1 + 1)
    off_c = sum([current[i] for i in range(h1, h2, 1)]) / (h2 - h1 + 1)

    volt_sym = voltage - off_v
    cur_sym = current - off_c

    rs = 10.5
    voltageL = volt_sym - cur_sym * rs

    n1, n2, m1, m2 = getPeriod(voltageL, cur_sym)

    T = time[m2] - time[m1]
    f = 1 / T
    dt = time[m1] - time[n1]
    phi = (dt * 360) / T

    ueff = sqrt(sum([voltageL[i] ** 2 for i in range(n1, n2, 1)]) / (n2 - n1 + 1))
    ieff = sqrt(sum([current[i] ** 2 for i in range(m1, m2, 1)]) / (m2 - m1 + 1))

    z = ueff / ieff
    zc = complex(z * cos(phi * pi / 180), z * sin(phi * pi / 180))

    yp = 1 / zc
    rp = 1 / yp.real
    xp = 1 / yp.imag
    L = -xp / (2 * np.pi * f)

    print('T: ' + str(T), 'f: ' + str(f), chr(0x3C6) + ': ' + str(phi), 'Ueff: ' + str(ueff), 'Ieff: ' + str(ieff), 'Z: '
      + str(zc), 'Rp: ' + str(rp), 'L: ' + str(L), sep='\n')

    u_smooth = np.polyfit(time, voltageL, 17)
    u_y = np.poly1d(u_smooth)(time)

    time_avrg = np.linspace(time[0], time[time.size - 1], 2000)
    u_new = ieff * sqrt(2) * np.sin(2 * np.pi * f * time_avrg - phi * np.pi / 180)

    fig = plt.figure(1)
    cur = fig.add_subplot(221)
    cur.plot(time, cur_sym, color='red', label='Current')

    volt = fig.add_subplot(222)
    volt.plot(time, volt_sym, color='#e233ee', label='Voltage')

    voltL = fig.add_subplot(223)
    voltL.plot(time, voltageL, color='blue', label='Voltage on inductor')

    voltS = fig.add_subplot(224)
    voltS.plot(time_avrg, u_new, label='Averaged curve', color='#ff2222')

    cur.grid(True)
    volt.grid(True)
    voltL.grid(True)
    voltS.grid(True)

    fig.legend(loc='upper right')

    fig.show()
