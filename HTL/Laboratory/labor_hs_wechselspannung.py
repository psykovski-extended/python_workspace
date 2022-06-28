# Hochpannungslabor - Wechselspannung

import numpy as np
import matplotlib.pyplot as plt

# In[29]:

# Kugel Kuglel, alle Werte ohne Faktor, Kugeldurchmesser 5cm
# Dreimalige Messung für Mittelwertbildung

l1 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55]  # mm

Uprim1 = np.array([20, 50, 70, 90, 105, 115, 125, 135, 144, 150, 158]) # V
Uc1 = np.array([24, 45, 63, 80, 97, 105, 116, 120, 130, 137, 140]) # kV

Uprim2 = np.array([25, 50, 69, 90, 104, 115, 126, 136, 144, 150, 158])
Uc2 = np.array([22, 46, 62, 78, 93, 105, 115, 121, 128, 135, 141])

Uprim3 = np.array([25, 50, 70, 90, 104, 115, 126, 136, 144, 150, 158])
Uc3 = np.array([23, 45, 61, 78, 90, 103, 113, 122, 130, 137, 140])

Up = ((Uprim1 + Uprim2 + Uprim3) / 3)
Uc = ((Uc1 + Uc2 + Uc3) / 3) / .5

messbereich = []
faktorC = [0.5]


# In[30]:


plt.plot(l1, Up, label="$U_P$ Primärspannung in V")
plt.plot(l1, Uc, label="$U_C$ Sekundärspannung in kV")
plt.xlabel("Abstand in mm")
plt.legend()
plt.show()


# In[31]:


l2 = [5, 10, 15, 20, 25, 30, 38, 48] # in mm

# Ab 30 V primär entstanden bereits erste Korona-Effekte, 6 cm

Uprim1 = np.array([20, 29, 26, 38, 45, 49, 54, 66]) # in V
Uc1 = np.array([17.5, 26, 25, 35, 42, 45, 47, 60]) # in kV

Uprim2 = np.array([16, 28, 29, 38, 46, 50, 55, 60]) # in V
Uc2 = np.array([16, 25, 27, 35, 42, 45, 47, 55]) # in kV

Uprim3 = np.array([18, 21, 31, 36.5, 45, 50, 56, 80]) # in V
Uc3 = np.array([17, 23, 29, 34, 41, 45, 49, 75]) # in kV

Up = (Uprim1 + Uprim2 + Uprim3) / 3
Uc = ((Uc1 + Uc2 + Uc3) / 3) / 0.5


# In[32]:


plt.plot(l2, Up, label="$U_P$ Primärspannung in V")
plt.plot(l2, Uc, label="$U_C$ Sekundärspannung in kV")
plt.xlabel("Abstand in mm")
plt.legend()
plt.show()


# In[33]:


l3 = [5, 10, 17, 25, 35, 45]  # in mm

# Ab 30 V primär entstanden bereits erste Korona-Effekte, 6cm

Uprim1 = np.array([15, 26, 35, 46, 55, 63]) # in V
Uc1 = np.array([14, 25, 31, 42, 47, 55]) # in kV

Uprim2 = np.array([18, 24, 32, 45, 59, 60]) # in V
Uc2 = np.array([17, 22, 30, 40, 52, 54]) # in kV

Uprim3 = np.array([16, 24, 33, 47, 55, 61]) # in V
Uc3 = np.array([14, 21, 29, 42, 48, 54]) # in kV

Up = (Uprim1 + Uprim2 + Uprim3) / 3
Uc = ((Uc1 + Uc2 + Uc3) / 3) / 0.5


# In[34]:


plt.plot(l3, Up, label="$U_P$ Primärspannung in V")
plt.plot(l3, Uc, label="$U_C$ Sekundärspannung in kV")
plt.xlabel("Abstand in mm")
plt.legend()
plt.show()


# In[35]:


# 60kV Isolator
#trocken
Uprim1 = np.array([150, 120, 116]) # in V
Uc1 = np.array([110, 115, 118]) # in kV
#Salzwasser
Uw = 45
Uc2 = 30

