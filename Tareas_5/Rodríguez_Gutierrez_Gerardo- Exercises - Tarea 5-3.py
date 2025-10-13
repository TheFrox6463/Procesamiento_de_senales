import numpy as np
import matplotlib.pyplot as plt
# Definir la función de transferencia H(z)
def H(z):
    return 1 / (1 - z**-1)
# Definir la frecuencia
W = np.linspace(-np.pi, np.pi, 400)
# calcular la respuesta en frecuencia 
z = np.exp(1j * W)  # z = e^(jω)
H_z = H(z)
# Calcular la magnitud y fase
magnitude = np.abs(H_z)
phase = np.angle(H_z)
# Graficar la magnitud y la fase
plt.figure(figsize=(10, 6))
# Magnitud
plt.subplot(2, 1, 1)
plt.plot(W, magnitude)
plt.title('Magnitud de H(z)')
plt.xlabel('Frecuencia angular (rad/s)')
plt.ylabel('Magnitud |H(e^jw)|')
plt.grid(True)
# Fase
plt.subplot(2, 1, 2)
plt.plot(W, phase)
plt.title('Fase de H(z)')
plt.xlabel('Frecuencia angular (rad/s)')
plt.ylabel('Fase ∠H(e^jw)')
plt.grid(True)

# Mostrar las gráficas
plt.tight_layout()
plt.show()
