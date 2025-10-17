import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import control as ss
#Del libro pagina 363
N, rp,rs, omega_c=2, 3, 40, [10]
omega1=np.linspace(0, 10, 100)
b_s, a_s=signal.ellip(N,rp,rs,omega_c,'low', analog=True)
s1 = ss.tf(b_s, a_s)
print('H(s) = ', s1)
z1=np.roots(b_s)
print('Zeros : ', z1)
mag, phase, omega1=ss.freqresp(s1, omega1)
plt.figure,plt.plot(omega1,np.abs(mag))
plt.xlabel('$\u03A9$-->'),plt.ylabel('$|H({j\u03A9})|$')
plt.title('Magnitude response of Elliptic LPF')
plt.tight_layout() 
plt.show()