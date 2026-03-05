numeros = [10, 20, 30, 40, 50]
inversa = []

for i in range(len(numeros) - 1, -1, -1):
    inversa.append(numeros[i])
    
print(f"Lista original: {numeros}")
print(f"Lista invertida: {inversa}")