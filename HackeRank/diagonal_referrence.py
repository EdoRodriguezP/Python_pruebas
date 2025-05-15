arr = [
    [1, 2, 3],
    [4, 5, 6],
    [9, 8, 9]
]

# arr [i][j] = arr[0][0],arr[1][1],arr[2][2]

sum_diag_der_izq = 0
sum_diag_izq_der = 0
for i in range(len(arr)):
    sum_diag_der_izq += arr[i][i]
    sum_diag_izq_der += arr[i][(len(arr)-1)-i]
    
print(abs(sum_diag_der_izq - sum_diag_izq_der))