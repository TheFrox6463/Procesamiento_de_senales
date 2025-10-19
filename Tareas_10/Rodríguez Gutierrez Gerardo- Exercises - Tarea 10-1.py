import numpy as np
import matplotlib.pyplot as plt

# Rango de n
n = np.arange(0, 11)

# Valores de M para probar
M_values = [1, 2, 3, 4]

# Crear una figura para graficar
plt.figure(figsize=(10, 8))
#Empeiza el ciclo for para representar la sumatoria
for i, M in enumerate(M_values):
    x_n = [] # Va a guardar los valores de muestreo de cada M por N
    for ni in n:
        suma = 0
        for k in range(M): #Las veces que lo recorre dependiendo del arreglo de M
            suma += np.exp(1j * 2 * np.pi * k * ni / M) #La representacion de la sumatoria 
        x_val = suma / M
        x_n.append(x_val)

    # Lo de siempre, sacamos la magnitud y fase 
    x_n = np.array(x_n)
    magnitude = np.abs(x_n)
    phase = np.angle(x_n)

    # Graficamos
    plt.subplot(len(M_values), 2, 2*i + 1)
    plt.stem(n, magnitude)
    plt.title(f' M = {M}')
    plt.xlabel('n')
    plt.ylabel('|x[n]|')
    plt.grid(True)
    plt.subplot(len(M_values), 2, 2*i + 2)
    plt.stem(n, phase)
    plt.title(f'Fase para M = {M}')
    plt.xlabel('n')
    plt.ylabel('Fase [rad]')
    plt.grid(True)

plt.tight_layout()
plt.show()
