import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import control as ss
#Del libro paginas  354
# Specifications of Filter
fsam=1000 # Sampling frequency
fp=250 # Passband frequency
fs=500 # Stopband frequency
Ap, As, Td=3,10,1/fsam   
wp=2*np.pi*(fp/fsam) # passband freq in radian per sample
ws=2*np.pi*(fs/fsam) # Stopband freq in radian per sample
# prewarping process
omega_p=(2/Td)*np.tan(wp/2)
omega_s=(2/Td)*np.tan(ws/2)
N, omega_c=signal.cheb1ord(omega_p,omega_s,Ap,As,analog=True)
print('Order of the Filter N =', N)
print('Cut-off frequency= {:.4f} rad/s'. format(omega_c))
# Computation of H(s)
b_s, a_s=signal.cheby1(N,Ap,omega_c,'low', analog=True)
s1 = ss.tf(b_s, a_s)
print('Transfer function H(s)=',s1)
bz, az=signal.bilinear(b_s, a_s, Td)
z1 = ss.tf(bz,az,Td)
print('Transfer function H(z)=',z1)
ws, hs = signal.freqz(bz, az) # Calculate Magnitude from hz in dB
Mag = 20*np.log10(abs(hs)) # Calculate phase angle in degree from hz
Phase = np.unwrap(np.arctan2(np.imag(hs), np.real(hs)))*(180/np.pi)
# Calculate frequency in Hz from wz
Freq = ws*fsam/(2*np.pi)
# Plot filter magnitude and phase responses using subplot.
fig = plt.figure(figsize=(10, 6))# Plot Magnitude response
sub1 = plt.subplot(2, 1, 1)
sub1.plot(Freq, Mag, 'r', linewidth=2)
sub1.axis([1, fsam/2, -100, 5])
sub1.set_title('Magnitude Response', fontsize=15)
sub1.set_xlabel('Frequency [Hz]', fontsize=15)
sub1.set_ylabel('Magnitude [dB]', fontsize=15)
sub1.grid()
# Plot phase angle
sub2 = plt.subplot(2, 1, 2)
sub2.plot(Freq, Phase, 'g', linewidth=2),sub2.set_ylabel('Phase (degree)', fontsize=15)
sub2.set_xlabel(r'Frequency (Hz)', fontsize=15)
sub2.set_title(r'Phase response', fontsize=15)
sub2.grid(),plt.subplots_adjust(hspace=0.5),fig.tight_layout(),plt.show() 