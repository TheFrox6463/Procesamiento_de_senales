#Linearity property of DFT
import numpy as np
import matplotlib.pyplot as plt
x1=np.array([1,1,1,1])
x2=np.array([1,-1,1,-1])
#Calcular DFT usando FFT
X1 = np.fft.fft(x1)
X2 = np.fft.fft(x2)
#Calcular magnitud 
mag_X1 = np.abs(X1)
mag_X2 = np.abs(X2)
#La frecuencia
N = len(x1)
k = np.arange(N)
# Graficar la magnitud y la fase
plt.figure(figsize=(10, 6))
# Magnitud x1
plt.subplot(2, 1, 1)
plt.stem(k , mag_X1)
plt.title('Magnitud de H(z)')
plt.xlabel('Frecuencia angular (rad/s)')
plt.ylabel('Magnitud |H(e^jw)|')
plt.grid(True)
# Magnitud x2
plt.subplot(2, 1, 2)
plt.stem(k , mag_X2)
plt.title('Magnitud de H(z)')
plt.xlabel('Frecuencia angular (rad/s)')
plt.ylabel('Magnitud |H(e^jw)|')
plt.grid(True)
plt.show()