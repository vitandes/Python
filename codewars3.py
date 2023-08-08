def count_positives_sum_negatives(arr):
    if len(arr) == 0:
        return []
    
    if len(arr) == 1: 
        if arr[0] > 0:
            return [1 , 0]
        elif arr[0] < 0:
            return [0 , arr[0]]
        else:
            return[0,0]
    
    num = count_positives_sum_negatives(arr[1:])
    positives, negatives = num[0], num[1]

    if(arr[0]>0):
        positives +=1
    elif arr[0]<0 :
        negatives += arr[0]
    return [positives, negatives]