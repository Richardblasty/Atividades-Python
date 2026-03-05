lista1 = [1, 2, 3, 4, 5, 6]
lista2 = [4, 5, 6, 7, 8, 9]
comuns = []

for elemento in lista1:
    for item in lista2:
        if elemento == item and elemento not in comuns:
            comuns.append(elemento)
            
print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")
print(f"Elementos comuns: {comuns}")