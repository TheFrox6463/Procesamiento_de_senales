import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
# datos
f0 = 5.0          
fs = 1000.0        
N = 2          
t_total = 1.0      
#senal cuadrada
t = np.arange(0, t_total, 1/fs)
x = signal.square(2 * np.pi * f0 * t)
#Upsalmping
x_ds = x[::N]
fs_ds = fs / N
t_ds = t[::N]
# Espectros (FFT)
def compute_fft(x, fs):
    N = len(x)
    X = np.fft.rfft(x * np.hamming(N)) #Usa la combinacion de los 2 filtros fft y sfft en una sola linea de codigo y hace el muestreo en X
    f = np.fft.rfftfreq(N, 1/fs)
    mag_db = 20 * np.log10(np.abs(X) / (N/2) + 1e-12)
    return f, mag_db
f1, mag1 = compute_fft(x, fs) # Primero sacamos el muestreo de la senal cuadrada con la funcion que generamos 
f2, mag2 = compute_fft(x_ds, fs_ds) #despues ahora la senal con el upsampling apra ver las diferencias 
#Gráfica
plt.figure(figsize=(10, 4))
plt.plot(t[:500], x[:500], label="Original (fs = 1000 Hz)")
plt.stem(t_ds[:250], x_ds[:250], linefmt='C1-', markerfmt='C1o',
         basefmt=" ", label="Downsampled x[::2] (fs = 500 Hz)")
plt.title("Onda cuadrada 5 Hz y versión decimada")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
plt.figure(figsize=(10, 4))
plt.plot(f1, mag1, label="Original (fs = 1000 Hz)")
plt.plot(f2, mag2, label="Downsampled (fs = 500 Hz)")
plt.xlim(0, 200)
plt.ylim(-80, 20)
plt.title("Espectro de magnitud (FFT)")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Magnitud [dB]")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
#Comentario dinamico
#Como lo que vimos en la clase, al muestrear las 2 senales, la original y luego con el umplasing todo lo que sea muestreado despues con el umpsampling se 
#desplaza dependiendo del valor de L que en este caso es N y teniendo el mismo patron todo solo que desplazando un pelin en el eje de las X