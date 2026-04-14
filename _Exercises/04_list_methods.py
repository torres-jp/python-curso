###
# EJERCICIOS
# Usa siempre que puedas los métodos que has aprendido
###

import os

os.system("cls" if os.name == "nt" else "clear")

# Ejercicio 1: Añadir y modificar elementos
# Crea una lista con los números del 1 al 5.
# Añade el número 6 al final usando append().
# Inserta el número 10 en la posición 2 usando insert().
# Modifica el primer elemento de la lista para que sea 0.
print("Ejercicio 1: Añadir y modificar elementos")
lista = [1, 2, 3, 4, 5]
lista.append(6)  # Añade el número 6 al final de la lista
lista.insert(2, 10)  # Inserta el número 10 en la posición 2
lista[0] = 0  # Modifica el primer elemento de la lista para que sea 0
print(lista)

# Ejercicio 2: Combinar y limpiar listas
# Crea dos listas:
# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6, 1, 2]
# Extiende lista_a con lista_b usando extend().
# Elimina la primera aparición del número 1 en lista_a usando remove().
# Elimina el elemento en el índice 3 de lista_a usando pop(). Imprime el elemento eliminado.
# Limpia completamente lista_b usando clear().
print("\n Ejercicio 2: Combinar y limpiar listas")
lista_a = [1, 2, 3]
lista_b = [4, 5, 6, 1, 2]
lista_a.extend(lista_b)  # Extiende lista_a con lista_b
lista_a.remove(1)  # Elimina la primera aparición del número 1 en lista_a
elemento_eliminado = lista_a.pop(
    3
)  # Elimina el elemento en el índice 3 de lista_a y lo devuelve
print(f"Elemento eliminado: {elemento_eliminado}")
lista_b.clear()  # Limpia completamente lista_b
print(lista_a)


# Ejercicio 3: Slicing y eliminación con del
# Crea una lista con los números del 1 al 10.
# Utiliza slicing y del para eliminar los elementos desde el índice 2 hasta el 5 (sin incluir el 5).
# Imprime la lista resultante.
print("\n Ejercicio 3: Slicing y eliminación con del")
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
del numeros[
    2:5
]  # Elimina los elementos desde el índice 2 hasta el 5 (sin incluir el 5)
print(numeros)


# Ejercicio 4: Ordenar y contar
# Crea una lista con los siguientes números: [5, 2, 8, 1, 9, 4, 2].
# Ordena la lista de forma ascendente usando sort().
# Cuenta cuántas veces aparece el número 2 en la lista usando count().
# Comprueba si el número 7 está en la lista usando in.
print("\n Ejercicio 4: Ordenar y contar")
numeros = [5, 2, 8, 1, 9, 4, 2]
numeros.sort()  # Ordena la lista de forma ascendente
print(numeros)
print(numeros.count(2))  # Cuenta cuántas veces aparece el número 2 en la lista
print(7 in numeros)  # Comprueba si el número 7 está en la lista

# Ejercicio 5: Copia vs. Referencia
# Crea una lista llamada original con los números [1, 2, 3].
# Crea una copia de la lista original llamada copia_1 usando slicing.
# Crea otra copia llamada copia_2 usando copy().
# Crea una referencia a la lista original llamada referencia.
# Modifica el primer elemento de la lista referencia a 10.
# Imprime las cuatro listas (original, copia_1, copia_2, referencia) y observa los cambios.
print("\n Ejercicio 5: Copia vs. Referencia")
numeros = [1, 2, 3]
copia_1 = numeros[:]  # Crea una copia de la lista original usando slicing
copia_2 = numeros.copy()  # Crea otra copia usando copy()
referencia = numeros  # Crea una referencia a la lista original
referencia[0] = 10  # Modifica el primer elemento de la lista referencia a 10
print(f"Original: {numeros}")
print(f"Copia 1: {copia_1}")
print(f"Copia 2: {copia_2}")
print(f"Referencia: {referencia}")


# Ejercicio 6: Ordenar strings sin diferenciar mayúsculas y minúsculas.
# Crea una lista con las siguientes cadenas: ["Manzana", "pera", "BANANA", "naranja"].
# Ordena la lista sin diferenciar entre mayúsculas y minúsculas.
print("\n Ejercicio 6: Ordenar strings sin diferenciar mayúsculas y minúsculas")
cadenas = ["Manzana", "pera", "BANANA", "naranja"]
cadenas.sort(
    key=str.lower
)  # Ordena la lista sin diferenciar entre mayúsculas y minúsculas
print(cadenas)
