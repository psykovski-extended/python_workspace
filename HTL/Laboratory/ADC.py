import matplotlib.pyplot as plt
import numpy as np

LSB = 5.12 / (2**8-1)
vpp2 = 2.56
ufl11 = 5.039
ufl12 = 5.017
uLSB1 = (ufl11-ufl12)

ufl13 = 4.999
uLSB2 = (ufl12-ufl13)

ufl14 = 4.98
uLSB3 = (ufl13-ufl14)

ufl15 = 4.958
uLSB4 = (ufl14-ufl15)

ufl16 = 4.94
uLSB5 = (ufl15-ufl16)

print(uLSB1, uLSB2, uLSB3, uLSB4, uLSB5)

uLSB_mu = (uLSB1 + uLSB2 + uLSB3 + uLSB4 + uLSB5)/5

print(uLSB_mu)
print(LSB)

off = LSB - np.array([LSB, uLSB1, uLSB2, uLSB3, uLSB5, uLSB4])

print(off)
