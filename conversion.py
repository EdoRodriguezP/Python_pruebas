import sys

def validar_argumentos():     # Funcion para validar entrada de argumentos
    if len(sys.argv) != 2:    # Si los argumentos son diferente a 2 imprime error y uso
        print("Error: Se debe ingresar 2 argumentos")
        print("Uso: python conversiones.py [archivo]")
        sys.exit(1)

archivo = sys.argv[1]             # Se crea variable archivo y se le asigna el archivo de texto

with open(archivo, "r") as f:
    texto = f.read()
    
palabras_distintas = set(texto.split())
distintos = set(texto)    
    

print(len(palabras_distintas))
print(len(distintos))


    
    