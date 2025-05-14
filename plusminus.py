
arr = [1,1,0,-1,-1]

def plusMinus(arr):
    positivos = 0
    negativos = 0
    zeros = 0
    n = 0
    
    for number in arr:
        n +=1
        if (number > 0):
            positivos += 1
        elif (number < 0):
            negativos += 1
        else:
            zeros += 1
            
    positivos_ratio = round(positivos / n, 6)
    negativos_ratio = round(negativos / n, 6)
    zeros_ratio = round(zeros / n, 6)
    
    print(positivos_ratio)
    print(negativos_ratio)
    print(zeros_ratio)