import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

# import pandas as pd

n = Counter()
reli = [3, 1, 1, 1, 1, 1, 1]
ger = [3, 3, 5, 4, 4, 4, 3]
eng = [1, 1, 4, 4, 3, 3, 2]
ggp = [1, 1, 4, 4, 4, 3, 2]
besp = [2, 2, 2, 2, 2, 1, 1]
math = [2, 3, 5, 3, 3, 2, 2]
nawi = [2, 2, 4, 2, 3, 2, 2]
es1 = [3, 2, 5, 4, 2, 4, 2]
aut = [2, 1, 4, 3, 3, 3, 1]
at1 = [0, 0, 5, 4, 4, 3, 2]
ie1 = [0, 0, 0, 0, 0, 3, 2]
aiit = [2, 2, 5, 3, 1, 1, 1]
cpe = [2, 2, 5, 3, 3, 1, 1]
lab1 = [0, 0, 0, 0, 0, 2, 1]
werk = [3, 2, 2, 1, 1, 2, 2]
year = ['2016/17 1. Semester', '2016/17 2. Semester', '2017/18 2. Semester',
        '2018/19 1. Semester', '2018/19 2. Semester', '2019/20 1. Semester',
        '2019/20 2. Semester']
yearn = np.arange(len(year))
width = 0.8 / 15
print(plt.style.available)

n.update(reli)
n.update(ger)
n.update(eng)
n.update(ggp)
n.update(besp)
n.update(math)
n.update(nawi)
n.update(es1)
n.update(aut)
n.update(at1)
n.update(ie1)
n.update(aiit)
n.update(cpe)
n.update(lab1)
n.update(werk)

# plt.xkcd()
# plt.style.use('fivethirtyeight')
plt.style.use('seaborn')
plt.title('Notenverlauf meiner HTL-Laufbahn')
plt.bar(yearn - width * 7, reli, width=width, label='Religion')
plt.bar(yearn - width * 6, ger, width=width, label='Deutsch')
plt.bar(yearn - width * 5, eng, width=width, label='Englisch')
plt.bar(yearn - width * 4, ggp, width=width, label='GGP')
plt.bar(yearn - width * 3, besp, width=width, label='BESP')
plt.bar(yearn - width * 2, math, width=width, label='Mathematik')
plt.bar(yearn - width, nawi, width=width, label='NAWI')
plt.bar(yearn, es1, width=width, label='Energiesysteme')
plt.bar(yearn + width, aut, width=width, label='AUT')
plt.bar(yearn + width * 2, at1, width=width, label='Antriebstechnik')
plt.bar(yearn + width * 3, ie1, width=width, label='Industrieelektronik')
plt.bar(yearn + width * 4, aiit, width=width, label='Informatik')
plt.bar(yearn + width * 5, cpe, width=width, label='CPE')
plt.bar(yearn + width * 6, lab1, width=width, label='Labor')
plt.bar(yearn + width * 7, werk, width=width, label='Werkstatt')
plt.legend(loc='upper right')
plt.xticks(ticks=yearn, labels=year)
plt.grid(True)
plt.tight_layout()

# with open("C:\\Users\\Dominik Lovetinsky\\Desktop\\Noten3AHET.png", 'wb') as export:
#     plt.savefig(fname=export, format='png', dpi=1024)

# plt.show()

"""grades = []
labels = []
for item in n.most_common(6):
    if item[0] != 0:
        labels.append(str(item[0]) + '.er')
        grades.append(item[1])
print(n)
explode = [0, 0.15, 0, 0, 0]
plt.pie(grades, labels=labels, explode=explode, wedgeprops={'edgecolor': 'black'})
plt.show()"""
# with open("C:\\Users\\Dominik Lovetinsky\\Desktop\\GradesAsPie.png", 'wb') as export:
#     plt.savefig(export, format='png', dpi=512)

# plt.show()
