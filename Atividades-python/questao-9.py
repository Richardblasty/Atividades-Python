lista = [1, 2, 3, 2, 1]
inversa = []

for i in range(len(lista) - 1, -1, -1):
    inversa.append(lista[i])
if lista == inversa:
    
    print("É um palíndromo")
else:
    print("Não é um palíndromo")