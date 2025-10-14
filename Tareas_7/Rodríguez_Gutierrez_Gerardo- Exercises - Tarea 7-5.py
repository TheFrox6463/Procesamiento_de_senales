import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Datos necesarios
fs = 50  # Frecuencia de muestreo (mayor que 10 Hz para evitar aliasing)
t = np.arange(0, 1, 1/fs)  # 1 segundo de duración, frecuencia de muestreo fs

x1_frec = 5  # 5 Hz
x2_frec = 10  # 10 Hz
frec_corte = 8  # 8 Hz

# Crear las señales
x1 = np.sin(2 * np.pi * x1_frec * t)  # Señal de 5 Hz
x2 = np.sin(2 * np.pi * x2_frec * t)  # Señal de 10 Hz

# Señal de entrada x(t) es la suma de x1 y x2
X_f = x1 + x2

# Parámetros del filtro pasa alto
order = 10  # Orden del filtro
nyquist = 0.5 * fs  # Frecuencia de Nyquist
normalized_cutoff = frec_corte / nyquist  # Normalización de la frecuencia de corte

# Diseñar el filtro pasa alto usando la función butter
b, a = signal.butter(order, normalized_cutoff, btype='high', analog=False)

# Filtrar la señal
x_filtered = signal.filtfilt(b, a, X_f)

# Graficar la señal de entrada y la señal filtrada
plt.figure(figsize=(10, 6))

# Señal de entrada
plt.subplot(2, 1, 1)
plt.plot(t, X_f, label='Señal de entrada x(t)', color='blue')
plt.title('Señal de entrada x(t)')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud')
plt.grid(True)

# Señal filtrada
plt.subplot(2, 1, 2)
plt.plot(t, x_filtered, label='Señal filtrada', color='red')
plt.title('Señal filtrada (pasa alto)')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud')
plt.grid(True)

plt.tight_layout()
plt.show()
 #Comentario, se ve que la senal la trata de hacer mas como una onda senoidal con este filtro. 