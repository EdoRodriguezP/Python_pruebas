# dada una lista pcon elementos duplicados devolver una lista sin duplicados manteniendo el orden

#lista [1,2,3,4,3,4,2,1,5,7,8,5]

lista = [1,2,3,4,3,4,2,1,5,7,8,5] # lista entregada
resultado = []                     #Se crea lista vacia resultado y duplicados
duplicados = []

for elemento in lista:     # se itera la lista 
    if elemento not in resultado:    # se revisa si el elemento no esta en la lista resultado
        resultado.append(elemento)   # si no esta lo guarda el elemento lo guarda en lista resultado
    else:
        duplicados.append(elemento)   #si esta en la lista resultado lo guarda en lista duplicados
        
print(f"{resultado}") # se imprimen nos resultados
print(f"{duplicados}")

