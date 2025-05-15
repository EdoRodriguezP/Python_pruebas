#contar todas las vocales de una palabra
#


palabra = "LOrem ipsun Asimetric close pArAlelepipedo" #se crea un string con una palabra
palabra = palabra.lower()                              #pasa el strin a minuscula
vocales = "aeiouáéíóú"                                 # se da el string vocales a revisar se agrgan con acento
vocales_en = 0
consonantes = 0

for letras in palabra:     # se itera la lista 
    if letras in vocales:  # se revisa si el letras esta en la lista vocales
        vocales_en = vocales_en + 1   # si esta suma 1 a vocales
    else:
        consonantes = consonantes + 1   #si no esta suma 1 a consonantes
        
        
print(f"{vocales_en}") # se imprimen nos resultados
print(f"{consonantes}")
print(f"{palabra}")