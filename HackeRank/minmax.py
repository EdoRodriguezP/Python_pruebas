arr = [1,3,5,7,9]  # lista tipo array

arr = sorted(arr)  # toma la lista y retorna la lista con los elementos en orden ascendente

min_sum = sum(arr[:4])  # realiza suma de la lista  desde 0:4         1,3,5,7,9
max_sum = sum(arr[-4:])  # realiza suma de la lista  desde -4:0       0 1 2 3 4

print(f"la suma minima es {min_sum}")  # se imprimen resultados
print(f"la suma maxima es {max_sum}")