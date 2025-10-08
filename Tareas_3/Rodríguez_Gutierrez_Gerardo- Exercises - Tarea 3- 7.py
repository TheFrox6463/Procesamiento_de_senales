import numpy as np
import matplotlib.pyplot as plt
# Rango de n
n = np.arange(-10, 11)
# Definir la señal x[n]
x = np.where(np.abs(n) <= 5, 5 - np.abs(n), 0)
# Parte par e impar
x_even = 0.5 * (x + x[::-1])   # x[-n] = x[::-1]
x_odd  = 0.5 * (x - x[::-1])
# Reconstrucción
x_reconstructed = x_even + x_odd
# --- Graficar ---
fig, axs = plt.subplots(4, 1, figsize=(8, 10))
axs[0].stem(n, x)
axs[0].set_title(r"")
axs[0].grid(True)
axs[1].stem(n)
axs[1].set_title("Even part of x[n]")
axs[1].grid(True)
axs[2].stem(n)
axs[2].set_title("Odd part of x[n]")
axs[2].grid(True)
axs[3].stem(n)
axs[3].set_title("Reconstructed signal xₑ[n] + xₒ[n]")
axs[3].grid(True)
plt.tight_layout()
plt.show()
# Verificación numérica
print("¿La reconstrucción es igual al original?:", np.allclose(x, x_reconstructed))
