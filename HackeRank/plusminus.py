
arr = [-4, 3, -9, 0, 4, 1]


positivos = 0
negativos = 0
zeros = 0
n = 0
    
for number in arr:
    n = n + 1
    if (number > 0):
        positivos = positivos + 1
    elif (number < 0):
        negativos = negativos + 1
    else:
        zeros = zeros + 1
        
    positivos_ratio = (positivos / n)
    negativos_ratio = (negativos / n)
    zeros_ratio = (zeros / n)
    
print(f"{positivos_ratio:.6f}")
print(f"{negativos_ratio:.6f}")
print(f"{zeros_ratio:.6f}")
