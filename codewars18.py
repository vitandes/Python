def get_count(sentence):
    cont = 0
    for i in range(len(sentence)):
        if sentence[i] in "aeiou":
            cont += 1
    return cont

print(get_count("hola"))