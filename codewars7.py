def invert(lst):
    
    if len(lst) == 1:
        r = []
        r.insert(0,lst[0]*-1)
        return r 
    
    rest_of_list = invert(lst[1:])  # Recursión para invertir el resto de la lista
    rest_of_list.insert(0, lst[0] * -1)  # Agregar el elemento invertido al comienzo de la lista

    return rest_of_list


a = invert([1,2,3,4,5])
print(a)