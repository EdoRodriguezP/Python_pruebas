hora = "06:00:00pm"
myString = hora.upper()  # Convertir a mayúsculas para estandarizar

def convertlist(hora):
    return [
        hora[0:2],  # hh
        hora[3:5],  # mm
        hora[6:8],  # ss
        hora[8:10]  # AM/PM
    ]

hh, mm, ss, shift = convertlist(myString)  # se extraen componentes y se asigna variable

# Convertir a formato 24h
if shift == "AM":        # si shift es igual AM y hh igual a 12
    if hh == "12":
        hh = "00"       # se le asigna el valor de  00 a la lista hh
else:
    if hh != "12":
        hh = str(int(hh) + 12).zfill(2)

print(f"{hh}:{mm}:{ss}")  # Mostrar resultado.