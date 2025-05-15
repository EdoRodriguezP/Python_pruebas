#contar cuantas letras aparecen en un texto

texto = "este es el teto necesario para la ejecuccion del programa"
contador = 0
letra = "f"

for i in texto:
    if letra == i:
        contador += 1
        
print(contador)
        
