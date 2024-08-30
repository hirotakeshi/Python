numero = int(input("Ingresa un número: "))


if numero % 4 == 0:
    print(f"El número {numero} es divisible por 4")
if numero % 6 == 0:
    print(f"El número {numero} es divisible por 6")
if numero % 8 == 0:
    print(f"El número {numero} es divisible por 8")
if numero % 10 == 0:
    print(f"El número {numero} es divisible por 10")
    

if numero % 4 != 0 and numero % 6 != 0 and numero % 8 != 0 and numero % 10 != 0:
    print(f"El número {numero} no es divisible ni por 4, ni por 6, ni por 8, ni por 10")



    