import sys

def validar_argumentos():     # Funcion para validar entrada de 4 argumentos
    if len(sys.argv) != 2:    # Si los argumentos son diferente a 4 imprime 
        print("Error: Se debe ingresar 4 argumentos")
        print("Uso: python conversiones.py [archivo]")
        sys.exit(1)

archivo = sys.argv[1]

with open(archivo, "r") as f:
    texto = f.read()
    
palabras_distintas = set(texto.split())
distintos = set(texto)    
    

print(len(palabras_distintas))
print(len(distintos))


    
    