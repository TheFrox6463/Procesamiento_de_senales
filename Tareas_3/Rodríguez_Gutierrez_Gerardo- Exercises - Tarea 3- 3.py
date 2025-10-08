import numpy as np
import matplotlib.pyplot as plt
# Rango de n
n = np.arange(-10, 11)
# Señal compleja x[n] = e^(jπ/4 * n)
x = np.exp(1j * np.pi/4 * n)
# (a) Extraer partes real e imaginaria
x_real = np.real(x)
x_imag = np.imag(x)
# --- Graficar ---
plt.figure(figsize=(10, 8))
# Parte real
plt.subplot(3, 1, 1)
plt.stem(n, x_real)
plt.title("Parte real: Re{x[n]} = cos(πn/4)")
plt.xlabel("n")
plt.ylabel("Amplitud")
plt.grid(True)
# Parte imaginaria
plt.subplot(3, 1, 2)
plt.stem(n, x_imag)
plt.title("Parte imaginaria: Im{x[n]} = sin(πn/4)")
plt.xlabel("n")
plt.ylabel("Amplitud")
plt.grid(True)
plt.tight_layout()
plt.show()
