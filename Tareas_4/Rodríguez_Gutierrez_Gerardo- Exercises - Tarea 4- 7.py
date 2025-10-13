import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz

# Coeficientes del sistema (función de transferencia H(z))
b = [1/3, 1/3, 1/3]  # Numerador: coeficientes de x[n], x[n-1], x[n-2]
a = [1]  # Denominador: solo el coeficiente de x[n] (no hay polos)

# Frecuencia de muestreo (suponemos que es 1 para normalización)
w, h = freqz(b, a, worN=8000)

# Magnitud y fase
magnitude = np.abs(h)
phase = np.angle(h)

# Graficar la respuesta en magnitud
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(w / np.pi, magnitude, 'b')
plt.title('Magnitud de la respuesta del sistema')
plt.xlabel('Frecuencia normalizada [π rad/muestra]')
plt.ylabel('Magnitud')
plt.grid(True)

# Graficar la respuesta en fase
plt.subplot(2, 1, 2)
plt.plot(w / np.pi, phase, 'r')
plt.title('Fase de la respuesta del sistema')
plt.xlabel('Frecuencia normalizada [π rad/muestra]')
plt.ylabel('Fase [radianes]')
plt.grid(True)

plt.tight_layout()
plt.show()