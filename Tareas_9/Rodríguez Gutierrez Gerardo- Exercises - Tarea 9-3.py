#Se supone que es verificar que no se pase la cantidad dependiendo del bit
N =input("Ingresa el bit: ")
a=int(input("\nValor a: "))
b=int(input("\n Valor b: "))
val_max=0
val_min=0
#Calculamos el minimo y el maximo en base a lo bits
min_val = -(2 ** (int(N) - 1))
max_val = (2 ** (int(N) - 1)) - 1
if (a+b) > max_val:
    saturado=val_max
elif  (a+b) < max_val:
    saturado=val_min
else:
    saturado=a+b
def wrap_around(value, bits=8):
    mask = (1 << bits) - 1
    value = value & mask
    if value >= (1 << (bits - 1)):
        value -= (1 << bits)
    return value
resultado_wrap = wrap_around(a + b)
# Simulación con saturación


print(f"Resultado real de 100 + 50: {a + b}")
print(f"Resultado con overflow (wrap-around): {resultado_wrap}")
print(f"Resultado con saturación: {saturado}")