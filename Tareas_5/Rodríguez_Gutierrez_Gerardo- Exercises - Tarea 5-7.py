#Generation of sine wave of different phase angles
import numpy as np
import matplotlib.pyplot as plt
# Parámetros
fs = 1000  
f = 5     
muestras = 100  
# Senal x[n] sin de 5 hz
n = np.arange(muestras)  
x = np.sin(2 * np.pi * f * n / fs)  
# # Senal x[n] cos de 5 hz
n2 = np.arange(muestras)  
x2 = np.cos(2 * np.pi * f * n2 / fs)  

# Extraer magnitudes y fases
magnitude_X = np.abs(x)
phase_X = np.angle(x)
magnitude_Y = np.abs(x2)
phase_Y = np.angle(x2)
X_prime_k = magnitude_X * np.exp(1j * phase_Y)  
Y_prime_k = magnitude_Y * np.exp(1j * phase_X)  
# Transformada Inversa de Fourier (IFFT)
x_prime_n = np.fft.ifft(X_prime_k) #fft es para aplicar la tranformada
y_prime_n = np.fft.ifft(Y_prime_k)

# Graficar las señales
plt.figure(figsize=(12, 8))

# Subplot para x[n] y y[n]
plt.subplot(2, 2, 1)
plt.plot(n, x, label='$x[n]$ (seno)', color='b')
plt.plot(n, x2, label='$y[n]$ (coseno)', color='g')
plt.title('Señales originales')
plt.xlabel('n')
plt.ylabel('Amplitud')
plt.legend()

# Subplot para x[n] y y[n] intercambiadas
plt.subplot(2, 2, 2)
plt.plot(n, np.real(x_prime_n), label='$x\'[n]$', color='b')
plt.plot(n, np.real(y_prime_n), label='$y\'[n]$', color='g')
plt.title('Señales con fases intercambiadas')
plt.xlabel('n')
plt.ylabel('Amplitud')
plt.legend()

# Subplot para la magnitud de X[k] y Y[k]
plt.subplot(2, 2, 3)
plt.plot(np.fft.fftfreq(100, 1/fs), magnitude_X, label='$|X[k]|$', color='b')
plt.plot(np.fft.fftfreq(100, 1/fs), magnitude_Y, label='$|Y[k]|$', color='g')
plt.title('Magnitudes de $X[k]$ y $Y[k]$')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Magnitud')
plt.legend()

# Subplot para las fases de X[k] y Y[k]
plt.subplot(2, 2, 4)
plt.plot(np.fft.fftfreq(100, 1/fs), phase_X, label='Fase de $X[k]$', color='b')
plt.plot(np.fft.fftfreq(100, 1/fs), phase_Y, label='Fase de $Y[k]$', color='g')
plt.title('Fases de $X[k]$ y $Y[k]$')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Fase (radianes)')
plt.legend()

plt.tight_layout()
plt.show()