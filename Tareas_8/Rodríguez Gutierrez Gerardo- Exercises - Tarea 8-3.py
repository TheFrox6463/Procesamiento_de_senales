import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import control as ss 
#Ejemplo del libro, filtro butterworth, datos del ejercicio
db=-3
frecuencia_corte=20
db2=-10
atenuacion=40
num1=10**(-db/10)-1
num2=10**(-db2/10)-1
num=np.log(num1/num2)
den=2*np.log(frecuencia_corte/atenuacion)
N=np.ceil(num/den)
print('Order of the filter (N) =',N) 
#para la magnitud 
omega1 = np.linspace(0, 10, 100)  
b, a = signal.butter(N, 1, 'low', analog=True) #Pasa bajas normalizado
s1= ss.tf(b, a) 
mag, phase, omega1=ss.freqresp(s1, omega1)
plt.figure(1),plt.plot(omega1,np.abs(mag)),plt.xlabel('$\Omega$-->'),
plt.ylabel('$|H(j\Omega)|$'),plt.title('Magnitude response of Normalized LPF') 
plt.show()