#Two-channel filter bank
#Ejemplo tomado del libro pagina 422
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
#Functions to perform downsampling and upsampling
def downsample(x,M):
 y=x[::M]
 return(y)
def upsample(x,L):
 y=np.zeros(L*len(x))
 y[::L]=x
 return(y)
#Step 1: Define the filters
h0=np.array([0.5,0.5])
h1=np.array([0.5,-0.5])
g0=np.array([1,1])
g1=np.array([-1,1])
#Step 2: Generate the input signal
f,fs,N=5,100,256
T=1/fs
t=np.linspace(0,N*T,N)
x=np.square(2*np.pi*f*t)
#Step 3: Traversing the path
x1=signal.lfilter(h0,1,x)
x2=signal.lfilter(h1,1,x)
x3=downsample(x1,2)
x4=downsample(x2,2)
x4 = np.zeros_like(x4)
x5=upsample(x3,2)
x6=upsample(x4,2)
x7=signal.lfilter(g0,1,x5)
x8=signal.lfilter(g1,1,x6)
y=x7+x8
plt.plot(t,x,'b',t,y,'r--',linewidth=2),plt.legend(['Input','Output'],loc=4)
plt.xlabel('Time'),plt.ylabel('Amplitude'),plt.title('Input and Output signals')
plt.tight_layout() 
plt.show()