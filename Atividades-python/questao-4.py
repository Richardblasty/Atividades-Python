numeros = [10, 45, 23, 87, 15, 62]

menor = numeros[0]  
for numero in numeros:
    if numero < menor:
        menor = numero

print(f"O menor valor na lista é: {menor}")