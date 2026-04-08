###
# 03 - cast
#  El casting es el proceso de convertir un valor de un tipo a otro.
#  En Python, se puede hacer casting explícito utilizando funciones como int(), float(), str(), etc.
###

import os
os.system('cls' if os.name == 'nt' else 'clear')

print('Casting en Python: ')

# print(type("100"))  # <class 'str'>
# print(type(int("100")))
# print(type(2.5 + int("5"))) # <class 'int'>

print(int(2.5))  # 2
# print(round(2.5))  # 2 Redondea al número par más cercano
# print(round(3.5))  # 4 Redondea al número par más cercano
# print(round(3.2))  # 3 Redondea al número par más cercano
# print(round(2.6))  # 3 Redondea al número par más cercano

# print(bool(3))  # True
# print(bool(0))  # False
# print(bool(-1))  # True

# print(bool(""))  # False
# print(bool(" "))  # True
# print(bool("False"))  # True