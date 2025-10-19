import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import sounddevice as sd
#Lector de archivos de audio
fs_m, audio = wavfile.read('Hola_buenas_tardes.wav')
# Normalizar
male = audio / np.max(np.abs(audio))
# Ahorc con el upsampling por L=2
upsample_factor = 2
upsampled = np.zeros(len(audio) * upsample_factor)
upsampled[::upsample_factor] = audio
fs_upsampled = fs_m * upsample_factor  # Nueva tasa de muestreo
#audio original
print("Reproduciendo audio original...")
sd.play(male, fs_m)
sd.wait()
#Audio con el downmsample
print("Reproduciendo audio downsampleado (factor 2)...")
sd.play(upsampled, fs_upsampled)
sd.wait()
# Grafica
plt.figure(figsize=(12, 5))
plt.subplot(2, 1, 1)
plt.plot(male)
plt.title('Audio Original')
plt.xlabel('Muestras')
plt.ylabel('Amplitud')
plt.subplot(2, 1, 2)
plt.plot(upsampled)
plt.title('Audio Downsampleado (factor 2)')
plt.xlabel('Muestras')
plt.ylabel('Amplitud')
plt.tight_layout()
plt.show()
#Comentario dinamico
#Rompe oidos, a comparacion del audio original este se escucha super saturado y es por las nuevos puntos que genera
#Tambien en la grafica se ve algo dificil de msotrar pero segun yo pasa eso 