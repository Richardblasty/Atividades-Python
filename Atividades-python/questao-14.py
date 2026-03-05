lista = [10, 25, 37, 42, 58, 63, 71]
elemento = 42
encontrado = False

for item in lista:
    if item == elemento:
        encontrado = True
        break
if encontrado:
    print(f"O elemento {elemento} existe na lista")
else:
    print(f"O elemento {elemento} não existe na lista")