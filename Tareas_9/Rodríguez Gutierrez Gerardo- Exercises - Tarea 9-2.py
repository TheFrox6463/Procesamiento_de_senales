from codecs import decode
import sys
import struct
binario = input("Ingresa un número binario: ")
print("\nEl número que ingresaste es:", binario)
# Validar que solo contenga 0 y 1
conversion=0
i=len(binario)-1
for caracter in binario:
  print("_______",caracter)
  if caracter == "0":
        i=i-1   
        print(conversion)    
  elif caracter== "1":
        conversion=conversion+(2**i)
        i=i-1
        print(conversion)   
  else:
      print("No es binario")
      sys.exit()
print("numero en decimal",conversion)
