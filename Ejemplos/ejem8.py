
s = "06:00:00PM"
def convertlist (s):
    return [
        s[0:2],
        s[3:5],
        s[6:8],
        s[8:10],
    ]

hh, mm, ss, shift = convertlist(s)

if shift == "AM":
    if hh == "12":
        hh = "00"
else:
    if hh != "12":
        hh = str(int(hh) + 12).zfill(2)

# Mostrar resultado
result = f"{hh}:{mm}:{ss}" 
print(result)
    # Write your code here