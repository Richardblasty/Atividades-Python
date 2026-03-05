lista = [1, 2, 3, 2, 4, 3, 5, 1, 6]
unica = []

for elemento in lista:
    if elemento not in unica:
        unica.append(elemento)
        
print(f"Lista original: {lista}")
print(f"Lista sem duplicatas: {unica}")