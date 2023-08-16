def sq_in_rect(lng, wdth):
    
    if lng==0 or wdth==0 or lng==wdth:
        return None
    
    horizontal = wdth
    longitud = lng

    if lng < wdth:
        horizontal = lng
        longitud = wdth
    arr = []

    arr.append(horizontal)
    arr.append(longitud - horizontal)
    horizontal = horizontal - (longitud - horizontal)
    if lng > wdth:
        longitud = lng - wdth
    else:
        longitud= wdth - lng
    for i in range(horizontal, 0, -1):
        if i <= horizontal and i<= longitud:
            arr.append(i)
            horizontal -= i
    
    if lng > wdth:
        longitud = lng-wdth - arr[-1]
    else:
        longitud = wdth-lng - arr[-1]

    horizontal = arr[-1]
    while(horizontal<=longitud):
        arr.append(horizontal)
        longitud-=horizontal
    return arr

print(sq_in_rect(3,5))