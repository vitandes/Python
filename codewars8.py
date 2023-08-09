def disemvowel(string_):
    vowels = "AEIOUaeriou"
    newchar = ""

    for char in string_:
        if char not in  vowels:
            newchar += char
    
    return newchar


a= disemvowel("This website is for losers LOL!")
print(a)