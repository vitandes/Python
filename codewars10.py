def number(bus_stops):
    cont = 0
    
    for stop in bus_stops:
        passengers_on = stop[0]
        passengers_off = stop[1]
        cont += passengers_on - passengers_off
        
    return cont

print(number([[10, 0], [3, 5], [5, 8]]))

