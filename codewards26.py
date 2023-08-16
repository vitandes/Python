def abbrev_name(name):
    cap = name.upper()
    arr = cap.split(" ")
    return arr[0][0]+"."+ arr[1][0]

print(abbrev_name("Hola Mundo"))