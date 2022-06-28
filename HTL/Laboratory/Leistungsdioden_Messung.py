import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
from scipy import interpolate


def movmean(arr, num=2):
    narr = []
    numT = num
    for i in range(len(arr)):
        if i + num < len(arr):
            narr.append(np.sum(arr[i:i + num]) / num)
        else:
            narr.append(np.sum(arr[-numT:i + num]) / num)
    return narr


if __name__ == '__main__':
    x = os.scandir('C:\\Users\\Dominik Lovetinsky\\HTBLuVA St. Pölten\\c.freudenthaler@htlstp.at - ' +
                   '4AHET\\09_Leistungsdioden\\data\\csv')

    csvData = [(i.name if '.csv' in i.name else None) for i in x]
    figure = 0
    legends = ['IDP30E120', '40HF120', '1N4007', '1N4148', 'Semikron']
    for i in csvData:
        if i is not None and 'scope' in i:
            data1 = pd.read_csv('C:\\Users\\Dominik Lovetinsky\\HTBLuVA St. Pölten\\c.freudenthaler@htlstp.at - ' +
                                '4AHET\\09_Leistungsdioden\\data\\csv\\' + i)
            U = data1[data1.keys()[1]]
            Ud = data1[data1.keys()[2]]

            I = np.array(movmean(np.array(U[600:-300]), 45))
            Ud = np.array(movmean(np.array(Ud[600:-300]), 45))

            plt.grid(True)
            plt.tight_layout()
            plt.plot(Ud, np.array(I), label=legends[figure])
            plt.ylabel('[Id] mA', size=12)
            plt.xlabel('[Ud] V', size=12)
            plt.legend(prop={'size': 12})
            figure += 1

    figure = 2

    """for i in csvData:
        if i is not None and 'scope' not in i:
            data = pd.read_csv('C:\\Users\\Dominik Lovetinsky\\HTBLuVA St. Pölten\\c.freudenthaler@htlstp.at - ' +
                               '4AHET\\09_Leistungsdioden\\data\\csv\\' + i)
            print(i)
            t_inv = np.array(movmean(np.array(data[data.keys()[0]]), 45))
            U = movmean(np.array(data[data.keys()[1]]), 45)
            U1 = movmean(np.array(data[data.keys()[2]]), 45)
            U2 = movmean(np.array(data[data.keys()[3]]), 45)
            t_inv -= t_inv[0]
            # label = i.replace('Einschalten', '').replace('Ausschalten', '').replace('.csv', '')

            plt.figure(figure)
            plt.tight_layout()
            plt.ticklabel_format(style='scientific', scilimits=(0, 0), useMathText=True)
            plt.plot(t_inv, U, label='Eingangsspannung')
            plt.plot(t_inv, U1, label='Diodenspannung Ud')
            plt.plot(t_inv, U2, label='Diodenstrom Id')
            plt.legend(prop={'size': 12})
            plt.xlabel('[t_inv] s', size=12)
            plt.ylabel('[U] V', size=12)
            figure += 1"""
