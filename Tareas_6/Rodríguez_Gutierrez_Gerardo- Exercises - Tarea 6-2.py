import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
from scipy.signal import iirnotch, lfilter

# Parámetros
fs = 44100  # Frecuencia de muestreo (ahora sí puede representar 1000 Hz)
t = np.linspace(0, 1, fs, endpoint=False)

# Tonos de 500, 1000 y 1500 Hz
f = [500, 1000, 1500]
x1 = np.sin(2 * np.pi * f[0] * t)
x2 = np.sin(2 * np.pi * f[1] * t)
x3 = np.sin(2 * np.pi * f[2] * t)

# Concatenar las señales
senal_junta = np.concatenate([x1, x2, x3])

# Filtro Notch para eliminar 1000 Hz
freq_objetivo = 1000
Q = 30
w0 = freq_objetivo / (fs / 2)  # Normalización
b, a = iirnotch(w0, Q)

# Aplicar el filtro
senal_filtrada = lfilter(b, a, senal_junta)

# Graficar
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(senal_junta[:2000])
plt.title('Señal Original (500, 1000, 1500 Hz)')
plt.subplot(2, 1, 2)
plt.plot(senal_filtrada[:2000], color='green')
plt.title('Señal Filtrada (Notch en 1000 Hz)')
plt.tight_layout()
plt.show()

# Escuchar audio
print("Reproduciendo señal original...")
sd.play(senal_junta, samplerate=fs)
sd.wait()

print("Reproduciendo señal filtrada...")
sd.play(senal_filtrada, samplerate=fs)
sd.wait()
# Se escucha mas limpia, si sirve el filtro 