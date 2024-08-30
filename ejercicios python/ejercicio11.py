def es_numero_perfecto(numero):
    if numero <= 1:
        return False
    
    suma_divisores = 0
    
    for i in range(1, numero):
        if numero % i == 0:
            suma_divisores += i
    
   
    return suma_divisores == numero


numero = int(input("Ingresa un número: "))


if es_numero_perfecto(numero):
    print(f"El número {numero} es un número perfecto.")
else:
    print(f"El número {numero} no es un número perfecto.")