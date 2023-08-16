def series_sum(n):
    total_sum = 0
    denominator = 1   
    
    for i in range(n):
        total_sum += 1 / denominator 
        denominator += 3 
    string = (round(total_sum, 2))
    string = str("{:.2f}".format(string))
    
    return string

print(series_sum(1))


