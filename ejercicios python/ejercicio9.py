numero = int(input("Ingresa un número: "))


es_divisible = False


if numero % 4 == 0:
    print(f"El número {numero} es divisible por 4")
    es_divisible = True


if numero % 6 == 0:
    print(f"El número {numero} es divisible por 6")
    es_divisible = True


if numero % 8 == 0:
    print(f"El número {numero} es divisible por 8")
    es_divisible = True


if numero % 10 == 0:
    print(f"El número {numero} es divisible por 10")
    es_divisible = True


if not es_divisible:
    print(f"El número {numero} no es divisible ni por 4, ni por 6, ni por 8, ni por 10")