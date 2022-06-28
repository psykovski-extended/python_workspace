import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fString = open('C:\\Users\\Dominik Lovetinsky\\Desktop\\Python\\iris.data', 'r')
fFloat = open('C:\\Users\\Dominik Lovetinsky\\Desktop\\Python\\iris.csv', 'w')

for line in fString:
    line = line.replace('Iris-setosa', '1')
    line = line.replace('Iris-versicolor', '2')
    line = line.replace('Iris-virginica', '3')
    fFloat.write(line)

fString.close()
fFloat.close()

fFloat = open('C:\\Users\\Dominik Lovetinsky\\Desktop\\Python\\iris.csv', 'r')

dataset = np.loadtxt(fFloat, delimiter=',')

fFloat.close()

fig = plt.figure(1)

ax = fig.add_subplot(2, 2, 1)
ax.scatter(dataset[0:50, 0], dataset[0:50, 1], c='red', s=60, alpha=0.6)
ax.scatter(dataset[50:100, 0], dataset[50:100, 1], c='green', marker='^', s=60, alpha=0.6)
ax.scatter(dataset[100:150, 0], dataset[100:150, 1], c='blue', marker='*', s=60, alpha=0.6)
ax.set_xlabel('Kelchblattlänge (cm)')
ax.set_ylabel('Kelchblattbreite (cm)')
ax.grid(True, linestyle='-', color='0.75')

ax = fig.add_subplot(2, 2, 2)
ax.scatter(dataset[0:50, 2], dataset[0:50, 3], c='red', s=60, alpha=0.6)
ax.scatter(dataset[50:100, 2], dataset[50:100, 3], c='green', marker='^', s=60, alpha=0.6)
ax.scatter(dataset[100:150, 2], dataset[100:150, 3], c='blue', marker='*', s=60, alpha=0.6)
ax.set_xlabel('Kornblattlänge (cm)')
ax.set_ylabel('Kornblattbreite (cm)')
ax.grid(True, linestyle='-', color='0.75')

ax = fig.add_subplot(2, 2, 3)
ax.scatter(dataset[0:50, 0], dataset[0:50, 2], c='red', s=60, alpha=0.6)
ax.scatter(dataset[50:100, 0], dataset[50:100, 2], c='green', marker='^', s=60, alpha=0.6)
ax.scatter(dataset[100:150, 0], dataset[100:150, 2], c='blue', marker='*', s=60, alpha=0.6)
ax.set_xlabel('Kelchblattlänge (cm)')
ax.set_ylabel('Kornblattlänge (cm)')
ax.grid(True, linestyle='-', color='0.75')

ax = fig.add_subplot(2, 2, 4)
ax.scatter(dataset[0:50, 1], dataset[0:50, 3], c='red', s=60, alpha=0.6)
ax.scatter(dataset[50:100, 1], dataset[50:100, 3], c='green', marker='^', s=60, alpha=0.6)
ax.scatter(dataset[100:150, 1], dataset[100:150, 3], c='blue', marker='*', s=60, alpha=0.6)
ax.set_xlabel('Kelchblattbreite (cm)')
ax.set_ylabel('Kornblattbreite (cm)')
ax.grid(True, linestyle='-', color='0.75')

plt.tight_layout()
plt.show(block=False)

fig = plt.figure(2)
ax = fig.add_subplot(1, 1, 1, projection='3d')

ax.scatter(dataset[0:50, 1], dataset[0:50, 2], dataset[0:50, 3], c='red', s=60, alpha=0.6)
ax.scatter(dataset[50:100, 1], dataset[50:100, 2], dataset[50:100, 3], c='green', marker='^', s=60, alpha=0.6)
ax.scatter(dataset[100:150, 1], dataset[100:150, 2], dataset[100:150, 3], c='blue', marker='*', s=60, alpha=0.6)

ax.set_xlabel('Kelchblattbreite (cm)')
ax.set_ylabel('Kornblattlänge (cm)')
ax.set_zlabel('Kornblattbreite (cm)')

plt.show()
