import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import control as ss
#Datos
frecuencia_corte=np.radians(10)
frecuencia_res=np.radians(20)
Ap, As, Td=3,30, 1
muestras=1000
# prewarping process
omega_p=(2/Td)*np.tan(frecuencia_corte/2)
omega_s=(2/Td)*np.tan(frecuencia_res/2)
#Computation of order and normalized cut-off frequency
N, omega_c=signal.buttord(omega_p,omega_s,Ap,As,analog=True)
print('Order of the Filter N =', N)
print('Cut-off frequency= {:.4f} rad/s '. format(omega_c))
# Computation of H(s)
b, a=signal.butter(N,omega_c,'low', analog=True)
s1 = ss.tf(b, a)
print('Transfer function H(s)=',s1)
bz, az=signal.bilinear(b, a, Td)
z1 = ss.tf(bz,az,Td)
print('Transfer function H(z)=',z1) 
#La magnitud 
transfer=ss.tf(b,a)
omega1 = np.linspace(0, 10, 100)  
mag, phase, omega1=ss.freqresp(transfer, omega1)
plt.figure(1),plt.plot(omega1,np.abs(mag)),plt.xlabel('$\Omega$-->'),
plt.ylabel('$|H(j\Omega)|$'),plt.title('Magnitude del filtro Butterworth') 
plt.show()