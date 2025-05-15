a = [1,2,3,4,3,2,1]
resultado = []
duplicado = []
unico = []
for numbers in a:
    if numbers not in resultado:
        resultado.append(numbers)
    else:
        duplicado.append(numbers)
    for numbers in resultado:
        if numbers not in duplicado:    
            salida = numbers
print(salida)