import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz
# Parámetros
N = 21  
fc = np.pi / 2  
M = N - 1 
omega = np.linspace(0, np.pi, N)  #
H = np.zeros(N)
H[omega <= fc] = 1 
h = np.fft.ifft(H).real 
# Grafica
w, h_freq = freqz(h, worN=8000)
plt.figure(figsize=(10, 6))
plt.plot(w / np.pi, abs(h_freq), 'b')
plt.title("Respuesta en magnitud del filtro FIR pasa bajo")
plt.xlabel('Frecuencia normalizada (xπ rad/muestra)')
plt.ylabel('Magnitud')
plt.grid(True)
plt.show()
