import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, freqz, tf2zpk, impulse
from scipy.signal import lti
# Datos
fs = 20000  
fp = 1000  
fsb = 4000  
rp = 0.25   
rs = 0.25   
wp = 2 * np.pi * fp / fs  
ws = 2 * np.pi * fsb / fs  
numtaps = 51  #Orden del filtro 
h = firwin(numtaps, wp, window="hamming", pass_zero="lowpass")
# Respuesta en frecuencia
w, h_freq = freqz(h, worN=8000, fs=fs)
# Respuesta al impulso
t_impulse = np.arange(0, numtaps)
# Polos y ceros del filtro
b, a = np.array([h]), np.array([1])  # Numerador y denominador del filtro
z, p, k = tf2zpk(b, a)  # Cálculo de polos, ceros y ganancia

# Graficamos todo en un solo gráfico
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Respuesta en magnitud
axs[0, 0].plot(w, abs(h_freq), 'b')
axs[0, 0].set_title("Respuesta en Magnitud")
axs[0, 0].set_xlabel("Frecuencia [Hz]")
axs[0, 0].set_ylabel("Magnitud")
axs[0, 0].grid()

# Respuesta de fase
axs[0, 1].plot(w, np.angle(h_freq), 'b')
axs[0, 1].set_title("Respuesta de Fase")
axs[0, 1].set_xlabel("Frecuencia [Hz]")
axs[0, 1].set_ylabel("Fase [radianes]")
axs[0, 1].grid()

# Respuesta al impulso
axs[1, 0].stem(t_impulse, h, basefmt=" ")
axs[1, 0].set_title("Respuesta al Impulso")
axs[1, 0].set_xlabel("Muestras")
axs[1, 0].set_ylabel("Amplitud")
axs[1, 0].grid()

# Polos y ceros
# Dibuja el círculo unitario
theta = np.linspace(0, 2 * np.pi, 100)
x = np.cos(theta)
y = np.sin(theta)
axs[1, 1].plot(x, y, 'r--', label='Círculo Unitario')
axs[1, 1].scatter(np.real(z), np.imag(z), marker='o', label="Ceros")
axs[1, 1].scatter(np.real(p), np.imag(p), marker='x', label="Polos")
axs[1, 1].set_title("Gráfico de Polos y Ceros")
axs[1, 1].set_xlabel("Parte Real")
axs[1, 1].set_ylabel("Parte Imaginaria")
axs[1, 1].legend()
axs[1, 1].grid()

plt.tight_layout()
plt.show()
