#Impulse response of ideal filter
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz
#Prametros
wc = np.pi / 4   # frecuencia de corte digital
N_values = [5, 7]  # longitudes del filtro
plt.figure(figsize=(10, 6))
for N in N_values:
    n = np.arange(N)
    M = (N - 1) / 2 
    h = np.sinc((wc/np.pi)*(n - M)) * (wc/np.pi) 
    w = np.ones(N)
    h_rect = h * w
    w_freq, H = freqz(h_rect, worN=1024)
    plt.plot(w_freq/np.pi, np.abs(H), label=f'N = {N}')
#Gráficas 
plt.title('Magnitud de la respuesta del filtro pasa-bajas (ventana rectangular)')
plt.xlabel('Frecuencia normalizada (ω/π)')
plt.ylabel('|H(e^{jω})|')
plt.legend()
plt.grid(True)
plt.show()
