import numpy as np
import matplotlib.pyplot as plt

# Rango de n
n = np.arange(-10, 11)

# Valores de alfa
alphas = [1/4, 3/4, 1, 2]

# Crear figura con subplots
plt.figure(figsize=(10, 8))

for i, alpha in enumerate(alphas, 1):
    h = np.power(float(alpha), n)   #Para los exponentes negativos ocupamos que declararlos como float
    plt.subplot(2, 2, i)  # 2 filas, 2 columnas, gráfico i
    plt.stem(n, h)
    plt.title(f'α = {alpha}')
    plt.xlabel('n')
    plt.ylabel('h[n]')
    plt.grid(True)

plt.tight_layout()
plt.show()