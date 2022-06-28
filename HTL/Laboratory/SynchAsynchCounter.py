import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from HTL.util import inductor

# Rauschen
data1 = pd.read_csv(
    'C:\\Users\Dominik Lovetinsky\\HTBLuVA St. Pölten\\c.freudenthaler@htlstp.at - 4AHET\\05_Synch_Asynch_Counter\\data\\csv\\scope_8.csv')
# Asynch Counter
data2 = pd.read_csv(
    'C:\\Users\Dominik Lovetinsky\\HTBLuVA St. Pölten\\c.freudenthaler@htlstp.at - 4AHET\\05_Synch_Asynch_Counter\\data\\csv\\scope_9.csv')
# Synch Counter
data3 = pd.read_csv(
    'C:\\Users\Dominik Lovetinsky\\HTBLuVA St. Pölten\\c.freudenthaler@htlstp.at - 4AHET\\05_Synch_Asynch_Counter\\data\\csv\\scope_10.csv')

noiseT = np.array(data1[data1.keys()[0]]) * 10e+6
noise1 = inductor.movmean(data1[data1.keys()[1]], 5)
noise2 = inductor.movmean(data1[data1.keys()[2]], 5)
noise3 = inductor.movmean(data1[data1.keys()[3]], 5)
noise4 = inductor.movmean(data1[data1.keys()[4]], 5)

fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, sharex='col')

fig.tight_layout()
ax1.plot(noiseT, noise1, color='blue')
ax1.set_ylabel('Bit 0', size=15)
ax1.set_yticks(())
ax2.plot(noiseT, noise2, color='green')
ax2.set_ylabel('Bit 1', size=15)
ax2.set_yticks(())
ax3.plot(noiseT, noise3, color='orange')
ax3.set_ylabel('Bit 2', size=15)
ax3.set_yticks(())
ax4.plot(noiseT, noise4, color='red')
ax4.set_ylabel('Bit 3', size=15)
ax4.set_yticks(())
plt.xlabel('[t_inv] us', size=15)
plt.subplots_adjust(wspace=0, hspace=0)
plt.tick_params(axis='both', which='major', labelsize=12)

asyncT = np.array(data2[data2.keys()[0]]) * 10e+3
async1 = inductor.movmean(data2[data2.keys()[1]], 5)
async2 = inductor.movmean(data2[data2.keys()[2]], 5)
async3 = inductor.movmean(data2[data2.keys()[3]], 5)
async4 = inductor.movmean(data2[data2.keys()[4]], 5)

fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, sharex='col')

fig.tight_layout()
ax1.plot(asyncT, async1, color='blue')
ax1.set_ylabel('Bit 0', size=15)
ax1.set_yticks(())
ax2.plot(asyncT, async2, color='green')
ax2.set_ylabel('Bit 1', size=15)
ax2.set_yticks(())
ax3.plot(asyncT, async3, color='orange')
ax3.set_ylabel('Bit 2', size=15)
ax3.set_yticks(())
ax4.plot(asyncT, async4, color='red')
ax4.set_ylabel('Bit 3', size=15)
ax4.set_yticks(())
plt.xlabel('[t_inv] ms', size=15)
plt.subplots_adjust(wspace=0, hspace=0)
plt.tick_params(axis='both', which='major', labelsize=12)

syncT = np.array(data3[data3.keys()[0]]) * 10e+3
sync1 = inductor.movmean(data3[data3.keys()[1]], 5)
sync2 = inductor.movmean(data3[data3.keys()[2]], 5)
sync3 = inductor.movmean(data3[data3.keys()[3]], 5)
sync4 = inductor.movmean(data3[data3.keys()[4]], 5)

fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, sharex='col')

fig.tight_layout()
ax1.plot(syncT, sync1, color='blue')
ax1.set_ylabel('Bit 0', size=15)
ax1.set_yticks(())
ax2.plot(syncT, sync2, color='green')
ax2.set_ylabel('Bit 1', size=15)
ax2.set_yticks(())
ax3.plot(syncT, sync3, color='orange')
ax3.set_ylabel('Bit 2', size=15)
ax3.set_yticks(())
ax4.plot(syncT, sync4, color='red')
ax4.set_ylabel('Bit 3', size=15)
plt.xlabel('[t_inv] ms', size=15)
ax4.set_yticks(())
plt.subplots_adjust(wspace=0, hspace=0)
plt.tick_params(axis='both', which='major', labelsize=12)
