import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lfilter
#Tras leer entendi que la grfica que sale es asi por que no se retroalimenta este ripo de filtro
#Por eso en un instante se llega a calmar

fir= np.array([0.25, 0.50, 1.00, 1.25])
def quantize(coeffs, bits):
    levels = 2 ** bits
    return np.round(coeffs * levels) / levels
# Cuantizar los coeficientes
bits = 4  # Cambia este valor para más o menos precisión
quantized_coeffs = quantize(fir, bits)
print("Coeficietnes originales: ", fir)
print("Coeficientes cuantificados: ", quantized_coeffs)
n = 50
x = np.zeros(n)
x[0] = 1  # Impulso
# Salida del filtro FIR cuantizado
y = lfilter(quantized_coeffs, [1.0], x)
# Graficar la salida
plt.figure(figsize=(8, 4))
plt.stem(y)
plt.title("Coeficientes del FIR")
plt.xlabel("Muestras")
plt.ylabel("Salidas")
plt.grid(True)
plt.tight_layout()
plt.show()
