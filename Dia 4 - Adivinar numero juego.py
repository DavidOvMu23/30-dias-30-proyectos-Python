import random

print("═════════════════════════════════════════════════════")
print("     ¡Bienvenido al juego de adivinar el número!     ")
print("═════════════════════════════════════════════════════")
print("El juego consiste en adivinar un número entre 1 y 100")
print("═════════════════════════════════════════════════════")
print("Hay 2 niveles de dificultad:")
print("1- Fácil: sin intentos limitados")
print("2- Difícil: 7 intentos")
print("═════════════════════════════════════════════════════")

while True:
    try:
        dificultad = int(input("Elige la dificultad (1 o 2): "))
        if dificultad in [1, 2]:
            break
        else:
            print("¡Error! Por favor, elige 1 o 2.")
    except ValueError:
        print("¡Error! Por favor, introduce un número válido.")

# Generar un número aleatorio entre 1 y 100 independientemente de la dificultad
numero_entero = random.randint(1, 100)
intentos = 0

if dificultad == 1:
    while True:  # El bucle se ejecuta hasta que se encuentra un break
        intentos += 1  # Contador de intentos
        numero_usuario = int(input("Adivina el número: "))
        if numero_usuario == numero_entero:
            print("")
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
            break  # Rompe el bucle y termina el programa

        elif numero_usuario < numero_entero:
            print("")
            print("El número es mayor.")

        else:
            print("")
            print("El número es menor.")

elif dificultad == 2:
    while intentos < 7:
        intentos += 1  # Contador de intentos
        numero_usuario = int(
            input("Adivina el número: ")
        )  # El usuario introduce un número

        if numero_usuario == numero_entero:
            print("")
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
            break

        elif numero_usuario < numero_entero:
            print("")
            print("El número es mayor.")

        else:
            print("")
            print("El número es menor.")
    else:
        print("")
        print(f"¡Lo siento! El número era {numero_entero}.")
        print("¡Inténtalo de nuevo!")

print("══════════════════════════════════════════════════")
print("¡Gracias por jugar!")
print("══════════════════════════════════════════════════")
