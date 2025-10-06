import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
#Senal senoidal
f=1300 #Frequency of sine wave
fs=8000 #Muestreo
duracion=1
#tiempo
t = np.linspace(0, duracion, int(f * duracion))
#Senal
x=np.sin(2*np.pi*f*t)
#Generamos una senal de muestreo
t2=np.arange(0,1,1/fs)
#Senal original de muestreo
x_example=np.sin(2*np.pi*f*t2)
# Escala relativa de las notas (aproximada en razón de frecuencias)
print("Reproduciendo señal original (1300 Hz @ 8 kHz)...")
sd.play(x, samplerate=fs)
sd.wait()
signal_downsampled = x[::2]
fs_downsampled = fs // 2  # Nueva frecuencia de muestreo: 4000 Hz
# Reproducir tono submuestreado
print("Reproduciendo señal submuestreada (1300 Hz @ 4 kHz)...")
sd.play(signal_downsampled, samplerate=fs_downsampled)
sd.wait()
