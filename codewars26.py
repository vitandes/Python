def max_sequence(arr):
    suma = 0
    sumTotal = 0
    
    for i in range(len(arr)):
        for j in range(len(arr)-1, i, -1):
            suma = sum(arr[i:j+1])
            
            if suma > sumTotal:
                sumTotal= suma
        suma = 0
    return sumTotal

print(max_sequence([-2, -1, -3, -4, -1, -2, -1, -5, -4]))