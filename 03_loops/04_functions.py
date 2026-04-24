###
# 04 - functions
# BLoque de codigo que realiza una tarea especifica
# Se puede reutilizar
# Se define con def
# Se ejecuta cuando se llama
###

import os

os.system("cls" if os.name == "nt" else "clear")

""" Definicion de una funcion

def nombre_de_la_function(parametro1, parametro2,...):
    #docstring
    #cuerpo de la funcion
    return valor_de_retorno # opcional


"""


# Ejemplo funcion saludar
def saludar():
    print("hola!")


# LLamar a la funcion
saludar()


# Ejemplo de una funcion con parametro
def saludar_a(nombre):
    print(f"hola {nombre}")


# LLamar a la funcion con parametro
saludar_a("Juan")
saludar_a("Maria")
saludar_a("Pedro")


# Ejemplo con funciones con mas parametros
def sumar(a, b):
    suma = a + b
    return suma


print(sumar(55, 4))


# Documentar funciones con docstrings
def restar(a, b):
    """Resta 2 numeros y devuelve el resultado"""
    resta = a - b
    return resta


print(restar(10, 7))
print(restar.__doc__)


# Parametros por defecto
def multiplicar(a, b=2):
    return a * b


print(multiplicar(2))


# Argumentos por clave
def describir_persona(nombre, edad, sexo):
    print(f"Soy {nombre}, tengo {edad} años y soy {sexo}")


# parametros son posicionales
describir_persona("jhon", 30, "hombre")
describir_persona(30, "hombre", "jhon")

# argumentos por clave
# parametros nombrados
describir_persona(sexo="hombre", edad=30, nombre="Snow")

# Argumentos de longitud de variables (*args)
def sumar_numeros(*args):
    suma = 0
    for numero in args:
        suma += numero
    return suma

print(sumar_numeros(1,2,3,4,5,6,7,8,9,10))
print('\n')


# Argumentos de clave valor  variable (**kwargs)
def mostrar_informacion_de(**kwargs):
    for clave,valor in kwargs.items():
        print(f'{clave}: {valor}')

mostrar_informacion_de(nombre="jhon",edad=30,sexo="hombre")
print('\n')
mostrar_informacion_de(nombre="Wick",edad=30,pais='USA')
print('\n')
mostrar_informacion_de(nombre="Bond",es_mayor=True,sexo="mujer")
