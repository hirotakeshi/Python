numero = int(input("Ingresa un número: "))

print(f"Los múltiplos de 3 menores que {numero} son:")
for i in range(3, numero, 3):
    print(i)