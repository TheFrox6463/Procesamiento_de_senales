import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import square, freqz, filtfilt
#Senal cuadrada
fs = 1000          
f0 = 10             
t = np.linspace(0, 1, 1000)
x = square(2 * np.pi * f0 * t)
 # número de muestras de retardo (para 10 Hz)
N = int(fs / f0)  
b = np.array([1] + [0]*(N-1) + [-1])  
a = [1]                                 
y = filtfilt(b, a, x)  
def spectrum(signal, fs):
    N = len(signal)
    freqs = np.fft.fftfreq(N, 1/fs)
    mag = np.abs(np.fft.fft(signal)) / N
    return freqs[:N//2], mag[:N//2]
freq_x, mag_x = spectrum(x, fs)
freq_y, mag_y = spectrum(y, fs)
# Graficar
plt.figure(figsize=(12, 8))
plt.subplot(3, 1, 1)
plt.plot(t, x)
plt.title("Onda cuadrada de 10 Hz (entrada)")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.grid(True)
plt.subplot(3, 1, 2)
plt.plot(t, y, color='orange')
plt.title("Señal después del filtro peine (10 Hz y armónicos eliminados)")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.grid(True)
plt.subplot(3, 1, 3)
plt.plot(freq_x, mag_x, label='Original')
plt.plot(freq_y, mag_y, label='Filtrada', color='red')
plt.title("Espectro de magnitud")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("|X(f)|")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
