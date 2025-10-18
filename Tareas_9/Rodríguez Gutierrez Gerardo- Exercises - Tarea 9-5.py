# This program performs quantization using 2’s complement truncation
#Del libro pagina 279
import numpy as np
import matplotlib.pyplot as plt
h=float(input('Enter the value to be Quantized: '))
B=int(input('Enter the Number of Bits (N): '))
Q = 1/(2**(B))
print('The input unquantized value : ',h)
#print('The Quantized result using Rounding: ', Qhr)
x = np.linspace(-h, h, 1000)
Qht=Q*np.floor(x/Q)#2's Complement truncation
print('The Quantized result using 2s Complement truncation: ', Qht)
#Es lo que se va desplazando con la truncacion
step_size = (h - (-1*h)) / (int(B) - 1)
quantized = np.round((x - h) / step_size) * step_size + h
plt.figure(figsize=(8, 5))
plt.plot(x, Qht, label="Quantized (Truncation)", color='blue')
plt.plot(x, x, linestyle='--', color='gray', label='Ideal (y = x)')
plt.title("Quantization Characteristics Curve (2's Complement Truncation)")
plt.xlabel("Input")
plt.ylabel("Quantized Output")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()