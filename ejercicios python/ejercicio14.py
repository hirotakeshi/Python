n = int(input("Ingresa el número de filas para la pirámide inversa: "))


for i in range(n, 0, -1):
    
    print(' ' * (n - i) + '*' * (2 * i - 1))