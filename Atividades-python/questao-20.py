lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]
uniao = []

for elemento in lista1:
    if elemento not in uniao:
        uniao.append(elemento)

for elemento in lista2:
    if elemento not in uniao:
        uniao.append(elemento)
        
print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")
print(f"União sem repetições: {uniao}")