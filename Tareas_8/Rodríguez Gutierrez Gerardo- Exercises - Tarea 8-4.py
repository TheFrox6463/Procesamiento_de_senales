import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import control as ss 
#Datos
db=3
db2=30
frecuencia_corte=[100,10000]
atenuacion=[30,50,25000]
#Pasamos a radianes los cortes y la atenuacion
#corte1=2*np.pi*frecuencia_corte[0]
#corte2=2*np.pi*frecuencia_corte[1] 
#atenuacion1=2*np.pi*atenuacion[0] 
#atenuacion2=2*np.pi*atenuacion[1] 
#atenuacion3=2*np.pi*atenuacion[2]
wp = np.multiply(2*np.pi, frecuencia_corte)
ws = np.multiply(2*np.pi, atenuacion)
#Del libro 
fs=3000
b, a =  signal.buttord(wp, ws, db, db2, analog=True)
omega1 = np.linspace(0, 10, 250000)  
b2, a2 =  signal.butter(b, a, btype='bandpass', analog=True)
transfer=ss.tf(b2,a2)
mag, phase, omega1=ss.freqresp(transfer, omega1)
plt.figure(1),plt.plot(omega1,np.abs(mag)),plt.xlabel('$\Omega$-->'),
plt.ylabel('$|H(j\Omega)|$'),plt.title('Magnitude del filtro Butterworth') 
plt.show()