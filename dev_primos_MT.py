def es_primo(num):
    """Determina si un número es primo."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def filtrar_primos(lista):
    """Devuelve una lista con los números primos de la lista original."""
    return [num for num in lista if es_primo(num)]

numeros = []

cantidad = int(input("¿Cuántos números deseas ingresar? "))
for i in range(cantidad):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    numeros.append(numero)

print(f"Los números ingresados son: {numeros}")
numeros = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15]
primos = filtrar_primos(numeros)
print(f"Números primos: {primos}")