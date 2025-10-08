import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

# 1. Leer los archivos de audio
fs_m, male = wavfile.read('Hombre.wav')
fs_f, female = wavfile.read('Mujer.wav')

# Asegurarse de que ambas señales tengan la misma frecuencia de muestreo
if fs_m != fs_f:
    raise ValueError("Las frecuencias de muestreo no coinciden")

# Usar un solo canal si son estéreo
if male.ndim == 2:
    male = male[:, 0]
if female.ndim == 2:
    female = female[:, 0]

# Normalizar
male = male / np.max(np.abs(male))
female = female / np.max(np.abs(female))

# Asegurar que ambas señales tengan la misma longitud para comparación
min_len = min(len(male), len(female))
male = male[:min_len]
female = female[:min_len]

# (a) Autocorrelación de la voz masculina
auto_male = np.correlate(male, male, mode='full')
lags = np.arange(-len(male)+1, len(male))

# (b) Autocorrelación de la voz femenina
auto_female = np.correlate(female, female, mode='full')

# (c) Correlación cruzada: masculino con femenino
cross_mf = np.correlate(male, female, mode='full')

# (d) Correlación cruzada: femenino con masculino
cross_fm = np.correlate(female, male, mode='full')

# Visualización
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.plot(lags, auto_male)
plt.title('(a) Autocorrelación - Voz masculina')
plt.xlabel('Retraso (lag)')
plt.grid()

plt.subplot(2, 2, 2)
plt.plot(lags, auto_female)
plt.title('(b) Autocorrelación - Voz femenina')
plt.xlabel('Retraso (lag)')
plt.grid()

plt.subplot(2, 2, 3)
plt.plot(lags, cross_mf)
plt.title('(c) Correlación cruzada: masculino vs femenino')
plt.xlabel('Retraso (lag)')
plt.grid()

plt.subplot(2, 2, 4)
plt.plot(lags, cross_fm)
plt.title('(d) Correlación cruzada: femenino vs masculino')
plt.xlabel('Retraso (lag)')
plt.grid()

plt.tight_layout()
plt.show()
