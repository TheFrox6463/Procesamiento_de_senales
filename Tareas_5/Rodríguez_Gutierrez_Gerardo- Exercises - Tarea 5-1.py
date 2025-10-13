import numpy as np
import matplotlib.pyplot as plt
import lcapy as lc
import numpy as np
#Z-transform of unit sample and unit step signal
from lcapy import n,delta,us
#Operaciones
#X1
x1 = delta(n - 5)
X1 = x1.ZT()
print("X1(z) =", X1)
#X2
x2 = us(n) - us(n - 1)
X2 = x2.ZT()
print("X2(z) =", X2)
#X3
x3 = n * us(n)
X3 = x3.ZT()
print("X3(z) =", X3)
#X4
w0 = lc.w0
x4 = lc.sin(w0 * n)
X4 = x4.ZT()
print("X4(z) =", X4)
