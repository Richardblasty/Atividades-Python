numeros = [10, 45, 23, 87, 15, 62, 87, 34]
maior = numeros[0]
segundo_maior = numeros[0]

for numero in numeros:
    if numero > maior:
        segundo_maior = maior
        maior = numero
    elif numero > segundo_maior and numero != maior:
        segundo_maior = numero
        
print(f"O segundo maior valor é: {segundo_maior}")