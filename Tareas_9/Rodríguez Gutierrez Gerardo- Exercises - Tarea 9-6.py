#Es la combinacion del codigo 4 y 5 
import numpy as np
import matplotlib.pyplot as plt
N =input("Ingresa el bit: ")
valor_Equidistante=int(input("\nValor equidistante: "))
if valor_Equidistante<0:
    valor_Equidistante=valor_Equidistante-1
val_max=valor_Equidistante
val_min=valor_Equidistante*-1
x = np.linspace(val_max, val_min, 1000)
#Cuantizador, dependiendo de N
step_size = (val_max - val_min) / (int(N) - 1)
quantized = np.round((x - val_max) / step_size) * step_size + val_max
#Lo truncado 
Q = 1/(2**(int(N)))
Qht=Q*np.trunc(x/Q)#2's Complement truncation
print("Valores truncados", Qht)
# Graficar la curva de cuantización
plt.figure(figsize=(8, 5))
plt.plot(x, Qht, label="Quantizacion de lo Truncado)", color='blue')
plt.plot(x, x, linestyle='--', color='gray', label='Ideal (y = x)')
plt.title("Quantizacion Caracteristica de la Curva  Truncada")
plt.xlabel("Input")
plt.ylabel("Quantized Output")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()