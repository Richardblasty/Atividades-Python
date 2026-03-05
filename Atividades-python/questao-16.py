matriz1 = [[1, 2], [3, 4]]
matriz2 = [[5, 6], [7, 8]]
soma = [[0, 0], [0, 0]]

for i in range(2):
    for j in range(2):
        soma[i][j] = matriz1[i][j] + matriz2[i][j]

print("Matriz 1:")
print(matriz1[0])
print(matriz1[1])
print("\nMatriz 2:")
print(matriz2[0])
print(matriz2[1])
print("\nSoma das matrizes:")
print(soma[0])
print(soma[1])