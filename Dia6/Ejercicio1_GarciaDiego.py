entrada = input("")
numeros = [int (num) for num in entrada.split(',')]
numeros_unicos = []
for num in numeros:
    if num not in numeros_unicos:
        numeros_unicos.append(num)
numeros_unicos.sort()        
print(" " , numeros_unicos)        