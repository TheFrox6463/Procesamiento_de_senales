#Problema 5: Genera una fuincion gausiana con los valores en u de =0,1,2, 4
#Generation of Gaussian function
import numpy as np
import matplotlib.pyplot as plt
t=np.linspace(-10,10,1000)
#Primero de 0.01
k=1/np.sqrt(2*np.pi*1)
x=k*np.exp(-np.power(t-0,2.)/2*np.power(1,2.))
plt.subplot(2,2,1),plt.plot(t,x),plt.xlabel('Time'),
plt.ylabel('Amplitude'),plt.title('$\sigma={} $'.format(1))
plt.tight_layout()
#Segundo de 0.5
k=1/np.sqrt(2*np.pi*1)
x=k*np.exp(-np.power(t-1,2.)/2*np.power(1,2.))
plt.subplot(2,2,2),plt.plot(t,x),plt.xlabel('Time a'),
plt.ylabel('Amplitude'),plt.title('$\sigma={} $'.format(1))
plt.tight_layout()
#Tercero de 1
k=1/np.sqrt(2*np.pi*1)
x=k*np.exp(-np.power(t-2,2.)/2*np.power(1,2.))
plt.subplot(2,2,3),plt.plot(t,x),plt.xlabel('Time'),
plt.ylabel('Amplitude'),plt.title('$\sigma={} $'.format(1))
plt.tight_layout()
#Cuarto de 10
k=1/np.sqrt(2*np.pi*1)
x=k*np.exp(-np.power(t-4,2.)/2*np.power(1,2.))
plt.subplot(2,2,4),plt.plot(t,x),plt.xlabel('Time'),
plt.ylabel('Amplitude'),plt.title('$\sigma={} $'.format(1))
plt.tight_layout()
plt.show()