import numpy as np
import matplotlib.pyplot as plt
# Rango de n
n = np.arange(-10, 11)
# Señal compleja x[n] = e^(jπ/4 * n)
x=np.exp(1j * np.pi/8 * n)
y=np.exp(1j * np.pi/8 * n)*np.exp(-1j * np.pi/8 * n)
#Extraer partes real e imaginaria grafica 1
x_real = np.real(x)
x_imag = np.imag(x)
#Extraer partes real e imaginaria grafica 2
y_real = np.real(y)
y_imag = np.imag(y)
# --- Graficar ---
plt.figure(figsize=(10, 8))
# Parte real
plt.subplot(4, 1, 1)
plt.stem(n, x_real)
plt.title("Parte real: Re{x[n]} = cos(πn/8)")
plt.xlabel("n")
plt.ylabel("Amplitud")
plt.grid(True)
# Parte imaginaria
plt.subplot(4, 1, 2)
plt.stem(n, x_imag)
plt.title("Parte imaginaria: Im{x[n]} = sin(πn/8)")
plt.xlabel("n")
plt.ylabel("Amplitud")
plt.grid(True)
plt.tight_layout()
# Parte real en y
plt.subplot(4, 1, 3)
plt.stem(n, y_real)
plt.title("Parte real: Re{y[n]} = cos(πn/8)")
plt.xlabel("n")
plt.ylabel("Amplitud")
plt.grid(True)
# Parte imaginaria y
plt.subplot(4, 1, 4)
plt.stem(n, y_imag)
plt.title("Parte imaginaria: Im{xyy[n]} = sin(πn/8)")
plt.xlabel("n")
plt.ylabel("Amplitud")
plt.grid(True)
plt.tight_layout()
plt.show()
