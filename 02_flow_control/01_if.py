###
# 01 if - Sentencias condicionales (if , elif , else )
# Permiten ejecutar un bloque de código solo si se cumple una condición específica.
###

import os
os.system('cls' if os.name == 'nt' else 'clear')


print('\n Sentencia simple condicional if, else:')

edad = int(input('Ingrese su edad: '))

if edad >= 18:
    print('Eres mayor de edad.')
else:
    print('Eres menor de edad.')    
    

print('\n Sentencia condicional elif:')

nota = int(input('Ingrese la nota: '))

if nota >= 9:
    print('Excelente')
elif nota >= 7:
    print('Bueno')
elif nota >= 5:
    print('Suficiente')
else:
    print('Insuficiente')

print('\n Sentencias condicionales multiples:')
edad = int(input('Ingrese su edad: '))
tiene_carnet = input('¿Tienes carnet de conducir? (si/no): ').lower()

if edad >= 18 and tiene_carnet == 'si':
    print('Puedes conducir.')
elif edad >= 18 and tiene_carnet == 'no':
    print('Puedes conducir, pero necesitas obtener tu carnet.')
elif edad < 18 and tiene_carnet == 'si':
    print('No puedes conducir, aunque tienes carnet, eres menor de edad.')
else:
    print('No puedes conducir, eres menor de edad y no tienes carnet.')

es_fin_de_semana = False
if not es_fin_de_semana:
    print('Es un día de semana, a trabajar!')


print('\n Anidar sentencias condicionales.')
edad = 20
tiene_dinero = True

if edad >= 18:
    if tiene_dinero:
        print('Puedes salir a divertirte.')
    else:
        print('Puedes salir, pero necesitas dinero.')
else:
    print('Eres menor de edad, no puedes salir a divertirte.')


numero = 5
if numero: # true si numero es diferente de cero, False si es cero
    print("El numero no es cero, es considerado True en un contexto booleano.")


numero = 0
if numero: # false si numero es cero
    print("El numero es cero, es considerado False en un contexto booleano.")

nombre = ""
if nombre: # false si la cadena esta vacia
    print("El nombre no está vacío, es considerado True en un contexto booleano.")


numero = 3 # asignacion de un valor a la variable numero
es_el_tres = numero == 3 # comparacion, devuelve True o False

if es_el_tres:
    print("El numero es igual a 3.")

print('\n La condicion ternaria (operador condicional): ')
# [codigo si cumple la condicion] if [condicion] else [codigo si no cumple la condicion]

edad = 17

mensaje = "Es mayor de edad" if edad >= 18 else "Es menor de edad"
print(mensaje)

print("Es mayor de edad" if edad >= 18 else "Es menor de edad")
