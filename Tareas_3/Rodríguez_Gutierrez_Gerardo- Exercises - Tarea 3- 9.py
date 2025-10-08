import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

# 1. Leer archivo de audio (usa tu propio archivo aquí)
fs, signal = wavfile.read('record_out (1).wav')

# Asegurarse de trabajar con una sola canal (si es estéreo)
if len(signal.shape) == 2:
    signal = signal[:, 0]

# Normalizar señal (opcional, pero recomendado)
signal = signal / np.max(np.abs(signal))

# 2. Calcular la autocorrelación
autocorr = np.correlate(signal, signal, mode='full')

# Generar eje de tiempo para la autocorrelación
lags = np.arange(-len(signal) + 1, len(signal))

# 3. Verificar si la autocorrelación es par (simétrica)
is_even = np.allclose(autocorr, autocorr[::-1])
print(f"La función de autocorrelación es par: {is_even}")

# 4. Graficar la autocorrelación
plt.figure(figsize=(10, 4))
plt.plot(lags, autocorr)
plt.title('Autocorrelación de la señal de voz')
plt.xlabel('Retraso (lag)')
plt.ylabel('Autocorrelación')
plt.grid()
plt.show()