def find_short(s):
    array = s.split(" ")
    cont = len(array[0])
   
    for i in range(len(array)):
        if len(array[i]) < cont:
            cont = len(array[i])
            
    return cont

print(find_short("i want to travel the world writing code one day"))