numeros = [10, 45, 23, 87, 15, 62]

maior = numeros[0]  
for numero in numeros:
    if numero > maior:
        maior = numero

print(f"O maior valor na lista é: {maior}")