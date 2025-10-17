import control as ss
#datos
numerador=10
Denominador=[1,10]
periodo=1
fsam=1/periodo
s1=ss.tf(numerador,Denominador) 
#Transformada
print("Antes del immpulso")
print(s1)
yd = s1.sample(periodo, method='impulse')
print('impulso invanriante A)=',yd) 
#Bilineal?
yd2= s1.sample(periodo, method='bilinear')
print('impulso bilinear B)=',yd2)

