import numpy as np
import matplotlib.pyplot as plt

# Valor de N
N = 31
n = np.arange(0, N)
# Ventana rectangular
rectangular_window = np.ones(N)
#Ventana de Bartlett window or Triangular window
Bartlett_triangular = 1-((2*np.abs(n)/N-1))
#Hamming window 
Hamming=0.54+0.46*np.cos((2*np.pi*n)/N-1)
#Hanning window
Hanning=0.5+0.5*np.cos((2*np.pi*n)/N-1)
#Blackman window
Blackman=0.42+0.5*np.cos((2*np.pi*n)/N-1)+0.08*np.cos((4*np.pi*n)/N-1)
# Graficar la ventana
#Ahi le puse en nombre  1
plt.figure(figsize=(8, 8))
plt.subplot(5,1,1)
plt.stem(n, rectangular_window, basefmt=" ")
plt.title("Ventana Rectangular (N = 31)")
plt.xlabel("n")
plt.ylabel("w[n]")
plt.grid(True)
plt.tight_layout()
#Ahi le puse en nombre  2
plt.subplot(5,1,2)
plt.stem(n, Bartlett_triangular, basefmt=" ")
plt.title(" Bartlett window or Triangular window (N = 31)")
plt.xlabel("n")
plt.ylabel("w[n]")
plt.grid(True)
plt.tight_layout()
#Ahi le puse en nombre  3
plt.subplot(5,1,3)
plt.stem(n, Hamming, basefmt=" ")
plt.title(" Hamming window(N = 31)")
plt.xlabel("n")
plt.ylabel("w[n]")
plt.grid(True)
plt.tight_layout()
#Ahi le puse en nombre  4
plt.subplot(5,1,4)
plt.stem(n, Hanning, basefmt=" ")
plt.title(" Hanning window(N = 31)")
plt.xlabel("n")
plt.ylabel("w[n]")
plt.grid(True)
plt.tight_layout()
#Ahi le puse en nombre  5
plt.subplot(5,1,5)
plt.stem(n, Blackman, basefmt=" ")
plt.title(" Blackman window(N = 31)")
plt.xlabel("n")
plt.ylabel("w[n]")
plt.grid(True)
plt.tight_layout()
plt.show()
#Comentario, los priemros 2 tiposd e ventanas si se nota como cambia su manera de ver los resultados
#Pero en las ultimas 3 es muy dificil notar un cambio, diria que son lo mimso.