#Del libro pagina 406
#Illustration of downsampling operation
import numpy as np
import matplotlib.pyplot as plt
#Step 1: Generation of input signal x[n]
n=np.linspace(-10,10,21)
x=np.exp(1j*np.pi*n)
x2=np.exp(2j*np.pi*n)
#Step 2: Downsampling the input signal
M=2
y=x[::M]
y2=x[::M]
#Step 3: Plotting the results
n1=np.linspace(min(n)/M,max(n)/M,len(y))
n2=np.linspace(min(n)/M,max(n)/M,len(y2))
plt.subplot(4,1,1),plt.stem(n,x),plt.xticks(range(-10,11))
plt.xlabel('n-->'),plt.ylabel('x[n]'),plt.title('Input Signal (x[n])')
plt.subplot(4,1,2),plt.stem(n1,y),plt.xticks(range(-10,11))
plt.xlabel('n-->'),plt.ylabel('y[n]'),
plt.title('Downsampled Signal (y[n]) by (M={})'.format(M))
plt.tight_layout() 
plt.subplot(4,1,3),plt.stem(n,x2),plt.xticks(range(-10,11))
plt.xlabel('n-->'),plt.ylabel('x[n]'),plt.title('Input Signal (x[n])')
plt.subplot(4,1,4),plt.stem(n2,y2),plt.xticks(range(-10,11))
plt.xlabel('n-->'),plt.ylabel('y[n]'),
plt.title('Downsampled Signal (y[n]) by (M={})'.format(M))
plt.tight_layout() 
plt.show()
#Aditividad : el downsampling de la suma es igual a la suma de los downsamplings.
#Homogeneidad: el downsampling del escalar por la señal es igual al escalar por el downsampling.
#Aditividad
aux=y+y2
left_additivity = y+y2
aux[::M]
print("✅ Aditividad comprobada:", np.array_equal(left_additivity, aux))
print("Downsample(x1 + x2):", left_additivity)
print("Downsample(x1) + Downsample(x2):", aux)
#Segun si cumple la grafica la ley de aditividad.
plt.subplot(2,1,1),plt.stem(n,(x+x2)),plt.xticks(range(-10,11))
plt.xlabel('n-->'),plt.ylabel('x[n]'),plt.title('Input Signal (x[n])')
plt.subplot(2,1,2),plt.stem(n1+n2,y+y2),plt.xticks(range(-10,11))
plt.xlabel('n-->'),plt.ylabel('y[n]'),
plt.show()
#Homogeneidad
a = 3  # escalar
aux2=a*y
left_homogeneity = aux2[::M]
right_homogeneity = a * y
print("\n✅ Homogeneidad comprobada:", np.array_equal(left_homogeneity, right_homogeneity))
print("Downsample(a * x1):", left_homogeneity)
print("a * Downsample(x1):", right_homogeneity)
