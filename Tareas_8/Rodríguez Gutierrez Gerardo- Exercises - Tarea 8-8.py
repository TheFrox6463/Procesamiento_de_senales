import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import control as ss
#Del libro pagina 360
# Specifications of Filter
fsam=8000 # Sampling frequency in Hz
fc1,fc2=[1000,2000],[800,2500] 
Ap, As, T = 3, 40, 1/fsam
wp1 = 2*np.pi*fc1[0]
wp2 = 2*np.pi*fc1[1]
ws1 = 2*np.pi*fc2[0]
ws2 = 2*np.pi*fc2[1]
wp1a = (2/T)*np.tan(wp1*T/2)
wp2a = (2/T)*np.tan(wp2*T/2)
ws1a = (2/T)*np.tan(ws1*T/2)
ws2a = (2/T)*np.tan(ws2*T/2)
N,wn=signal.cheb2ord([wp1a,wp2],[ws1a,ws2a],Ap,As,analog=True)
print('Order of the filter (N) = ',N)
# Design analog Chebyshev Type 2 filter using signal.cheby2 function
b, a = signal.cheby2(N, As, wn, 'bandstop', analog='True')
s1 = ss.tf(b,a)
print('Transfer function H(s)=',s1)
# Perform bilinear transformation
bz, az = signal.bilinear(b, a, fs=fsam)
z1 = ss.tf(bz,az,T)
print('Transfer function H(z)=',z1)
# Compute frequency response of the filter using signal.freqz function
wz, hz = signal.freqz(bz, az, 512)
fig = plt.figure(figsize=(10, 8))
Mag = 10*np.log10(abs(hz)) # Calculate Magnitude in dB
Freq = wz*fsam/(2*np.pi) # Calculate frequency in Hz
# Plot Magnitude response
sub1 = plt.subplot(2, 1, 1)
sub1.plot(Freq, Mag, 'r', linewidth=2),sub1.axis([1, fsam/2, -60, 5])
sub1.set_title('Magnitude Response', fontsize=15),
sub1.set_xlabel('Frequency [Hz]', fontsize=15),sub1.set_ylabel('Magnitude [dB]', fontsize=15)
sub1.grid()
# Plot phase angle
sub2 = plt.subplot(2, 1, 2)
Phase = np.unwrap(np.angle(hz))*180/np.pi # Calculate phase angle in degree from hz
sub2.plot(Freq, Phase, 'g', linewidth=2),sub2.set_ylabel('Phase (degree)', fontsize=15)
sub2.set_xlabel(r'Frequency (Hz)', fontsize=15),sub2.set_title(r'Phase response', fontsize=15)
sub2.grid(),plt.subplots_adjust(hspace=0.5),fig.tight_layout(),plt.show() 