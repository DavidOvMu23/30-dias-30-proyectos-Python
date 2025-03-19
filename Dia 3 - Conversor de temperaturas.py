import sys

salir = False  # Variable para controlar la salida del programa

while not salir:  # Bucle principal que se ejecuta hasta que 'salir' sea True
    print("")
    print("-----Conversor de temperaturas-----")
    print("1- Convertir temperatura")
    print("2- Salir del programa")
    print("-----------------------------------")
    opcMenu = int(input("Ingrese una opcion: "))

    if opcMenu == 1:
        while True:  # Bucle para el menú de conversión
            print("")
            print("-----Tipo de conversion-----")
            print("1- Celsius a Fahrenheit")
            print("2- Fahrenheit a Celsius")
            print("3- Celsius a Kelvin")
            print("4- Kelvin a Celsius")
            print("5- Fahrenheit a Kelvin")
            print("6- Kelvin a Fahrenheit")
            print("7- Volver al menu principal")
            print("8- Salir del programa")
            print("-----------------------------")
            opcConv = int(input("Ingrese una opcion: "))

            if opcConv == 1:
                print("")
                celsius = float(input("Ingrese la temperatura en Celsius: "))
                fahrenheit = (celsius * 9 / 5) + 32
                print("La temperatura en Fahrenheit es: ", fahrenheit)
                break  # Sale del bucle de conversión y vuelve al menú principal

            elif opcConv == 2:
                print("")
                fahrenheit = float(input("Ingrese la temperatura en Fahrenheit: "))
                celsius = (fahrenheit - 32) * 5 / 9
                print("La temperatura en Celsius es: ", celsius)
                break  # Sale del bucle de conversión y vuelve al menú principal

            elif opcConv == 3:
                print("")
                celsius = float(input("Ingrese la temperatura en Celsius: "))
                kelvin = celsius + 273.15
                print("La temperatura en Kelvin es: ", kelvin)
                break  # Sale del bucle de conversión y vuelve al menú principal

            elif opcConv == 4:
                print("")
                kelvin = float(input("Ingrese la temperatura en Kelvin: "))
                celsius = kelvin - 273.15
                print("La temperatura en Celsius es: ", celsius)
                break  # Sale del bucle de conversión y vuelve al menú principal

            elif opcConv == 5:
                print("")
                fahrenheit = float(input("Ingrese la temperatura en Fahrenheit: "))
                kelvin = (fahrenheit - 32) * 5 / 9 + 273.15
                print("La temperatura en Kelvin es: ", kelvin)
                break  # Sale del bucle de conversión y vuelve al menú principal

            elif opcConv == 6:
                print("")
                kelvin = float(input("Ingrese la temperatura en Kelvin: "))
                fahrenheit = (kelvin - 273.15) * 9 / 5 + 32
                print("La temperatura en Fahrenheit es: ", fahrenheit)
                break  # Sale del bucle de conversión y vuelve al menú principal

            elif opcConv == 7:  # Volver al menú principal
                break  # Sale del bucle de conversión y vuelve al menú principal

            elif opcConv == 8:  # Salir del programa
                salir = True  # Establece 'salir' a True para salir del bucle principal
                print("")
                print("Gracias por usar el conversor de temperaturas")
                sys.exit()  # Sale del programa

            else:
                print(
                    "Opcion no valida, por favor intente de nuevo."
                )  # Muestra un mensaje de error y vuelve a mostrar el menú de conversión

    elif opcMenu == 2:  # Si el usuario elige salir del programa
        salir = True  # Establece 'salir' a True para salir del bucle principal
        print("")
        print("Gracias por usar el conversor de temperaturas")
        sys.exit()  # Sale del programa

    else:
        print("")
        print(
            "Opcion no valida, por favor intente de nuevo."
        )  # Muestra un mensaje de error y vuelve a mostrar el menú principal
