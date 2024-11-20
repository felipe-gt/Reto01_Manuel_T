seguir = 0
seguir = str(input("desea operar? si / no"))
if seguir == "si":
    while seguir == "si":
        print("***operaciones aritméticas básicas")
        a = int(input("Digite el valor del primer número:"))
        b = int(input("Digite el valor del segundo número: "))
    
        print("Menú de operaciones básicas")
        print("(+) Suma ")
        print("(-) Resta")
        print("(*) Multiplicación")
        print("(/) División")
        
        c = str(input("¿Qué operación desea usar? "))
        sumar = a + b
        res = a - b
        mul = a * b
        div = a / b
        if c == "+":
            print(f'La suma de los números ingresados es: {sumar}')
        
        elif c == "-":
            print(f'La resta de los números ingresados es: {res}')
        
        elif c == "*":
            print(f'La multiplicación de los números ingresados es: {mul}')
        
        elif c == "/":
            if b == 0:
                print("No se puede dividir por cero")
            else:
                div = a / b
                print(f'La división de los números ingresados es: {div}')
                
        else:
            print("El carácter ingresado no está dentro del rango de operaciones")
        seguir = str(input("¿Desea continuar operando? si / no "))
