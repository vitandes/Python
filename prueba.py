def fact(n):

    if n == 1:
        return n
    
    mult = n * fact(n - 1)

    return mult 


a = fact(6)
print(a)