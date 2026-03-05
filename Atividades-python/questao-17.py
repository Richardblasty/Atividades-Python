vetor1 = [1, 2, 3]
vetor2 = [4, 5, 6]
produto_escalar = 0

for i in range(len(vetor1)):
    produto_escalar += vetor1[i] * vetor2[i]

print(f"Vetor 1: {vetor1}")
print(f"Vetor 2: {vetor2}")
print(f"Produto escalar: {produto_escalar}")