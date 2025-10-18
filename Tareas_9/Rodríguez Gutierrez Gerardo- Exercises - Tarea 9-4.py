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
plt.figure(figsize=(8, 5))
#plt.plot(x, quantized, label='Quantized Output', color='blue')
plt.plot(x, x, linestyle='--', color='gray', label='Ideal (y = x)')
plt.title('Quantization por rounding')
plt.ylabel('Quantized Output')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()