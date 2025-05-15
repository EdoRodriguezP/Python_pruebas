hora = "06:00:00pm"
myString = hora.upper()  # Convertir a mayúsculas para estandarizar

def convert2list(hora):
    return [
        hora[0:2],  # hh
        hora[3:5],  # mm
        hora[6:8],  # ss
        hora[8:10]  # AM/PM
    ]

# Extraer componentes
hh, mm, ss, shift = convert2list(myString)

# Convertir a formato 24h
if shift == "AM":
    if hh == "12":
        hh = "00"
else:
    if hh != "12":
        hh = str(int(hh) + 12).zfill(2)

# Mostrar resultado
print(f"{hh}:{mm}:{ss}")