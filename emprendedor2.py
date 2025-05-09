p = float(input("Ingresa el precio de suscripcion : "))
u_n= float(input("Ingresa el numero de usuarios normales : "))
u_p = float(input("Ingresa el numero de usuarios premium : "))
gt = float(input("Ingrsa el gasto total : "))



utilidades = (p * u_n) + ((p*0.5+p) * u_p) - gt

print(f"la utilidad es : {utilidades}")