import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz, tf2zpk
import scipy.signal as signal
# Parámetros
N = 9
wc = 4  # radianes/muestra
M = (N - 1) // 2  # punto central de la ventana
n = np.arange(N)
# Filtro ideal paso bajo (sinc modificado)
h_lp = np.sinc((n - M) * wc / np.pi / np.pi)
# Ajustar por la frecuencia de corte (sinc normalizada)
h_lp = np.sin(wc * (n - M)) / (np.pi * (n - M + 1e-10))  # evitar división por cero
h_lp[M] = wc / np.pi  # corrección en el punto central
# Convertir a filtro paso alto
delta = np.zeros(N)
delta[M] = 1  # impulso unitario en el centro
h_hp = delta - h_lp
# Aplicar ventana de Bartlett
bartlett = 1 - (2 * np.abs(n - M)) / (N - 1)
h_hp_windowed = h_hp * bartlett
# Mostrar respuesta en frecuencia
w, H = freqz(h_hp_windowed, worN=8000)
plt.figure(figsize=(10, 4))
plt.plot(w, 20 * np.log10(np.abs(H)))
plt.title('Magnitud de la respuesta en frecuencia (dB)')
plt.xlabel('Frecuencia [rad/muestra]')
plt.ylabel('Magnitud [dB]')
plt.grid()
plt.tight_layout()
plt.show()
# Diagrama polo-cero
b = h_hp_windowed
a = [1]  # FIR: solo ceros
z, p, k = tf2zpk(b, a)
plt.figure(figsize=(6, 6))
plt.plot(np.real(z), np.imag(z), 'o', label='Ceros')
plt.plot(np.real(p), np.imag(p), 'x', label='Polos')
unit_circle = plt.Circle((0, 0), 1, color='black', fill=False, linestyle='--')
plt.gca().add_artist(unit_circle)
plt.axhline(0, color='gray', linestyle='--')
plt.axvline(0, color='gray', linestyle='--')
plt.title('Diagrama Polo-Cero del filtro')
plt.xlabel('Re')
plt.ylabel('Im')
plt.legend()
plt.grid()
plt.axis('equal')
plt.tight_layout()
plt.show()
