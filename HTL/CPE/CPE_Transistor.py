import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("D:\\HTL\\CPE\\4AHET\\L-DAMB\\mehrstufig.Trans.V\\furierAnalyse.DAT")
data1 = pd.read_csv("D:\\HTL\\CPE\\4AHET\\L-DAMB\\mehrstufig.Trans.V\\Frequenzgang.DAT")
data2 = pd.read_csv("D:\\HTL\\CPE\\4AHET\\L-DAMB\\mehrstufig.Trans.V\\voltageGainOutput.DAT")
f = data[data.keys()[0]]
UaFourier = data[data.keys()[1]]

f1 = data1[data1.keys()[0]]
gain = data1[data1.keys()[1]]

t = data2[data2.keys()[0]]
Ua = data2[data2.keys()[1]]
Ue = data2[data2.keys()[2]]

plt.figure(1)
plt.grid(True)
plt.plot(f, UaFourier)
plt.ylabel('[Ua] dB')
plt.xlabel('[f] Hz')
# plt.title('Fourier Analyse - Klirrfaktor')

plt.figure(2)
plt.grid(True)
plt.plot(f1, gain)
plt.xscale('log')
# plt.title('Spannungsverstärkung - Frequenzgang')
plt.ylabel('[G] dB')
plt.xlabel('[f] Hz')

plt.figure(3)
plt.grid(True)
plt.plot(t, Ua, label='Ua')
plt.plot(t, Ue, label='Ue')
# plt.title('Spannungsverstärkung - Ue / Ua')
plt.xlabel('[t_inv] ms')
plt.ylabel('[U] V')
plt.legend()

"""i1, i2, j1, j2 = inductor.getPeriod(list(Ua), list(Ua))
off = sum_(Ua[i1:i2])
print(off)"""
