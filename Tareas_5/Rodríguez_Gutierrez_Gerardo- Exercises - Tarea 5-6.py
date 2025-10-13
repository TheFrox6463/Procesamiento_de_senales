import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
#DAtos
fs = 1000  
f0 = 5     
T = 1      
t = np.linspace(0, 1, 1000)
# Generar onda cuadrada
x = signal.square(2 * np.pi * f0 * t)
# Calcular el espectro (DFT)
X = np.fft.fft(x)
N = len(X)
freqs = np.fft.fftfreq(N, 1/fs)
# Tomar solo mitad positiva del espectro
X_mag = np.abs(X[:N//2])
freqs_pos = freqs[:N//2]
# Graficar
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.plot(t, x)
plt.title('Onda cuadrada de 5 Hz')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud')
plt.grid(True)
plt.subplot(1, 2, 2)
plt.plot(freqs_pos, X_mag)
plt.title('Espectro de magnitud')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('|X(f)|')
plt.grid(True)

plt.tight_layout()
plt.show()
