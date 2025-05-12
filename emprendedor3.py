

p = float(input("Ingresa el precio de suscripcion : "))
u_n = float(input("Ingresa el numero de usuarios normales: "))
gt = float(input("Ingrsa el gasto total : "))
utilidad_anterior = float(input("Ingresa la utilidad del año anterior : "))

utilidades = p * u_n - gt
razon = utilidades / utilidad_anterior

print(f"La utilidad actual es : {utilidades}")
print(f"La razon entre las utilidades es: {razon}")