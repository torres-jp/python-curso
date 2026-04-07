###
# 02 - types
#  Los tipos de datos son las categorías que definen el comportamiento y las # # # operaciones que se pueden realizar con los valores en un lenguaje de programación.
# int, float, str, bool, list, tuple, dict, set, NoneType, range , complex , # frozenSet, bytes, bytearray, memoryview, etc.
###

import os
os.system('cls' if os.name == 'nt' else 'clear')

""" 
Esto es una cadena de texto
que se extiende a varias líneas. Se puede usar para escribir comentarios largos o para incluir texto con saltos de línea sin necesidad de usar caracteres de escape.
"""

print('int: ')

# print(type(10))
# print(type(0))
# print(type(-55))
# print(type(34231235676434532))

print('float: ')
# print(type(3.14))
# print(type(1.0))
# print(type(1e3))  # Notación científica para 1000.0
# print(type(-0.001))

print('complex: ')
# print(type(3+4j))
# print(type(1-2j))

print('str: ')
# # print(type('Hola, mundo!'))
# # print(type("Python es genial"))
# print(type('''Esto es una cadena de texto
# que se extiende a varias líneas.'''))

print('bool: ')
# print(type(True))
# print(type(False))

print('NoneType: ')
# print(type(None))