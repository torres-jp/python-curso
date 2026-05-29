###
# EJERCICIOS
###

import os
os.system('cls' if os.name == 'nt' else 'clear')

# Ejercicio 1: El mensaje secreto
# Dada la siguiente lista:
# mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# Utilizando slicing y concatenación, crea una nueva lista que contenga solo el mensaje "secreto".

print("\n Ejercicio 1: El mensaje secreto")
mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
print(mensaje[7:])


# Ejercicio 2: Intercambio de posiciones
# Dada la siguiente lista:
# numeros = [10, 20, 30, 40, 50]
# Intercambia la primera y la última posición utilizando solo asignación por índice.

print("\n Ejercicio 2: Intercambio de posiciones")
numeros = [10, 20, 30, 40, 50]
numeros[0], numeros[-1] = numeros[-1], numeros[0]
print(numeros) # [50, 20, 30, 40, 10]



# Ejercicio 3: El sándwich de listas
# Dadas las siguientes listas:
# Crea una lista llamada sandwich que contenga el pan de arriba, los ingredientes y el pan de abajo, en ese orden.

pan = ["pan arriba"]
ingredientes = ["jamón", "queso", "tomate"]
pan_abajo = ["pan abajo"]

print("\n Ejercicio 3: El sándwich de listas")
sandwich = pan + ingredientes + pan_abajo
print(sandwich) # ['pan arriba', 'jamón', 'queso', 'tomate', 'pan abajo']

# Ejercicio 4: Duplicando la lista
# Dada una lista:
# lista = [1, 2, 3]
# Crea una nueva lista que contenga los elementos de la lista original duplicados.
# Ejemplo: [1, 2, 3] -> [1, 2, 3, 1, 2, 3]
print("\n Ejercicio 4: Duplicando la lista")
lista = [1, 2, 3]
lista = lista + lista
print(lista)


# Ejercicio 5: Extrayendo el centro
# Dada una lista con un número impar de elementos, extrae el elemento que se encuentra en el centro de la lista utilizando slicing.
# Ejemplo: lista = [10, 20, 30, 40, 50] -> El centro es 30
print("\n Ejercicio 5: Extrayendo el centro")
lista = [10, 20, 30, 40, 50]
print(lista[len(lista) // 2]) # 30
print(lista[2])


# Ejercicio 6: Reversa parcial
# Dada una lista, invierte solo la primera mitad de la lista (utilizando slicing y concatenación).
# Ejemplo: lista = [1, 2, 3, 4, 5, 6] -> Resultado: [3, 2, 1, 4, 5, 6]
print("\n Ejercicio 6: Reversa parcial")
lista = [1, 2, 3, 4, 5, 6]
print(lista[len(lista)//2:][::-1] + lista[:len(lista)//2])