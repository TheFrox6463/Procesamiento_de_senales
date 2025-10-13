#Generation of sine wave of different phase angles
import numpy as np
import matplotlib.pyplot as plt
# Parámetros
fs = 1000  
f = 5     
muestras = 100  
padding=50
# Senal x[n]
n = np.arange(muestras)  
x = np.sin(2 * np.pi * f * n / fs)  
# Senal x[n] con el aumento de 50 
n2 = np.arange(muestras+padding)  
x2 = np.sin(2 * np.pi * f * n2 / fs)  

# Realizar el Zero Padding, añadiendo 50 ceros al final
y = np.concatenate([x, np.zeros(50)])

# Calcular la FFT para ambas señales
X = np.fft.fft(x)
X2 = np.fft.fft(x2)
Y = np.fft.fft(y)

# Calcular el eje de frecuencias
frequencies_x = np.fft.fftfreq(len(x), 1/fs)
frequencies_x2 = np.fft.fftfreq(len(x2), 1/fs)
frequencies_y = np.fft.fftfreq(len(y), 1/fs)

# Graficar el espectro de la señal original x[n] y la señal zero-padded y[n]
plt.figure(figsize=(12, 6))

# x[n]
plt.subplot(3, 1, 1)
plt.plot(frequencies_x[:len(x)//2], np.abs(X)[:len(x)//2])  
plt.title(' x[n] (5 Hz)')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Magnitud')
plt.grid(True)
# x[n] mas el pading 
plt.subplot(3, 1, 2)
plt.plot(frequencies_x2[:len(x2)//2], np.abs(X2)[:len(x2)//2])  
plt.title('x[n]con padding')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Magnitud')
plt.grid(True)
# y[n] 
plt.subplot(3, 1, 3)
plt.plot(frequencies_y[:len(y)//2], np.abs(Y)[:len(y)//2])  
plt.title(' y[n] Zero Padding')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Magnitud')
plt.grid(True)

plt.tight_layout()
plt.show()