seguir = 0
seguir = str(input(desea operar))
while seguir == "si":
    print("***operaciones aritméticas básicas")
    a = int(input("digite el valor del primer número: " ))
    print("Menú de operaciones básicas")
    print("(+) Suma ")
    print("(-) Resta")
    print("(*) Multiplicación")
    print("(/) División")
    
    c = str(input("Qué operación desea usar? "))
    
    sumar = a + b
    res = a - b
    mul = a * b
    div = a / b
    
    if c == "+":
        print(f'La suma de los números ingresados es:{sumar}')
    
    if c == "-":
        print(f'La resta de los números ingresados es:{res}')
    
    if  c == "*":
        print(f'La multiplicación de los números ingresados es:{mul}')
    
    if c == "/":
        if b == 0:
            print("no se puede operar")
        else:
            print(f'La división de los números ingresados es:{div}') 
            
    else:
        print("El carácter ingresado no está dentro del rango de operaciones")
    seguir = str(input( "desea continuar operando? si / no "))