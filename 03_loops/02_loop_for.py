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

# Break
animales = ['perro', 'gato', 'leon', 'tigre', 'elefante']
for idx,animal in enumerate(animales):
    print(animal)
    if animal == 'tigre':
        print(f'El animal {animal} se encuentra en la posicion {idx}')
        break


# Continue
animales = ['perro', 'gato', 'leon', 'tigre', 'elefante']
for idx,animal in enumerate(animales):
    if animal == 'tigre':
        continue
    
    print(animal)


# Comprension de listas
# Es una forma concisa de crear listas

letras =  ['A','B','C','D','E','F']
letras_minusculas = [letra.lower() for letra in letras]
print(letras_minusculas)

## Muestra los numeros pares de una lista
pares = [num for num in [1,2,3,4,5,6,7,8,9,10] if num % 2 == 0]
print(pares)