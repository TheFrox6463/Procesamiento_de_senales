#Ejercicio 4: reproduce las 7 notas 
import numpy as np
import sounddevice as sd

# Frecuencia base (Sa)
Sa = 240.0  # Hz

# Escala relativa de las notas (aproximada en razón de frecuencias)
ratios = {
    "Sa": 1.0,         # Sa
    "Re": 9/8,         # Re
    "Ga": 5/4,         # Ga
    "Ma": 4/3,         # Ma
    "Pa": 3/2,         # Pa
    "Dha": 5/3,        # Dha
    "Ni": 15/8         # Ni
}

# Duración y muestreo
duration = 1.0  # segundos
fs = 44100      # frecuencia de muestreo

# Generar cada nota y reproducirla
for note, ratio in ratios.items():
    freq = Sa * ratio
    t = np.linspace(0, duration, int(fs * duration), endpoint=False)
    wave = 0.5 * np.sin(2 * np.pi * freq * t)  # señal senoidal
    print(f"Playing {note} ({freq:.2f} Hz)")
    sd.play(wave, fs)
    sd.wait()  # esperar a que termine antes de la siguiente