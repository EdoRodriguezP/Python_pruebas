import math as m

r_km = float(input("Ingrese el radio en Kilomnetros :"))
g = float(input("Ingrese la constante g :"))
r_metros = r_km * 1000

v = 2*g*r_metros
vel_escape = m.sqrt(v)


print(f"La Velocidad de escape es : {vel_escape:.1f} [m/s]")