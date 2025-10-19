import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import sounddevice as sd
#Lector de archivos de audio
fs_m, audio = wavfile.read('Hola_buenas_tardes.wav')
# Normalizar
male = audio / np.max(np.abs(audio))
# Downsamplear por un factor de 2
male_downsampled = male[::2]
fs_down = fs_m 
#audio original
print("Reproduciendo audio original...")
sd.play(male, fs_m)
sd.wait()
#Audio con el downmsample
print("Reproduciendo audio downsampleado (factor 2)...")
sd.play(male_downsampled, fs_down)
sd.wait()
# Grafica
plt.figure(figsize=(12, 5))
plt.subplot(2, 1, 1)
plt.plot(male)
plt.title('Audio Original')
plt.xlabel('Muestras')
plt.ylabel('Amplitud')
plt.subplot(2, 1, 2)
plt.plot(male_downsampled)
plt.title('Audio Downsampleado (factor 2)')
plt.xlabel('Muestras')
plt.ylabel('Amplitud')
plt.tight_layout()
plt.show()
#Comentario dinamico
#Al escuchart el audio suena mas chillona la base y me imagino por que es como recorta el audio por así decirlo con el dowsampling
#en la grafica no se aprecia muy bien el cambio pero las muestras en comparacion de la toam original si cambia en el eje de las x