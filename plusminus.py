

arr = [1,1,0,-1,-1]

def plusMinus(arr):
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
            
    positivos_ratio = round(positivos / n, 6)
    negativos_ratio = round(negativos / n, 6)
    zeros_ratio = round(zeros / n, 6)
    
    print(f"porcentaje positivos :{positivos_ratio:.6f}")
    print(positivos_ratio)
    print(negativos_ratio)
    print(arr)
    
    print(f"La utilidad obtenida es : {positivos_ratio}")