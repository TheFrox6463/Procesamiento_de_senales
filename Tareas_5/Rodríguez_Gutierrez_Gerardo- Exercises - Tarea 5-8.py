import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import chirp, spectrogram

# Parámetros
fs = 1000       
t = np.linspace(0, 10, fs * 10)  
f0 = 10         
f1 = 1          

# Generar chirp lineal 
x = chirp(t, f0=f0, f1=f1, t1=10, method='linear')
# Calcular la FFT para ver el espectro
N = len(x)
X = np.fft.fft(x)
freqs = np.fft.fftfreq(N, 1/fs)
# Solo mitad positiva
freqs_pos = freqs[:N//2]
X_mag = np.abs(X[:N//2])
# Calcular espectrograma
f, tt, Sxx = spectrogram(x, fs=fs, nperseg=256, noverlap=128)
#Grafica
plt.figure(figsize=(12, 6))

# Señal en el tiempo
plt.subplot(3, 1, 1)
plt.plot(t, x)
plt.title("Chirp lineal (frecuencia de 10 Hz a 1 Hz en 10 s)")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.grid(True)

# Espectro (magnitud de la FFT)
plt.subplot(3, 1, 2)
plt.plot(freqs_pos, X_mag)
plt.title("Espectro de magnitud del chirp")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("|X(f)|")
plt.grid(True)

# Espectrograma (frecuencia vs tiempo)
plt.subplot(3, 1, 3)
plt.pcolormesh(tt, f, 10 * np.log10(Sxx), shading='gouraud')
plt.title("Espectrograma del chirp lineal")
plt.ylabel("Frecuencia [Hz]")
plt.xlabel("Tiempo [s]")
plt.colorbar(label='Potencia [dB]')

plt.tight_layout()
plt.show()
