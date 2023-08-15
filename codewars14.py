def decrypt(encrypted_text, n):
    arr = list(encrypted_text)
    length = len(encrypted_text)
    
    for j in range(n):
        mid = length // 2
        odd_chars = arr[:mid]  # Caracteres en posiciones impares originales
        even_chars = arr[mid:]  # Caracteres en posiciones pares originales
        
        arr = [char for pair in zip(odd_chars, even_chars) for char in pair]
        if length % 2 != 0:
            arr.append(odd_chars[-1])
    
    return ''.join(arr)

encrypted_text = encrypt("135024", 2)
decrypted_text = decrypt(encrypted_text, 2)

print("Encrypted:", encrypted_text)
print("Decrypted:", decrypted_text)


def encrypt(text, n):
    arr = list(text)
    for j in range(n-1):
        odd_chars = arr[1::2]  # Extraer caracteres en posiciones impares
        even_chars = arr[0::2]  # Extraer caracteres en posiciones pares
        
        arr = odd_chars + even_chars  # Concatenar las listas
        
    return ''.join(arr)  # Convertir la lista de caracteres de nuevo a una cadena

print(encrypt("135024", 1))
    


print(encrypt("135024", 2))
print(encrypt("135024", 3))