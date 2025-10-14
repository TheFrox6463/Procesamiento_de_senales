import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz
N = 7                   # longitud del filtro
wc = np.pi / 3          # frecuencia de corte
n = np.arange(N)
M = (N - 1) / 2         
#Filtro pasa bajas 
hd_lp = np.sinc((wc/np.pi)*(n - M)) * (wc/np.pi)
#Convertir a pasa-altas
delta = np.zeros(N)
delta[int(M)] = 1
hd_hp = delta - hd_lp
#ventana Bartlett 
w = np.bartlett(N)
h = hd_hp * w
#Respuesta en frecuencia
w_freq, H = freqz(h, worN=1024)
# Graficar
plt.figure(figsize=(12, 5))
# Magnitud
plt.subplot(1, 2, 1)
plt.plot(w_freq / np.pi, np.abs(H))
plt.title('Magnitud del filtro pasa-altas (Bartlett window)')
plt.xlabel('Frecuencia normalizada (ω/π)')
plt.ylabel('|H(e^{jω})|')
plt.grid(True)
# Fase
plt.subplot(1, 2, 2)
plt.plot(w_freq / np.pi, np.angle(H))
plt.title('Fase del filtro pasa-altas (Bartlett window)')
plt.xlabel('Frecuencia normalizada (ω/π)')
plt.ylabel('Fase (radianes)')
plt.grid(True)

plt.tight_layout()
plt.show()
