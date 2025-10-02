#Exercise 1-T2
#Aliasig in time domain
import numpy as np
import matplotlib.pyplot as plt
f=10 #Signal frequency... las veces que aparece la onda, osea 10 veces se toman en cuenta
fs=[25,100] #Sampling frequencies muestras por segundo
#primera senal de muestreo de 25 hz 
t=np.arange(0,1,1/fs[0])
x=np.sin(20*np.pi*f*t) + np.sin(50*np.pi*t*f)
plt.subplot(2,2,1)
plt.plot(t,x),plt.xlabel('Time'),plt.ylabel('Amplitude')
plt.title('$F_s={} $ Hz'.format(fs[0]))
plt.tight_layout()
#Segunda senal de muestreo  de 100hz 
t=np.arange(0,1,1/fs[1])
x=np.sin(20*np.pi*f*t) + np.sin(50*np.pi*t*f)
plt.subplot(2,2,2)
plt.plot(t,x),plt.xlabel('Time'),plt.ylabel('Amplitude')
plt.title('$F_s={} $ Hz'.format(fs[1]))
plt.tight_layout()
plt.show()