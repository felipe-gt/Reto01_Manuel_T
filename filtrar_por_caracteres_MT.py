def filtrar_por_caracteres(lista):
    """Filtra y retorna los elementos de la lista que tienen los mismos caracteres."""
    resultado = []
    
    # Recorrer la lista y comparar cada par de palabras
    for palabra in lista:
        for otra_palabra in lista:
            if palabra != otra_palabra and sorted(palabra) == sorted(otra_palabra):
                if palabra not in resultado:
                    resultado.append(palabra)
                if otra_palabra not in resultado:
                    resultado.append(otra_palabra)
    return resultado

palabras = []

cantidad = int(input("¿Cuántas palabras deseas ingresar? "))
for i in range(cantidad):
   palabra = (input(f"Ingrese las palabras {i + 1}: "))
   palabras.append(palabra)

salida = filtrar_por_caracteres(palabras)
print(f"Anagramas encontrados: {salida}")