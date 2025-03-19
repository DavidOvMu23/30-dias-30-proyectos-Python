import sys

salir = False

while not salir:
    print("")
    print("-----Conversor de temperaturas-----")
    print("1- Convertir temperatura")
    print("2- Salir del programa")
    print("-----------------------------------")
    opcMenu = int(input("Ingrese una opcion: "))

    if opcMenu == 1:
        while True:
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
                break

            elif opcConv == 2:
                print("")
                fahrenheit = float(input("Ingrese la temperatura en Fahrenheit: "))
                celsius = (fahrenheit - 32) * 5 / 9
                print("La temperatura en Celsius es: ", celsius)
                break

            elif opcConv == 3:
                print("")
                celsius = float(input("Ingrese la temperatura en Celsius: "))
                kelvin = celsius + 273.15
                print("La temperatura en Kelvin es: ", kelvin)
                break

            elif opcConv == 4:
                print("")
                kelvin = float(input("Ingrese la temperatura en Kelvin: "))
                celsius = kelvin - 273.15
                print("La temperatura en Celsius es: ", celsius)
                break

            elif opcConv == 5:
                print("")
                fahrenheit = float(input("Ingrese la temperatura en Fahrenheit: "))
                kelvin = (fahrenheit - 32) * 5 / 9 + 273.15
                print("La temperatura en Kelvin es: ", kelvin)
                break

            elif opcConv == 6:
                print("")
                kelvin = float(input("Ingrese la temperatura en Kelvin: "))
                fahrenheit = (kelvin - 273.15) * 9 / 5 + 32
                print("La temperatura en Fahrenheit es: ", fahrenheit)
                break

            elif opcConv == 7:
                break  # Volver al menú principal

            elif opcConv == 8:
                salir = True
                print("")
                print("Gracias por usar el conversor de temperaturas")
                sys.exit()

            else:
                print("Opcion no valida, por favor intente de nuevo.")

    elif opcMenu == 2:
        salir = True
        print("")
        print("Gracias por usar el conversor de temperaturas")
        sys.exit()

    else:
        print("")
        print("Opcion no valida, por favor intente de nuevo.")
1
