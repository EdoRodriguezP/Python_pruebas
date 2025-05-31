



def menu():
    print(""" 
menu de opciones
1.ingresar nota
2.calcular estadisticas
3.resultados
4.salir
      """)
    
    
def main():
    notas = []

    while True:
        menu()
        opcion = int(input("ingrese una opcion:"))
        
        if opcion == 1:
            n = input("ingresa las notas: ")
            n = n.split(" ")
            notas = [float(nota) for nota in n]
            print(notas)
        
        elif opcion == 2:
            try:
                promedio = sum(notas) / len(notas)
                mayor = max(notas)
                menor = min(notas)
                aprobado = [a for a in notas if a > 4.0]
                print(promedio)
                print(aprobado)
                print(mayor,menor)
                
            except ZeroDivisionError:
                print("no hay notas agregadas")
            continue
        elif opcion == 3:
            
            
            print(f"""
promedio : {promedio}
minimo   : {menor}
mayor    : {mayor}
aprobado : {aprobado}
""")
            break
        else:
            print("4")
            
main()
menu()
if __name__ == "__main__":
    main()