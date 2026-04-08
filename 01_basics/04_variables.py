###
# 04 - variables
#  Las variables son contenedores para almacenar valores.
#  En Python, no es necesario declarar el tipo de variable.
#  Se puede asignar un valor a una variable utilizando el operador de asignación (=).
# Python es un lenguaje de tipado dinámico, lo que significa que el tipo de una variable se determina en tiempo de ejecución y puede cambiar a lo largo del programa.
###


import os
os.system('cls' if os.name == 'nt' else 'clear')

# my_name = 'Alice'
# age = 40

# print(my_name)

my_name = 'Bob'
age = 30

# print(my_name)
# print(age)


# Tipado dinámico: 
# name = 'Alice'
# print(type(name))  # <class 'str'>

# name = 42
# print(type(name))  # <class 'int'>

# Tipado fuerte:
# print("10" + 3)  # Esto generará un error de tipo, ya que no se pueden concatenar una cadena y un número entero.

# f-strings:
# print(f'Mi nombre es {my_name} y tengo {age + 12} años.')    

# name, age ,city = 'Alice', 40, 'New York'
# print(f'Mi nombre es {name}, tengo {age} años y vivo en {city}.')

# Convecion de nombres de variables:
# my_name = 'Alice'  # snake_case
# myName = 'Alice'   # camelCase
# my-name = 'Alice'  # kebab-case (no es válido en Python)
# MY_NAME = 'Alice'  # UPPER_SNAKE_CASE (usado para constantes)

# Palabras reservadas:
# def = 'Alice'  # Esto generará un error, ya que 'def' es una palabra reservada en Python.
# ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

is_user_logged_in: bool = True 
print(is_user_logged_in)

is_user_logged_in = 42
print(is_user_logged_in)