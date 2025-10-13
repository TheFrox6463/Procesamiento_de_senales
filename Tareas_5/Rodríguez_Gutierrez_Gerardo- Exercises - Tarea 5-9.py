#Effect of window length of STFT
import numpy as np
import matplotlib.pyplot as plt
#Step1: Signal generation
fs=100
T,N=1/fs, 100
#Frequency components of the signal
f1,f2,f3=5, 0, 10
t1=np.linspace(0,N*T,N)
t=np.linspace(0,N*T,3*N)
x1=np.sin(2*np.pi*f1*t1)
x2=np.sin(2*np.pi*f2*t1)
x3=np.sin(2*np.pi*f3*t1)
x=np.concatenate([x1,x2,x3])
x[150:160]=2 #Discontinuity
#Step 2: Plotting the signal and its spectrogram
plt.subplot(2,2,1),plt.plot(t,x),plt.xlabel('t-->'),plt.ylabel('x(t)')
plt.title('Signal')
plt.subplot(2,2,2),plt.specgram(x, Fs=fs, NFFT=16, noverlap=1,window =None)
plt.xlabel('Time (t-->)'),plt.ylabel('Frequency ($\omega$-->)'),
plt.title('Window length=16')
plt.subplot(2,2,3),plt.specgram(x, Fs=fs, NFFT=32, noverlap=1,window =None)
plt.xlabel('Time (t-->)'),plt.ylabel('Frequency ($\omega$-->)'),
plt.title('Window length=32')
plt.subplot(2,2,4),plt.specgram(x, Fs=fs, NFFT=128, noverlap=1,window =None)
plt.xlabel('Time (t-->)'),plt.ylabel('Frequency ($\omega$-->)'),
plt.title('Window length=128')
plt.tight_layout() 
plt.show()