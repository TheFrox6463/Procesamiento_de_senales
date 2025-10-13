import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
#Step 1: Defining the independent variable
t=np.linspace(0,1,1000) #La garica va en el eje de las x desde 0 hasta 1, 
#El numero final nos dice cuantas muestras van a ir en ese tramo
#Step 2: Defining the parameters of sine wave
f=5 #Frequency of sine wave
#Step 3: Expression of sine wave
x=np.sin(2*np.pi*f*t)
#Senal de ruido uniforme datos
duracion = 1.0        
fs = 1000         
N = int(duracion * fs)
# Rango del ruido uniforme
amplitud_min = -1.0
amplitud_max = 1.0
# Generar señal de ruido uniforme
ruido_uniforme = np.random.uniform(low=amplitud_min, high=amplitud_max, size=N)
#El filtro de media movil 
def filtro_media_movil(senal, N):
    return np.convolve(senal, np.ones(N)/N, mode='same')

senal_filtrada = filtro_media_movil(ruido_uniforme, N=50)
# Graficar 
#Seno
plt.figure(figsize=(12, 8))
plt.subplot(3, 1, 1)
plt.plot(t,x)  
plt.title('Senal senoidal')
plt.xlabel('tiempo')
plt.ylabel('Amplitud')
plt.grid(True)
#Ruido
plt.subplot(3, 1, 2)
plt.plot(ruido_uniforme[:1000])  
plt.title('Ruido Uniforme')
plt.xlabel('Muestra')
plt.ylabel('Amplitud')
plt.grid(True)
#Filtro 
plt.subplot(3, 1, 3)
plt.plot(t,senal_filtrada)  
plt.title('Ruido Uniforme')
plt.xlabel('Muestra')
plt.ylabel('Amplitud')
plt.grid(True)
plt.show()
#Lo visto en la grafica final es que se parece mucho más a una onda senoidal cuando se aplica el filtrop y se puede apreciar mejor como funciono el filtro 