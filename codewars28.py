def are_you_playing_banjo(name):
    return (f"{name} plays banjo" if name.lower()[0]== "r" else f"{name} does not play banjo")

print(are_you_playing_banjo("rarta"))