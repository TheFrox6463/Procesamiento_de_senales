#Characteristics of bandpass filter
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
#Step 1: Desired impulse response hd[n]
N,omega_1,omega_2 = 7,np.pi*0.15,np.pi*0.45 #longitud, corte 1, corte 2 
n = np.arange(0,N)
rect_win=np.ones(N)
hd =(omega_1/np.pi * np.sinc((n-(N-1)/2)*omega_1/np.pi))+np.sinc(n-(N-1)/2)-(omega_2/np.pi *
np.sinc((n-(N-1)/2)*omega_2/np.pi))
h=signal.firwin(N,omega_1,window='hamming',pass_zero=True) 
w,H=signal.freqz(h) #Step 3: Frequency response of ideal filter
#Step 4:Impulse response of the filter
plt.subplot(2,2,1),plt.stem(n,h),plt.xlabel('n-->'),plt.ylabel('Amplitude'),plt.title('h[n]')
z, p, k = signal.tf2zpk(h,1)#Step 5: Pole-zero plot of the filter
theta = np.linspace(0, np.pi*2, 500)
circle = np.exp(1j*theta)
plt.subplot(2,2,2),plt.plot(circle.real, circle.imag, 'k--')
plt.plot(z.real, z.imag, 'ro', ms=7.5),plt.plot(p.real, p.imag, 'rx')
plt.xlabel('$\sigma$'),plt.ylabel('$j\omega$'),plt.title('Pole-zero plot')
#Step 6: Magnitude response of the filter
plt.subplot(2,2,3),plt.plot(w,20*np.log10(np.abs(H))),plt.xlabel('$\omega$-->'),
plt.ylabel('$|H(e^{j^\omega})|$'),plt.title('Magnitude response')
#Step 7: Phase response of the filter
plt.subplot(2,2,4),plt.plot(w,np.unwrap(np.angle(H))),plt.xlabel('$\omega$-->'),
plt.ylabel('$\phi(e^{j^\omega})$'),plt.title('Phase response'),plt.tight_layout() 
plt.show()