###
# EJERCICIOS
###

import os
os.system('cls' if os.name == 'nt' else 'clear')

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales
num1 = int(input('Ingrese el primer número: '))
num2 = int(input('Ingrese el segundo número: '))

if num1 > num2:
    print(f'El número {num1} es mayor que {num2}.')
elif num2 > num1:
    print(f'El número {num2} es mayor que {num1}.') 
else:
    print('Los números son iguales.')




# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)
num1 = float(input('Ingrese el primer número: '))
num2 = float(input('Ingrese el segundo número: '))

operacion = input('Ingrese la operación (+, -, *, /): ')

if operacion == '+':
    resultado = num1 + num2
    print(f'El resultado de {num1} + {num2} es: {resultado}')
elif operacion == '-':
    resultado = num1 - num2
    print(f'El resultado de {num1} - {num2} es: {resultado}')
elif operacion == '*':
    resultado = num1 * num2
    print(f'El resultado de {num1} * {num2} es: {resultado}')
elif operacion == '/':
    if num2 != 0:
        resultado = num1 / num2
        print(f'El resultado de {num1} / {num2} es: {resultado}')
    else:
        print('Error: No se puede dividir entre cero.')
else:
    print('Operación no válida.')

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

age = int(input("Introduce un año: "))

if (age % 4 == 0 and age % 100 != 0) or age % 400 == 0:
    print(f"{age} es un año bisiesto.")
else:
    print(f"{age} no es un año bisiesto.")


# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)
age = int(input('Ingrese una edad: '))
if age >= 0 and age <= 2:
    print('La persona es un bebé.')
elif age >= 3 and age <= 12:
    print('La persona es un niño.')
elif age >= 13 and age <= 17:
    print('La persona es un adolescente.')
elif age >= 18 and age <= 64:
    print('La persona es un adulto.')
else:
    print('La persona es un adulto mayor.')