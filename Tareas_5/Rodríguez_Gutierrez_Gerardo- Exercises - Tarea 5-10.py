#Discontinuity detection using CWT
import pywt
import numpy as np
import matplotlib.pyplot as plt
#Step 1: Signal generation
#t=np.linspace(0,1,200)
t=np.arange(0,200,1)
x=np.sin(2*np.pi*5*t/len(t))
x[90]=10
#Step 2: CWT of the signal
scale=np.arange(1,5)
coef,freqs=pywt.cwt(x,scale,'gaus1')
plt.subplot(2,1,1),plt.plot(t,x),plt.xlabel('t-->'),plt.ylabel('x(t)')
plt.title('Signal with discontinuity')
#Step 3: Plotting the reslt
plt.subplot(2,1,2),
plt.imshow(abs(coef),extent=[0,200,30,1],interpolation='bilinear',cmap='winter',
 aspect='auto',vmax=abs(coef).max(),vmin=-abs(coef).max())
plt.gca().invert_yaxis()
plt.xticks(np.arange(0,201,20))
plt.xlabel('Time (t-->)'),plt.ylabel('Freq Scale ($\omega$-->)'),
plt.title('CWT of the signal')
plt.tight_layout()
plt.show() 