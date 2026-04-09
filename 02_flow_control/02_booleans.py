###
# 02 - booleanos 
# Los booleanos son un tipo de dato que representa dos valores posibles: True (verdadero) y False (falso).
# Se utilizan para controlar el flujo de un programa, tomar decisiones y realizar comparaciones.
###
import os
os.system('cls' if os.name == 'nt' else 'clear')

# Los booleanos se pueden obtener a través de comparaciones y operaciones lógicas.
print('\n Valores booleanos:')
print(True)
print(False)

# Operadores de comparación
print('\n Operadores de comparación:')
print(5 > 3)   # True
print(5 < 3)   # False
print(5 == 5)  # True igualdad
print(5 != 3)  # True diferente
print(5 >= 5)  # True
print(5 <= 3)  # False

print('\n Comparar cadenas de texto:')
print("manzana < pera", "manzana" < "pera")  # True, comparación lexicográfica  
print("manzana > pera", "manzana" > "pera")  # False
print("Manzana == manzana", "Manzana" == "manzana")  # True

# Operadores lógicos
print('\n Operadores lógicos:')
print('AND (y):', True and False)  # False
print('AND (y):', True and True)   # True
print('OR (o):', True or False)    # True
print('OR (o):', False or False)   # False
print('NOT (no):', not True)       # False
print('NOT (no):', not False)      # True

# tablas de verdad (para referencia)
print('\n Tabla de verdad del AND:')
print('True and True:', True and True) # True
print('True and False:', True and False) # False
print('False and True:', False and True) # False
print('False and False:', False and False) # False

print('\n Tabla de verdad del OR:')
print('True or True:', True or True) # True
print('True or False:', True or False) # True
print('False or True:', False or True) # True
print('False or False:', False or False) # False

print('\n Tabla de verdad del NOT:')
print('not True:', not True) # False
print('not False:', not False) 