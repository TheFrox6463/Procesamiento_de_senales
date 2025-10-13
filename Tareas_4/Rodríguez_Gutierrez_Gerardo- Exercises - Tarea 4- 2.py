from scipy.signal import TransferFunction

# Coeficientes de la función de transferencia H(z) = z^2 / (z^2 + 4z - 2)
num = [1, 0, 0]  # Numerador
den = [1, 4, -2]  # Denominador

# Crear el objeto de la función de transferencia
sys = TransferFunction(num, den, dt=1)  # Asumimos que el sistema es discreto (dt=1)

# Obtener la representación en espacio de estados
A, B, C, D = sys.to_ss().A, sys.to_ss().B, sys.to_ss().C, sys.to_ss().D

# Mostrar los resultados
print("Matriz A:\n", A)
print("Matriz B:\n", B)
print("Matriz C:\n", C)
print("Matriz D:\n", D)
