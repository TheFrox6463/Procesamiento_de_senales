import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
#Hacemos una senal senoidal que pase primero que pase 
#Por el muestreo upsampling y luego por el downsampling
#Datos
fs=1000
t=np.arange(0,1,1/fs)
f= 5
x= np.sin(2*np.pi*f*t)
N=5
# El factor que se usara para los 2 tipos de muestreo 
#Downsampling
M=2
x_down = x[::M]
#upsampling
L=2 #No especifica cuanto debe de ser, supongamos 2 
y = np.zeros(L * len(x_down))
y[::L]=x_down
#Grafica
plt.figure(figsize=(10,4))
plt.subplot(2,1,1)
plt.stem(np.arange(len(x)), x, linefmt='C0-', markerfmt='C0o', basefmt=" ", label='x[n]')
plt.title("Señal original x[n]")
plt.xlabel("n")
plt.ylabel("Amplitud")
plt.grid(True)
plt.legend()
plt.subplot(2,1,2)
plt.stem(np.arange(len(y)), y, linefmt='C1-', markerfmt='C1s', basefmt=" ", label='y[n]')
plt.title("Señal de salida y[n] después de up y down")
plt.xlabel("n")
plt.ylabel("Amplitud")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()