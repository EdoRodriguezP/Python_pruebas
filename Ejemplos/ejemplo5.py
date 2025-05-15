# Sumar todos los numeros de un rango
#[1,2,3,4,5,6,7,8,9]

numero = int(input("ingresa un numero : ")) #se ingresa el numero

suma = 0      # se declara la variable 

for i in range(1,numero + 1 ):     # el rango parte de cero por lo cual se indica que inicie en 1 y sume uno al final
    suma = suma + i                 # se van sumando los numeros del rango hasta numero + 1
    print(i)
    
print(f"la suma es  {suma}")