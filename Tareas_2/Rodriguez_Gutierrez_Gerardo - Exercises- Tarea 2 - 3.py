#Generation of sine wave of different phase angles
import numpy as np
import matplotlib.pyplot as plt
#Generation of cos wave "SENAL CONTINUA"
t=np.linspace(0,1,1000)
x=np.cos(2*np.pi*t)+np.cos(14*np.pi*t)+np.cos(18*np.pi*t)
#Generamos una senal de muestreo
fs=8
t2=np.arange(0,1,1/fs)
#Senal original de muestreo
x_example=np.cos(2*np.pi*t2)+np.cos(14*np.pi*t2)+np.cos(18*np.pi*t2)
#Senal de alineamiento
x2=3*np.cos(2*np.pi*t2)
#Dibujo
plt.subplot(2,2,1)
plt.plot(t,x),plt.xlabel('Time (t)'),plt.ylabel('Amplitude (V)')
plt.title('$\Phi ={}^\circ $'.format("0"))
plt.tight_layout()
#Plotting the result
plt.subplot(2,2,2)
plt.plot(t2,x2),plt.xlabel('Time (t)'),plt.ylabel('Amplitude (V)')
plt.title('$\Phi ={}^\circ $'.format("0"))
plt.tight_layout()
plt.subplot(2,2,3)
plt.plot(t,x),plt.xlabel('Time (t)'),plt.ylabel('Amplitude (V)')
plt.plot(t2,x2),plt.xlabel('Time (t)'),plt.ylabel('Amplitude (V)')
plt.title('$\Phi ={}^\circ $'.format("0"))
plt.tight_layout()
plt.subplot(2,2,4)
plt.plot(t, x, label='Señal original x(t)', color='blue')  # señal continua
plt.stem(t2, x_example, linefmt='g-', markerfmt='go', basefmt=' ', label='x(t) muestreada') #stem ayuda a marcar las lineas de los
plt.stem(t2, x2, linefmt='r--', markerfmt='ro', basefmt=' ', label="Señal aliasada $x'(t)$")# puntos de muestreo
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.title('Comparación de x(t) y $x\'(t)$ en instantes de muestreo')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()