arr = [1,3,5,7,9]

arr = sorted(arr)
min_sum = sum(arr[:4])
max_sum = sum(arr[-4:])
print(f"la suma minima es {min_sum}")
print(f"la suma maxima es {max_sum}")