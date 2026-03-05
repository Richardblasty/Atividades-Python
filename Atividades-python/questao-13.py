numeros = [64, 34, 25, 12, 22, 11, 90]
lista_ordenada = numeros[:]
n = len(lista_ordenada)

for i in range(n - 1):
    for j in range(n - i - 1):
        if lista_ordenada[j] > lista_ordenada[j + 1]:
            temp = lista_ordenada[j]
            lista_ordenada[j] = lista_ordenada[j + 1]
            lista_ordenada[j + 1] = temp
            
print(f"Lista original: {numeros}")
print(f"Lista ordenada: {lista_ordenada}")