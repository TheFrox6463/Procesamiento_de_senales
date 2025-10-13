#Inverse z-transform of z^(-1)
from lcapy import z
#Inversa de Z**-2
X1=z**(-2)
x1=X1.IZT()
print(x1) 
#Inversa de 1/(1-z**-1)**2
X2=1/(1-z**-1)**2
x2=X2.IZT()
print(x2) 