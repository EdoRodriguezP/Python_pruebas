# dada una lista pcon elementos duplicados devolver una lista sin duplicados manteniendo el orden

#lista [1,2,3,4,3,4,2,1,5,7,8,5]

lista = [1,2,3,4,3,4,2,1,5,7,8,5] # lista entregada
resultado = []
duplicados = []

for elemento in lista:
    if elemento not in resultado:
        resultado.append(elemento)
    else:
        duplicados.append(elemento)
        
print(f"{resultado}")
print(f"{duplicados}")

