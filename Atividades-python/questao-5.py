numeros = [10, 45, 23, 88, 15, 62, 30, 41]

contador = 0
for numero in numeros:
    if numero % 2 == 0:
        contador += 1

print(f"Quantidade de números pares: {contador}")