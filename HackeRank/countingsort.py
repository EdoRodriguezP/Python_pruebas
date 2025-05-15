arr = [1,2,3,4,3,2,1]            # array de ejemplo para uso

counting_arr = [0 for x in range(100)]  #se toma el array y se cuenta cien veces

for number in arr:                       #se itera el array
    
        counting_arr[number] += 1       
    
print(counting_arr)
