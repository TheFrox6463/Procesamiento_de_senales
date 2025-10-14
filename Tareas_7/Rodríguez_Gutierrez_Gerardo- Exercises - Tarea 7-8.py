import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz
# Respuesta al impulso del filtro lowpass
h1 = np.array([0.159, 0.225, 0.25, 0.225, 0.159])
# Generar el filtro highpass usando h2[n] = (-1)^n * h1[n]
n = np.arange(len(h1))
h2 = ((-1)**n) * h1

# Obtener respuesta en frecuencia
w, H1 = freqz(h1, worN=8000)
w2, H2 = freqz(h2, worN=8000)

# Graficar respuestas en magnitud
plt.figure(figsize=(10, 5))
plt.plot(w, 20 * np.log10(np.abs(H1)), label='Filtro Pasa Bajas (h1[n])')
plt.plot(w, 20 * np.log10(np.abs(H2)), label='Filtro Pasa Altas (h2[n])', linestyle='--')
plt.title('Comparación de Magnitudes de Filtros')
plt.xlabel('Frecuencia (rad/muestra)')
plt.ylabel('Magnitud (dB)')
plt.grid()
plt.legend()
plt.tight_layout()
plt.show()
#Comentario: lo que se peude ver es que refleja la senal origianl, tienen 
#mismas magnitudes y todo, solo que lo redleja.