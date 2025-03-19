import random

numero_entero = random.randint(0, 100)
print(f"Número entero aleatorio: {numero_entero}")

intentos = 0

while True:  # El bucle se ejecuta hasta que se encuentra un break
    intentos += 1  # Contador de intentos
    numero_usuario = int(input("Adivina el número: "))
    if numero_usuario == numero_entero:
        print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
        break  # Rompe el bucle y termina el programa

    elif numero_usuario < numero_entero:
        print("El número es mayor.")

    else:
        print("El número es menor.")
