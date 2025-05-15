arr = [1,2,3,4,3,2,1]

    
counting_arr = [0 for x in range(100)]

for number in arr:
    
        counting_arr[number] += 1
    
print(counting_arr)
