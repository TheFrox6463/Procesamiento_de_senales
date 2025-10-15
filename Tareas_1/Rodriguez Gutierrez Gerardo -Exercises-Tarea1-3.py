#Problema 3: Generacion de una onda senoidal con los paremaetros de Amplitud de 1 V, frecuencia de 5Hz y con una fase de 0 
#Marca el punto más alto de cada onda con una X
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
#Step 1: Defining the independent variable
t=np.linspace(0,1,100) #La garica va en el eje de las x desde 0 hasta 1, 
#El numero final nos dice cuantas muestras van a ir en ese tramo
#Step 2: Defining the parameters of sine wave
A=2 #Amplitude of sine wave
f=5 #Frequency of sine wave
ph=0 #Phase of sine wave
#Step 3: Expression of sine wave
x=A*np.sin(2*np.pi*f*t+ph)
# Detectar cruces por cero
# np.sign(x) da -1 cuando x<0, 0 cuando x=0, +1 cuando x>0
signos = np.sign(x)
cambios = np.diff(signos)  # diferencias entre signos consecutivos

# Índices donde hay cruce (cuando cambia de signo)
zero_crossings = np.where(cambios != 0)[0]

# Coordenadas aproximadas de cruces
t_cross = t[zero_crossings]
x_cross = x[zero_crossings]
#Step 4: Plotting the sine wave
plt.plot(t, x, label="Señal senoidal")
plt.axhline(0, color="black", linestyle="--", linewidth=1)
plt.scatter(t_cross, x_cross, color="red", zorder=5, label="Cruces por cero")
plt.title('A={}V,F={} Hz,$\phi={}^\circ$'.format(A,f,ph))
plt.show()

#Cantidad de veces que pasa por 0 
print("Cruces por cero en 0 =", len(t_cross))
