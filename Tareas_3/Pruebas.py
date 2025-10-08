#Distributive property of convolution 
import numpy as np 
import matplotlib.pyplot as plt 
n=np.arange(-5,6) 
#Step 1: Generation of input signal 
x=np.array([0,0,0,0,1,2,1,0,0,0,0]) 
#Step 2: Generation of h1 and h2 
k=5 
h1=np.array([0,0,0,0,1,1,1,0,0,0,0]) 
h2=np.array([0,0,0,0,-1,0,-1,0,0,0,0]) 
#Step 3: Perform the convolution 
h=h1+h2 
y1=np.convolve(x,h,mode='full') 
y2=np.convolve(x,h1,mode='full')+np.convolve(x,h2,mode='full') 
N=len(y1) 
n1=np.arange(-N/2,N/2) 
#Step 4: Displaying the result 
plt.figure(1),plt.subplot(3,1,1),plt.stem(n,x),plt.xticks(n),plt.xlabel('n-->'), 
plt.ylabel('Amplitude'),plt.title('x[n]'),plt.subplot(3,1,2),plt.stem(n,h1),plt.xticks(n) 
plt.xlabel('n-->'),plt.ylabel('Amplitude'),plt.title('$h_1$[n]'),plt.subplot(3,1,3), 
plt.stem(n,h2),plt.xticks(n),plt.xlabel('n-->'),plt.ylabel('Amplitude'),plt.title('$h_2$[n]') 
plt.tight_layout() 
plt.figure(2),plt.subplot(2,1,1),plt.stem(n1,y1),plt.xlabel('n-->'), 
plt.ylabel('Amplitude'),plt.title('$y_1[n]$=(x[n]*$h_1$[n])*$h_2$[n]') 
plt.subplot(2,1,2),plt.stem(n1,y1),plt.xlabel('n-->'),plt.ylabel('Amplitude'), 
plt.title('$y_2[n]$=x[n]*($h_1$[n])*$h_2$[n])') 
plt.tight_layout()
plt.show() 