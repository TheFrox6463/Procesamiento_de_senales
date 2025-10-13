import numpy as np
import matplotlib.pyplot as plt

# Parámetros
fs = 100  # Frecuencia de muestreo (100 Hz)
f = 5  # Frecuencia de la señal de entrada (5 Hz)
n = np.arange(0, 100, 1)  # Tiempo discreto para 100 muestras

# Generar la señal de entrada (onda senoidal de 5 Hz)
x = np.sin(2 * np.pi * f * n / fs)

# Definir la respuesta al impulso de H1(z) = X(z^2)
# H1(z) es un filtro que aplica el cambio z^2, lo que puede ser interpretado como
# un retardo en la señal (pero para este caso lo simularemos como una operación
# de filtrado).
y1 = np.roll(x, 2)  # Desplazar la señal 2 pasos

# Definir la respuesta al impulso de H2(z) = 1/2 * (X(z^2) + X(z^-2))
# H2(z) es una combinación de desplazamientos positivos y negativos
y2 = 0.5 * (np.roll(x, 2) + np.roll(x, -2))  # Desplazamientos en ambas direcciones

# Resultado de la cascada (aplicar H1 seguido de H2)
output = y2

# Graficar las señales
plt.figure(figsize=(12, 8))

# Señal de entrada
plt.subplot(3, 1, 1)
plt.plot(n, x, label='Entrada', color='blue')
plt.title('Señal de Entrada (5 Hz)')
plt.xlabel('Muestras')
plt.ylabel('Amplitud')
plt.grid()

# Señal después de H1(z)
plt.subplot(3, 1, 2)
plt.plot(n, y1, label='Salida después de H1(z)', color='green')
plt.title('Salida después de H1(z)')
plt.xlabel('Muestras')
plt.ylabel('Amplitud')
plt.grid()

# Señal después de H2(z) (Salida final)
plt.subplot(3, 1, 3)
plt.plot(n, output, label='Salida después de H2(z)', color='red')
plt.title('Salida después de H2(z) (Sistema en Cascada)')
plt.xlabel('Muestras')
plt.ylabel('Amplitud')
plt.grid()

plt.tight_layout()
plt.show()
