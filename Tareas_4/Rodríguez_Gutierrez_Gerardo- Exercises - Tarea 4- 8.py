import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lfilter
# Definimos la respuesta al impulso
h = [1, -1]
# Número de muestras
N = 10
# Entrada impulso δ[n]
delta = np.zeros(N)
delta[0] = 1
# Entrada escalón u[n]
step = np.ones(N)
# Respuesta al impulso del sistema
impulse_response = lfilter(h, [1], delta)
# Respuesta al escalón del sistema
step_response = lfilter(h, [1], step)
# Gráficas
plt.figure(figsize=(10, 6))
# Subplot 1: respuesta al impulso
plt.subplot(2, 1, 1)
plt.stem(np.arange(N), impulse_response)
plt.title('Respuesta al Impulso del Sistema (h[n] = δ[n] - δ[n-1])')
plt.xlabel('n')
plt.ylabel('h[n]')
plt.grid(True)

# Subplot 2: respuesta al escalón
plt.subplot(2, 1, 2)
plt.stem(np.arange(N), step_response)
plt.title('Respuesta al Escalón del Sistema')
plt.xlabel('n')
plt.ylabel('y[n]')
plt.grid(True)

plt.tight_layout()
plt.show()
