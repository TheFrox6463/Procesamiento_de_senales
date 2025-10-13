#Ejercicio 5
import numpy as np
import matplotlib.pyplot as plt

# Definir señal de entrada x[n]
n = np.arange(-10, 11)
x = np.sin(0.3 * np.pi * n)  # señal de prueba

# Definir el sistema: y[n] = x[n/2]
def system(x, n):
    y = np.zeros_like(x)
    for i in range(len(n)):
        val = n[i] / 2
        # Buscar el índice correspondiente si existe
        if val in n:
            y[i] = x[np.where(n == val)[0][0]]
        else:
            y[i] = 0
    return y

# --- Verificación de linealidad ---
x1 = np.sin(0.3 * np.pi * n)
x2 = np.cos(0.3 * np.pi * n)
a, b = 2, 3

# Propiedad lineal: a*x1 + b*x2 → a*y1 + b*y2
y1 = system(x1, n)
y2 = system(x2, n)
lhs = system(a*x1 + b*x2, n)  # lado izquierdo (entrada combinada)
rhs = a*y1 + b*y2             # lado derecho (salida combinada)

# --- Verificación de invariancia temporal ---
k = 2  # desplazamiento
x_shifted = np.roll(x, k)
y_original = system(x, n)
y_shifted_input = system(x_shifted, n)
y_output_shifted = np.roll(y_original, k)

# --- Resultados ---
plt.figure(figsize=(10, 8))

# Linealidad
plt.subplot(2, 1, 1)
plt.stem(n, lhs - rhs)
plt.title("Verificación de Linealidad (lhs - rhs)")
plt.xlabel('n')
plt.ylabel('Diferencia')
plt.grid(True)

# Invariancia temporal
plt.subplot(2, 1, 2)
plt.stem(n, y_shifted_input - y_output_shifted)
plt.title("Verificación de Invariancia Temporal (y_shifted_input - y_output_shifted)")
plt.xlabel('n')
plt.ylabel('Diferencia')
plt.grid(True)

plt.tight_layout()
plt.show()