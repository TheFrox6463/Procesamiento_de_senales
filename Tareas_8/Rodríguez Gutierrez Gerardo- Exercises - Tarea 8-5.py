import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import control as ss 
#Datos
db=3
db2=10
frecuencia_corte=250
frecuencia_res=500
muestras=1000
T=1/muestras
#Corte en radianes
Corte = 2 * np.pi * frecuencia_corte
Corte2 = 2 * np.pi * frecuencia_res
#Con esto es lo del orden del filtro
b, a =  signal.buttord(Corte, Corte2, db, db2, analog=True)
b2, a2 =  signal.butter(b, a, btype='low', analog=True)
transfer=ss.tf(b2,a2)
yd = transfer.sample(T, method='backward_diff') 
#Parte invariante
t_imp, h_imp = signal.impulse((b2, a2), T=np.arange(0, 1, T))
bz = h_imp
az = [1.0]  # FIR
# Obtener respuesta en frecuencia del filtro digital
w, h_freq = signal.freqz(bz, az, worN=1024, fs=1000)
# Graficar la respuesta en frecuencia
plt.figure(figsize=(8, 5))
plt.plot(w, 20 * np.log10(np.abs(h_freq)), label='Magnitud |H(f)|')
plt.axvline(frecuencia_corte, color='green', linestyle='--', label='Frecuencia de corte (250 Hz)')
plt.axvline(frecuencia_res, color='red', linestyle='--', label='Frecuencia de rechazo (500 Hz)')
plt.title('Respuesta en frecuencia del filtro Butterworth (Invariancia de impulso)')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Magnitud (dB)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()