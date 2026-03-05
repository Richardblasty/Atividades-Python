numeros = [10, -5, 23, -8, 0, 15, -3, 7, -12, 4]
positivos = 0
negativos = 0

for numero in numeros:
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
        
print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")