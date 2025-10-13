import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz
# Definir la respuesta al impulso de h1[n] y h2[n]
# h1[n] = u[n] (escalón unitario)
h1 = np.ones(50)  # Respuesta al impulso de u[n], de longitud 50
# h2[n] = delta[n] - delta[n-1] (diferencia)
h2 = np.array([1, -1] + [0] * 48)  # Respuesta al impulso de h2[n]
# Convolución de los dos sistemas (en cascada)
h_cascade = np.convolve(h1, h2)
# Calcular la respuesta en frecuencia de la cascada
w, H = freqz(h_cascade, worN=8000)
# Magnitud y fase
magnitude = np.abs(H)
phase = np.angle(H)

# Graficar la magnitud y la fase
plt.figure(figsize=(12, 6))

# Magnitud
plt.subplot(2, 1, 1)
plt.plot(w / np.pi, magnitude, 'b')
plt.title('Magnitud de la respuesta en frecuencia')
plt.xlabel('Frecuencia normalizada (π rad/muestra)')
plt.ylabel('Magnitud')
plt.grid()

# Fase
plt.subplot(2, 1, 2)
plt.plot(w / np.pi, phase, 'r')
plt.title('Fase de la respuesta en frecuencia')
plt.xlabel('Frecuencia normalizada (π rad/muestra)')
plt.ylabel('Fase (radianes)')
plt.grid()

plt.tight_layout()
plt.show()
