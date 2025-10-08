import numpy as np
import matplotlib.pyplot as plt

# Definir el eje del tiempo (simétrico para poder verificar la paridad)
t = np.linspace(-10, 10, 1000)

# Definir dos señales pares (por ejemplo: coseno y una función cuadrada)
x1 = np.cos(t)       # coseno es par
x2 = 1 / (1 + t**2)  # esta también es una función par
# Producto de las dos señales
y = x1 * x2
#Senales impares para una senal par 
x3 = np.sin(t)       # coseno es par
x4 = t / (1 + t**2)  # esta también es una función par
y2 = x3 * x4
#Senal par por una impar
x5 = np.sin(t)       # coseno es par
x6 = np.cos(t)  # esta también es una función par
y3 = x5 * x6
# Verificación visual
plt.plot(t, y, label='Producto x1(t) * x2(t)', color='blue')
plt.plot(-t, y, '--', label='Reflejo: y(-t)', color='red')
plt.title('Producto de dos señales pares')
plt.xlabel('Tiempo t')
plt.ylabel('Amplitud')
plt.legend()
plt.grid(True)
plt.show()
plt.plot(t, y2, label='Producto x1(t) * x2(t)', color='blue')
plt.plot(-t, y2, '--', label='Reflejo: y(-t)', color='red')
plt.title('Producto de dos señales pares')
plt.xlabel('Tiempo t')
plt.ylabel('Amplitud')
plt.legend()
plt.grid(True)
plt.show()
plt.plot(t, y3, label='Producto x1(t) * x2(t)', color='blue')
plt.plot(-t, y3, '--', label='Reflejo: y(-t)', color='red')
plt.title('Producto de dos señales pares')
plt.xlabel('Tiempo t')
plt.ylabel('Amplitud')
plt.legend()
plt.grid(True)
plt.show()

