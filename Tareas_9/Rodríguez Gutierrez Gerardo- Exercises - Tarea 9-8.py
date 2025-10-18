# This program performs quantization using Magnitude truncation
import numpy as np
import matplotlib.pyplot as plt
#Del libro pag 382
h=float(input('Enter the value to be Quantized: '));
B=int(input('Enter the Number of Bits (N): '));
Q = 1/(2**(B))
def magnitude_truncation(x, Q):
    if x > 0:
        return Q * np.floor(x / Q)
    else:
        return Q * np.ceil(x / Q)
#print('The input unquantized value : ',h)
#print('The Quantized result using Magnitude truncation: ', Qhmt)
def simulate_system(truncate=False):
    N = 100  # número de pasos
    x = np.zeros(N)
    x[0] = 1.0  # condición inicial
    for n in range(1, N):
        x[n] = 0.95 * x[n-1]  # sistema con realimentación (simula oscilaciones amortiguadas)  
        if truncate:
            x[n] = magnitude_truncation(x[n], Q)
    return x
#Simulacion
x_no_trunc = simulate_system(truncate=False)
x_trunc = simulate_system(truncate=True)
# Gráficas
plt.figure(figsize=(10, 5))
plt.plot(x_no_trunc, label='Sin truncamiento', linestyle='--')
plt.plot(x_trunc, label='Con truncamiento de magnitud', linestyle='-')
plt.title('Comparación de sistema con y sin truncamiento de magnitud')
plt.xlabel('Tiempo (pasos)')
plt.ylabel('Valor del sistema')
plt.legend()
plt.grid(True)
plt.show()