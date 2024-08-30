max_numero = 300


contador_lineas = 0


for numero in range(1, max_numero + 1):
   
    if numero % 5 == 0 and numero % 7 == 0:
        print(f"{numero} (Múltiplo de 5 y 7)")
    elif numero % 5 == 0:
        print(f"{numero} (Múltiplo de 5)")
    elif numero % 7 == 0:
        print(f"{numero} (Múltiplo de 7)")
    else:
        print(numero)

    
    contador_lineas += 1

   
    if contador_lineas % 6 == 0:
        print("-" * 60) 