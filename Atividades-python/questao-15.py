lista = [1, 2, 3, 2, 4, 2, 5, 2, 6]
valor = 2
contador = 0

for elemento in lista:
    if elemento == valor:
        contador += 1
        
print(f"O valor {valor} aparece {contador} vezes na lista")