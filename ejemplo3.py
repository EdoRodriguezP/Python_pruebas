#contar todas las vocales de una palabra
#


palabra = "LOrem ipsun Asimetric close pArAlelepipedo"
palabra = palabra.lower()
vocales = "aeiouáéíóú"
vocales_en = 0
consonantes = 0

for letras in palabra:     # se itera la lista 
    if letras in vocales:  # se revisa si el elemento no esta en la lista resultado
        vocales_en = vocales_en + 1   # si no esta lo guarda el elemento lo guarda en lista resultado
    else:
        consonantes = consonantes + 1   #si esta en la lista resultado lo guarda en lista duplicados
        
print(f"{vocales_en}") # se imprimen nos resultados
print(f"{consonantes}")
print(f"{palabra}")