import numpy as np
import matplotlib.pyplot as plt

# Definir el rango de n
n = np.arange(-10, 11)

# Función escalón unitario u[n]
def u(n):
    return np.where(n >= 0, 1, 0)

# Función delta (impulso unitario)
def delta(n):
    return np.where(n == 0, 1, 0)
# Generar las secuencias
x1 = u(n)-u(n -5)
x2 = delta(n)
x3 = u(n+5) - u(n-5)
x4 = np.where((n >= 0) & (n <= 5), n, 0)
# Gráficas
plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)
plt.stem(n, x1, basefmt=" ")
plt.title('$x_1[n] = u[n] - u[n-5]$')
plt.grid(True)

plt.subplot(2, 2, 2)
plt.stem(n, x2, basefmt=" ")
plt.title('$x_2[n] = \delta[n]$')
plt.grid(True)

plt.subplot(2, 2, 3)
plt.stem(n, x3, basefmt=" ")
plt.title('$x_3[n] = u[n+5] - u[n-5]$')
plt.grid(True)

plt.subplot(2, 2, 4)
plt.stem(n, x4, basefmt=" ")
plt.title('$x_4[n] = n \\, \\text{para} \\, 0 \\leq n \\leq 5$')
plt.grid(True)

plt.tight_layout()
plt.show()