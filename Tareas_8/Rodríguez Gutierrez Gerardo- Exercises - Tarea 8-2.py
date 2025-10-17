import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import control as ss 
#Ejemplo del libro, filtro butterworth 
N=1 #Orden del filtro 
Corte=5 #Frecuencia de corte
omega1 = np.linspace(0, 10, 100)    
b, a = signal.butter(N, 1, 'low', analog=True) #Pasa bajas normalizado
b2, a2 = signal.butter(N, Corte, 'high', analog=True)     # HPF
s1= ss.tf(b, a) 
s2 = ss.tf(b2, a2) 
print('Desired Butterworth HPF H2(s)=', s1) 
mag, phase, omega1=ss.freqresp(s1, omega1)
plt.figure(1),plt.plot(omega1,np.abs(mag)),plt.xlabel('$\Omega$-->'),
plt.ylabel('$|H(j\Omega)|$'),plt.title('Magnitude response of Normalized LPF') 
mag2, phase2, omega2=ss.freqresp(s2, omega1)
plt.figure(1),plt.plot(omega1,np.abs(mag2)),plt.xlabel('$\Omega$-->'),
plt.ylabel('$|H(j\Omega)|$'),plt.title('Magnitude response of pasa altas HPF') 
plt.show()