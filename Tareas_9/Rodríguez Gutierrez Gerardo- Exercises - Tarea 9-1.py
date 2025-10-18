def decimal_a_binario(num, decimales=8): #Definimos la funcion 
    # Parte entera
    parte_entera = int(num)
    # Parte fraccionaria
    parte_fraccionaria = num - parte_entera
    
    # Convertir parte entera a binario
    bin_entera = bin(parte_entera).replace("0b", "")
    
    # Convertir parte fraccionaria a binario
    bin_fraccionaria = [] #Lo que hace el ciclo for es que va iterando para cada numero y lo convierte 
    for _ in range(decimales):  #en numeros decimales
        parte_fraccionaria *= 2
        bit = int(parte_fraccionaria)
        bin_fraccionaria.append(str(bit))
        parte_fraccionaria -= bit
        if parte_fraccionaria == 0:
            break
    
    # Completar con ceros si es necesario
    bin_fraccionaria = ''.join(bin_fraccionaria).ljust(decimales, '0')
    
    # Combinar parte entera y fraccionaria
    return f"{bin_entera}.{bin_fraccionaria}"

# Ejemplo de uso
numero = 12.375
resultado = decimal_a_binario(numero, decimales=8)
print(f"El número {numero} en binario es: {resultado}")
