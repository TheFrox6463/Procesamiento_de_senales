#Illustration of upsampling operation
#Del libor pagina 410
import numpy as np
import matplotlib.pyplot as plt
#Step 1: Generation of input signal x[n]
N=2
n=np.arange(N)
x=np.array([1,2])
#Step 2: Upsampling the input signal
n0 = 1  # desplazamiento en el tiempo
x_shifted = np.roll(x, n0)
x_shifted[:n0] = 0
#Upsampling
L=2
y=np.zeros(L*N)
y[::L]=x
# #Step 3: Plotting the results
upsampled_then_shifted = np.roll(y, L * n0)
upsampled_then_shifted[:L * n0] = 0
def upsample(x, L):
    y = np.zeros(L * len(x))
    y[::L] = x
    return y

upsampled_x = upsample(x, L)
upsampled_shifted = upsample(x_shifted, L)
n_upsampled = np.arange(len(y))
n1=np.arange(L*N)
plt.figure(figsize=(10, 6))
plt.subplot(3,1,1)
plt.stem(n_upsampled, upsampled_shifted)
plt.title("Upsample 1")

plt.subplot(3,1,2)
plt.stem(n_upsampled, upsampled_then_shifted)
plt.title("Upsample 2 por L·n₀")

plt.subplot(3,1,3)
plt.stem(n_upsampled, upsampled_shifted - upsampled_then_shifted)
plt.title("Diferencia (debería ser ≠ 0 si es time-varying)")

plt.tight_layout()
plt.show()