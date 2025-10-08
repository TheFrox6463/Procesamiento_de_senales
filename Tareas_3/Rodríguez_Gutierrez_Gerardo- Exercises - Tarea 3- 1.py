import numpy as np
import matplotlib.pyplot as plt

# Definir el rango de n
n = np.arange(-5, 6)

# Función delta (impulso unitario)
def delta(n, index): #Dedine la funcion delta  equivalente a "delta"[n - index]
    #Lo que pedia el ejercicio
    return np.where(n == index, 1, 0)

# Generar las secuencias
x1 = delta(n, -1) + delta(n, 1)
x2 = delta(n, -1) - delta(n, 1)
x3 = delta(n, 0) + 2*delta(n, 1) + delta(n, 2)
x4 = delta(n, 0) - delta(n, 1) + delta(n, 2)

# Crear los subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Graficar cada secuencia en su respectivo subplot
#axs sirve para dividirlo en cuadriculas es como usar subploats pero de manera más simple
axs[0, 0].stem(n, x1)
axs[0, 0].set_title(r"$x_1[n] = \delta[n+1] + \delta[n-1]$")
axs[0, 1].stem(n, x2)
axs[0, 1].set_title(r"$x_2[n] = \delta[n+1] - \delta[n-1]$")
axs[1, 0].stem(n, x3)
axs[1, 0].set_title(r"$x_3[n] = \delta[n] + 2\delta[n-1] + \delta[n-2]$")
axs[1, 1].stem(n, x4)
axs[1, 1].set_title(r"$x_4[n] = \delta[n] - \delta[n-1] + \delta[n-2]$")

# Ajustar el espacio entre los subplots
plt.tight_layout()
plt.show()
