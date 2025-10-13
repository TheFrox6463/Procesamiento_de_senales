#Ejercicio 3
#State-space to transfer function
from scipy import signal
import numpy as np
#Step 1: Defining the state-space model
A=[[0,1],[-1/6,-5/6]]
B=[[0], [1]]
C = [[1, 0]]
D = 0
#Step 2: Obtaining the transfer function
[num,den]=signal.ss2tf(A,B,C,D)
print('numerator=',num)
print('denominaor=',den) 