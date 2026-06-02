###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

import os
os.system('cls' if os.name == 'nt' else 'clear') # Limpiar la consola antes de ejecutar los ejercicios

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

### Completa aquí
print("Tu nombre es: Jhon y \n  tu ciudad es: USA")
print("--------------")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

### Completa aquí
print(type(a)) # int
print(type(b)) # float
print(type(c)) # str
print(type(d)) # bool
print(type(e)) # NoneType

print("--------------")

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

### Completa aquí
cadena = "12345"
print(int(cadena)) # 12345
print(float(cadena)) # 12345.0

float_num = 3.99
print(int(float_num)) # 3, se pierde la parte decimal al convertir a entero
print(round(float_num)) # 4, redondea al número entero más cercano

print("--------------")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

# "Hola! Me llamo midudev y tengo 39 años, mido 1.70 metros"

### Completa aquí
nombre = 'Jhon'
age = 40
height = 1.89
print(f'Hola! Me llamo {nombre} y tengo {age} años, mido {height} metros.')


print("--------------")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

### Completa aquí
pi = 3.14159
print(round(pi)) # 3
print(3 // 2) # 1