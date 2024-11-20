def mayor_suma_consecutivos(lista):
    """Encuentra la mayor suma entre dos elementos consecutivos en una lista."""
    if len(lista) < 2:
        raise ValueError("La lista debe tener al menos dos elementos.")
    
    mayor_suma = lista[0] + lista[1]
    
    for i in range(1, len(lista) - 1):
        suma_actual = lista[i] + lista[i + 1]
        if suma_actual > mayor_suma:
            mayor_suma = suma_actual

    return mayor_suma

numeros = []

cantidad = int(input("¿Cuántos números deseas ingresar? "))
for i in range(cantidad):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    numeros.append(numero)
    
resultado = mayor_suma_consecutivos(numeros)
print(f"La mayor suma entre dos elementos consecutivos es: {resultado}")