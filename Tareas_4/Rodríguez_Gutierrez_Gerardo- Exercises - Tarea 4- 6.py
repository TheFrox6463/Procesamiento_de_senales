import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import TransferFunction, zpk2tf

# H1(z)
numerador_1 = [-2]  # La única raíz del numerador
denominador_1 = []  # No hay polos
H1 = TransferFunction([1, 1/2], [1], dt=1)  # Coeficientes de numerador y denominador

# Sistema 2: H2(z)
numerador_2 = []  # No hay ceros
denominador_2 = [1/3]  # Polo en z = 1/3
H2 = TransferFunction([1], [1, -1/3], dt=1)

# Sistema 3: H3(z)
numerador_3 = [-1/2]  # La raíz del numerador
denominador_3 = [1/3]  # El polo en el denominador
H3 = TransferFunction([1, 1/2], [1, -1/3], dt=1)

#Grafica
def plot_pz(zeros, poles, system_label):
   
    plt.scatter(np.real(zeros), np.imag(zeros), color='red', label='Ceros')
    plt.scatter(np.real(poles), np.imag(poles), color='blue', label='Polos')
    plt.axhline(0, color='black',linewidth=1)
    plt.axvline(0, color='black',linewidth=1)
    plt.title(f'Pole-Zero Plot of {system_label}')
    plt.xlabel('Re')
    plt.ylabel('Im')
    plt.legend()
    plt.grid(True)

# Dibujar los diagramas de polos y ceros
plot_pz(numerador_1, numerador_1, 'H1(z)')
plot_pz(numerador_2, numerador_2, 'H2(z)')
plot_pz(numerador_3, numerador_3, 'H3(z)')

# Mostrar los gráficos
plt.show()