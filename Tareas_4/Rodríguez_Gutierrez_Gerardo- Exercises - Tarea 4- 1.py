import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lfilter

# Parámetros del sistema
b = [1, 0]  # Coeficientes de la entrada (x[n] + 0*x[n-1])
a = [1, -0.5]  # Coeficientes de la salida (y[n] - 0.5*y[n-1])

# Generar la secuencia de impulsos (delta[n])
n = np.arange(0, 20)  # Tiempo discreto
x = np.zeros_like(n)
x[0] = 1  # Impulso unitario

# Calcular la respuesta al impulso utilizando lfilter
y = lfilter(b, a, x)

# Graficar la respuesta al impulso
plt.stem(n, y)
plt.title("Respuesta al impulso del sistema")
plt.xlabel("n")
plt.ylabel("y[n]")
plt.grid(True)
plt.show()
