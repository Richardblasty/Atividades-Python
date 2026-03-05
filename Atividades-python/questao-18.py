lista = [1, 2, 3, 2, 4, 3, 5, 1, 6, 2, 3]
contados = []

for elemento in lista:
    if elemento not in contados:
        contador = 0
        
        for item in lista:
            if item == elemento:
                contador += 1
        contados.append(elemento)

        print(f"Elemento {elemento}: {contador} vezes")