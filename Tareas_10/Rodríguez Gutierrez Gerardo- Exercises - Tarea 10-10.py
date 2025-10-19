import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import scipy.io.wavfile as wav
from scipy import signal
#Datos
fs = 8000  
duration = 2  
#Normalizamos los audios
fs0, x0 = wav.read("Yes.wav")
fs1, x1 = wav.read("No.wav")
# Aplanar las señales
x0 = x0.flatten()
x1 = x1.flatten()
#En esta parte se supone que se aplica el banco de pruebas para el ejercicio
# Filtros de análisis
h0 = np.array([0.5, 0.5])
h1 = np.array([0.5, -0.5])
# Filtros de síntesis
g0 = np.array([1, 1])
g1 = np.array([-1, 1])
# Si no me equivoco aplicamos lo del banco de pruebas para al final aplicar lo del transmultiplexer
def downsample(x, M):
    return x[::M]
def upsample(x, L):
    y = np.zeros(L * len(x))
    y[::L] = x
    return y
#Transmultiplexor
x0_filtered = signal.lfilter(h0, 1, x0)
x1_filtered = signal.lfilter(h1, 1, x1)
# Downsampling
d0 = downsample(x0_filtered, 2)
d1 = downsample(x1_filtered, 2)
# Multiplexado: combinación de señales
mux_signal = d0 + d1
# Separación: asumir conocemos d0 y d1 (sin canal de transmisión real)
# En la práctica: se usarían filtros selectivos para separar mux_signal
# Upsampling
u0 = upsample(d0, 2)
u1 = upsample(d1, 2)
# Filtros de síntesis
y0 = signal.lfilter(g0, 1, u0)  # Reconstrucción de x0 (YES)
y1 = signal.lfilter(g1, 1, u1)  # Reconstrucción de x1 (NO)
#Normalizar y guardar
y0 = y0 / np.max(np.abs(y0))
y1 = y1 / np.max(np.abs(y1))
# Guardar como archivos de audio
wav.write("y0_output_yes.wav", fs, y0.astype(np.float32))
wav.write("y1_output_no.wav", fs, y1.astype(np.float32))
#Reproducir los resultado
print("Reproduciendo salida y0 (YES)...")
sd.play(y0, fs)
sd.wait()
print("Reproduciendo salida y1 (NO)...")
sd.play(y1, fs)
sd.wait()
print("Fin del procesamiento")
#Me espante
#Comentario dinamico
#Creo que al estar separando las 2 señales y al hacer un muestreo para cada audio al final recontruye cada audio pero no salen iguales a como 
#Es el audio origial de cada archivo, la teoria dice que se debe de recontruir la senal pero no se si de manera exacta