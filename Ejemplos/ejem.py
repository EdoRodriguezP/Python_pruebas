a = [1,2,3,4,3,2,1]

resultado = []
unico = []
for numbers in a:
    if numbers not in resultado:
        resultado.append(resultado)
    else:
        unico.append(unico)
print(unico)
print(resultado)