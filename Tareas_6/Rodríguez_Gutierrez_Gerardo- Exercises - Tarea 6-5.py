import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import iirnotch, filtfilt
from scipy.fft import fft, fftfreq
#Datos
fs = 500      
t = np.linspace(0, 1, 1000) 
f1 = 5    
f2 = 10   
x1 = np.sin(2 * np.pi * f1 * t)    
x2 = np.sin(2 * np.pi * f2 * t)    
x = x1 + x2                         
f0 = 5.0     
Q = 30.0     
b, a = iirnotch(f0, Q, fs)
y = filtfilt(b, a, x)
def spectrum(signal, fs):
    N = len(signal)
    freqs = fftfreq(N, 1/fs)
    mag = np.abs(fft(signal)) / N
    return freqs[:N//2], mag[:N//2]

freq_x, mag_x = spectrum(x, fs)
freq_y, mag_y = spectrum(y, fs)
#Graficar 
plt.figure(figsize=(12, 8))
plt.subplot(3, 1, 1)
plt.plot(t, x)
plt.title("Señal original: 5 Hz + 10 Hz")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.grid(True)
plt.subplot(3, 1, 2)
plt.plot(t, y, color='orange')
plt.title("Señal filtrada (componente de 5 Hz eliminada)")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.grid(True)
plt.subplot(3, 1, 3)
plt.plot(freq_x, mag_x, label='Antes del filtro')
plt.plot(freq_y, mag_y, label='Después del filtro', color='red')
plt.title("Espectro de magnitud")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("|X(f)|")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
