import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la señal
f = 10             # Frecuencia de la señal (Hz)
fs = 1000          # Frecuencia de muestreo (Hz)
t = np.arange(0, 0.1, 1/fs)   # Tiempo (0.1 segundos para visualizar bien)
x = np.sin(2*np.pi*f*t)       # Señal senoidal de 10 Hz
# Parámetros del cuantificador
n_bits = 4                   # Número de bits
L = 2**n_bits                # Niveles de cuantificación
x_min, x_max = -1, 1         # Rango de la señal
delta = (x_max - x_min) / L  # Paso de cuantificación
# Cuantificación uniforme
xq = np.round((x - x_min) / delta) * delta + x_min
# Error de cuantificación
error = xq - x
# Gráficas
plt.figure(figsize=(12,8))
plt.subplot(3,1,1)
plt.plot(t, x, label='Señal Original', color='blue')
plt.title('Señal de entrada (10 Hz)')
plt.ylabel('Amplitud')
plt.grid(True)
plt.subplot(3,1,2)
plt.plot(t, xq, label='Señal Cuantificada', color='orange')
plt.title('Señal Cuantificada (4 bits)')
plt.ylabel('Amplitud')
plt.grid(True)
plt.tight_layout()
plt.show()