###
# 03 - listas
# Sequencings mutable de elementos.
# Pueden contener elementos de diferentes tipos.
###

import os
os.system('cls' if os.name == 'nt' else 'clear')

# Creation de listas
print("\n Crear listas: ")
lista1 = [1,2,3,4,5,6,7,8,9,10] # lista de enters
lista2 = ["manzanas", "frutillas", "bananas", "pera", "uva", "durazno"] # lista de cadenas de texto
lista3: list[str | int | float | bool] = [3, "hola", 3.14, True] # lista de tipos mixtos

lista_vacia = []
lista_de_listas = [[1,2,3],[4,5,6],[7,8,9]]
matrix = [[1,2],[2,3],[4,5]]

print(lista1)
print(lista2)
print(lista3)
print(lista_vacia)
print(lista_de_listas)
print(matrix)

# Acceso a elementos por indice
print('\nAcceso a elementos por indice: ')
print(lista2[0]) # manzanas
print(lista2[1]) # frutillas
print(lista2[-1]) # durazno
print(lista2[-2]) # uva

print(matrix[1][1]) # 3


# Slicing de listas
print('\n Slicing de listas: ')
lista_1 = [1,2,3,4,5,6,7,8,9,10]

print(lista_1[1:4]) # [2,3,4] No cuenta el indice 4
print(lista_1[:3]) # [1,2,3] Desde el inicio hasta el indice 3 (no incluido)
print(lista_1[:]) # [1,2,3,4,5,6,7,8,9,10] Copia de toda la lista


print('\n Mas slicing: ')

# print(lista_1[desde:hasta:paso]) # [1,3,5,7,9] Desde el inicio hasta el final con un paso de 2
print(lista_1[::2]) # [1,3,5,7,9] Desde el inicio hasta el final con un paso de 2
print(lista_1[1:10:2]) # [2,4,6,8,10] Desde el indice 1 hasta el indice 10 (no incluido) con un paso de 2
print(lista_1[::-1]) # [10,9,8,7,6,5,4,3,2,1] Desde el final hasta el inicio con un paso de -1 (reversa)


# Modificacion de elementos
print('\n Modificacion de elementos: ')

lista_1[0] = 20
print(lista_1) # [20,2,3,4,5,6,7]

# Añadir elementos a la lista
lista_2 = [1,2,3,4,5,6]

# forma larga
lista_2 = lista_2 + [7,8,9,10] # concatenacion de listas
print(lista_2) # [1,2,3,4,5,6,7,8,9,10]

# forma corta
lista_1 += [11,12,13,14,15] # concatenacion de listas
print(lista_1) 

# Recuperar longitud
print('\n Longitud de la lista: ')
print(len(lista_1)) # 15