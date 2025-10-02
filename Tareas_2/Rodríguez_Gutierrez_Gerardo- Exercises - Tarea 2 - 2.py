#Exercise 2-T2
#mid rise con un bit rate de 1,2 y 4
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
#Generamos la onda senoidal de con 5 hz de frecuencia 
t=np.linspace(0,1,100) #La garica va en el eje de las x desde 0 hasta 1, 
f=5
x=np.sin(2*np.pi*f*t)
#bit rates generados
br=[1,2,4]
#Parametros del cuantizador
DR=np.max(x)-np.min(x) #Dynamic range
#Bit rate 1
L=2**br[0] #Quantization level
q=DR/(L) #Quantization step size
#Obtenemos la señal cuantizada bit rate en 1 
y=np.sign(x)*q*(np.floor((abs(x)/q))+(1/2))
plt.figure(0+1)
plt.subplot(2,2,1),plt.plot(t,x,'b',t,y,'r'),plt.xlabel('Time'),plt.ylabel('Amplitude')
plt.legend(['Input signal','Quantized Signal'],loc='upper right')
plt.title('Quantization with b={}'.format(br[0]))
plt.tight_layout()
#Obtenemos la señal cuantizada bit rate en 2 
L=2**br[1] #Quantization level
q=DR/(L) #Quantization step size
y=np.sign(x)*q*(np.floor((abs(x)/q))+(1/2))
plt.figure(1+1)
plt.subplot(2,2,1),plt.plot(t,x,'b',t,y,'r'),plt.xlabel('Time'),plt.ylabel('Amplitude')
plt.legend(['Input signal','Quantized Signal'],loc='upper right')
plt.title('Quantization with b={}'.format(br[1]))
plt.tight_layout()
#Obtenemos la señal cuantizada bit rate en 4 
L=2**br[2] #Quantization level
q=DR/(L) #Quantization step size
y=np.sign(x)*q*(np.floor((abs(x)/q))+(1/2))
plt.figure(2+1)
plt.subplot(2,2,2),plt.plot(t,x,'b',t,y,'r'),plt.xlabel('Time'),plt.ylabel('Amplitude')
plt.legend(['Input signal','Quantized Signal'],loc='upper right')
plt.title('Quantization with b={}'.format(br[2]))
plt.tight_layout()
plt.show()