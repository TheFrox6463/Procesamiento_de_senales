#Problema 2: Generacion de una onda senoidal con los paremaetros de Amplitud de 1 V, frecuencia de 5Hz y con una fase de 0 
#Marca el punto más alto de cada onda con una X
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
#Step 1: Defining the independent variable
t=np.linspace(0,1,100) #La garica va en el eje de las x desde 0 hasta 1, 
#El numero final nos dice cuantas muestras van a ir en ese tramo
#Step 2: Defining the parameters of sine wave
A=1 #Amplitude of sine wave
f=10 #Frequency of sine wave
ph=0 #Phase of sine wave
#Step 3: Expression of sine wave
x=A*np.sin(2*np.pi*f*t+ph)
#Buscamos el argumento con el calor mas alto con np.argmax(x)
peaks, _ = find_peaks(x)     # índice del máximo
t_max = t[peaks]         # tiempo correspondiente
x_max = x[peaks]         # valor máximo
#Step 4: Plotting the sine wave
plt.plot(t,x),plt.xlabel('Time'),plt.ylabel('Amplitude')
plt.scatter(t_max, x_max, color="red", zorder=5)  # marca en el punto máximo
plt.title('A={}V,F={} Hz,$\phi={}^\circ$'.format(A,f,ph))
plt.show()
