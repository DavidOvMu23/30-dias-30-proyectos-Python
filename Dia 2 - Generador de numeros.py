import random

# Genera un número entero aleatorio entre 1 y 10
numero_entero = random.randint(1, 10)
print(f"Número entero aleatorio: {numero_entero}")


# Genera un número de punto flotante aleatorio entre 1 y 10
numero_flotante_rango = random.uniform(1, 10)
print(f"Número flotante aleatorio en rango: {numero_flotante_rango}")


# Elige un elemento aleatorio de la lista
lista = [1, 2, 3, 4, 5]

elemento_aleatorio = random.choice(lista)
print(f"Elemento aleatorio de la lista: {elemento_aleatorio}")


# Genera una lista de 5 números enteros aleatorios entre 1 y 10
lista_numeros = []

for i in range(5):  # Itera 5 veces
    # Genera un número entero aleatorio entre 1 y 10
    numero_aleatorio = random.randint(1, 10)
    # Agrega el número aleatorio a la lista
    lista_numeros.append(numero_aleatorio)

print(f"Lista de números enteros aleatorios: {lista_numeros}")
