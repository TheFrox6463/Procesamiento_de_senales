import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import iirnotch, filtfilt

fs = 500  
t = np.linspace(0, 10, fs * 10)  
# ECG simulado
ecg_clean = 0.6 * np.sin(2 * np.pi * 1.3 * t)          
ecg_clean += 1.0 * np.sin(2 * np.pi * 1.7 * t + 1.5)   
ecg_clean += 0.3 * np.sin(2 * np.pi * 0.5 * t + 0.5)   
interferencia = 0.3 * np.sin(2 * np.pi * 50 * t)
ecg_noisy = ecg_clean + interferencia
f0 = 50.0  
Q = 30.0  
b, a = iirnotch(f0, Q, fs)
ecg_filtered = filtfilt(b, a, ecg_noisy)
plt.figure(figsize=(12, 8))
plt.subplot(3, 1, 1)
plt.plot(t, ecg_clean, 'g')
plt.title('Señal ECG limpia (simulada)')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud')
plt.grid(True)
plt.subplot(3, 1, 2)
plt.plot(t, ecg_noisy, 'r')
plt.title('Señal ECG con interferencia de 50 Hz')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud')
plt.grid(True)
plt.subplot(3, 1, 3)
plt.plot(t, ecg_filtered, 'b')
plt.title('Señal ECG filtrada (Notch aplicado)')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud')
plt.grid(True)

plt.tight_layout()
plt.show()
