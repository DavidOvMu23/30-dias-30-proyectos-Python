import sys  # Importa el módulo sys para poder usar sys.exit() y salir del programa

salir = False  # Variable para controlar el bucle principal

# Bucle principal que se ejecuta mientras 'salir' sea False
while not salir:
    print("")
    print("-----¿Que operación deseas realizar?-----")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potenciación")
    print("6. Salir")
    print("")
    print("-----Elige una opcion-----")
    opcion = int(input())  # Lee la opción del usuario y la convierte a entero

    # Condicionales para cada opción
    if opcion == 1:
        print("")
        print("-----Suma-----")
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        print(f"El resultado de la suma es: {num1 + num2}")

    elif opcion == 2:
        print("")
        print("-----Resta-----")
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        print(f"El resultado de la resta es: {num1 - num2}")

    elif opcion == 3:
        print("")
        print("-----Multiplicar-----")
        num1 = float(input("Ingrese el multiplicando: "))
        num2 = float(input("Ingrese el multiplicador: "))
        print(f"El resultado de la multiplicación es: {num1 * num2}")

    elif opcion == 4:
        print("")
        print("-----Dividir-----")
        num1 = float(input("Ingrese el dividendo: "))
        num2 = float(input("Ingrese el divisor: "))

        # Verifica que el divisor no sea cero
        if num2 != 0:
            print(f"El resultado de la división es: {num1 / num2}")
            print(f"El residuo es: {num1 % num2}")
        else:
            print("¡¡¡¡¡Error: División por cero no permitida.!!!!!")

    elif opcion == 5:
        print("")
        print("-----Potenciación-----")
        num1 = float(input("Ingrese la base: "))
        num2 = float(input("Ingrese el exponente: "))
        print(f"El resultado de la potenciación es: {num1 ** num2}")

    elif opcion == 6:
        print("")
        print("-----Gracias por usar la calculadora-----")
        sys.exit()  # Sale del programa

    else:
        print("")
        print("Opción no válida")
        continue  # Vuelve al inicio del bucle

    while True:
        print("")
        print("-----¿Deseas realizar otra operación? (s/n)-----")
        # Lee la respuesta del usuario y la convierte a minúsculas
        continuar = input().strip().lower()

        if continuar == "s":
            salir = False  # Continúa el bucle
            break
        elif continuar == "n":
            print("")
            print("-----Gracias por usar la calculadora-----")
            sys.exit()  # Sale del programa
        else:
            print("")
            # Mensaje de error si la opción no es válida
            print("Opción no válida, por favor ingresa 's' o 'n'.")
