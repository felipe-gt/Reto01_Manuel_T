def es_palindromo(palabra):
    palabra = palabra.lower().replace(" ", "")
    
    longitud = len(palabra)
    for i in range(longitud // 2):
        if palabra[i] != palabra[longitud - i - 1]:
            return False
    return True

palabra = input("Introduce una palabra: ")
if es_palindromo(palabra):
    print(f'"{palabra}" es un palíndromo.')
else:
    print(f'"{palabra}" no es un palíndromo.')