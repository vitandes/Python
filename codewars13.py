def tower_builder(n_floors):
    arr = []
    contador = n_floors - 1
    asteriscos = 1

    if n_floors==0:
        return []
    
    if n_floors == 1:
        return ["*"]
    
    for i in range(n_floors):
        a = " " * contador + "*" * asteriscos + " " * contador
        arr.append(a)
        contador -= 1
        asteriscos +=2
        
        
    return arr

print(tower_builder(4))
