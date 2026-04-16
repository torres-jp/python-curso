###
# 02 - loop for
# Permite ejecutar un bloque de codigo repetidamente mientras ITERA un iterable o una lista
###

import os
os.system('cls')

print('\n Bucle for: ')

# Iterar una lista
frutas = ['manzana', 'pera', 'banana', 'frutilla', 'limon', 'uva']

for fruta in frutas:
    print(fruta)


# Iterar sobre cualquier cosa iterable
cadena = 'python'
for caracteres in cadena:
    print(caracteres)


# Enumerates
# Devuelve el indice y el valor
frutas = ['manzana', 'pera', 'banana', 'frutilla', 'limon', 'uva']
for index, fruta in enumerate(frutas):
    print(f'El indice es {index} y la fruta es {fruta}')


# Bucles anidados
letras = ['A','B','C']
numeros = [1,2,3]

for letra in letras: # 1ra iteracion
    for numero in numeros: # 1ra iteracion
        print(f'{letra}-{numero}') # A-1
    # 2da iteracion
    # 3ra iteracion
