import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import time

plt.figure(1)
fuenf = mpimg.imread('C:\\Users\\Dominik Lovetinsky\\Desktop\\Python\\mnist_png\\testing\\5\\356.png')
plt.imshow(fuenf, cmap='gray')
print(fuenf.shape)

plt.figure(2)
weka = mpimg.imread('C:\\Users\\Dominik Lovetinsky\\Desktop\\Python\\wekaralle.png')
plt.imshow(weka)
print(weka.shape)

newWeka = np.copy(weka)
t = time.time()
for x in range(1007):
    for y in range(1008):
        newWeka[x, y, 0] = max(1 - (x/500 - 1)**2 - (y/500 - 1)**2, 0)
elapsed = time.time() - t
print('Benötigte Zeit(s): ' + str(elapsed))

plt.figure(3)
plt.imshow(newWeka)

newWeka2 = np.copy(weka)
t = time.time()
xv, yv = np.meshgrid(np.arange(0, 1008), np.arange(0, 1007))
newWeka[:, :, 0] = np.maximum(1 - (xv/500 - 1)**2 - (yv/500 - 1)**2, 0)
del(xv, yv)
elapsed = time.time() - t
print('Benötigte Zeit(s): ' + str(elapsed))
plt.figure(4,)
plt.imshow(newWeka2[..., :3]@[0.299, 0.587, 0.114])
