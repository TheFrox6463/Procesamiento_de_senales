import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la señal
A = 2              # Amplitud
f = 10             # Frecuencia en Hz
phi = 0            # Fase
num_samples = 100  # Número de muestras
fs = 1000          # Frecuencia de muestreo en Hz

# Tiempo (en segundos)
t = np.arange(num_samples) / fs

# Señal sinusoidal
x = A * np.sin(2 * np.pi * f * t + phi)

# Graficar la señal
plt.plot(t, x)
plt.title("Señal Sinusoidal: A=2V, f=10Hz")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud (V)")
plt.grid(True)
plt.show()
