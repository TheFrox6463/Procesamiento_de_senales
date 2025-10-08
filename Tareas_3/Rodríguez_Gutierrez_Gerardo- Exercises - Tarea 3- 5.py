import numpy as np
import matplotlib.pyplot as plt

# Definir el rango de n
n = np.arange(-2, 10)

# Función delta (impulso unitario)
def delta(n, index): #Dedine la funcion delta  equivalente a "delta"[n - index]
    #Lo que pedia el ejercicio
    return np.where(n == index, 1, 0)

# Generar las secuencias
x1 = delta(n,0) + delta(n, 1) + delta(n, 2)+ delta(n, 3) + delta(n, 4) + delta(n, 5) + delta(n, 6)+ delta(n, 7)
x2 = delta(n,0) - delta(n, 1) + delta(n, 2)- delta(n, 3) + delta(n, 4) - delta(n, 5) + delta(n, 6)- delta(n, 7)
x3 = delta(n,0) + delta(n, 1) - delta(n, 2)- delta(n, 3) + delta(n, 4) + delta(n, 5) - delta(n, 6)- delta(n, 7)
x4 = delta(n,0) + delta(n, 1) + delta(n, 2)+ delta(n, 3) - delta(n, 4) - delta(n, 5) - delta(n, 6)- delta(n, 7)

#Calculamos la energía
E1 = np.sum(np.abs(x1)**2)
E2 = np.sum(np.abs(x2)**2)
E3 = np.sum(np.abs(x3)**2)
E4 = np.sum(np.abs(x4)**2) 
#Resultados de la sumatorai
print(f"Energía de x1[n]: {E1}")
print(f"Energía de x2[n]: {E2}")
print(f"Energía de x3[n]: {E3}")
print(f"Energía de x4[n]: {E4}")
# Crear los subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 8))
# Graficar cada secuencia en su respectivo subplot
#axs sirve para dividirlo en cuadriculas es como usar subploats pero de manera más simple
axs[0, 0].stem(n, x1)
axs[0, 0].set_title(r"$x_1[n]")
axs[0, 1].stem(n, x2)
axs[0, 1].set_title(r"$x_2[n]")
axs[1, 0].stem(n, x3)
axs[1, 0].set_title(r"$x_3[n]")
axs[1, 1].stem(n, x4)
axs[1, 1].set_title(r"$x_4[n] ")
# Ajustar el espacio entre los subplots
plt.tight_layout()
plt.show()