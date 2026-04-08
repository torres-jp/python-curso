###
# 05 - input()
# la funcion input permite al usuario ingresar datos a traves del teclado.
# El valor ingresado por el usuario se almacena como una cadena (str) por defecto
###

# nombre = input('¿Cual es tu nombre?\n')
# print(f'hola {nombre}, bienvenido a Python!')

# age = input('¿Cuantos años tienes?\n')
# print(f'Dentro de 10 años tendras {int(age) + 10} años.') # Esto no funciona porque age es una cadena, no un numero. Para solucionarlo, debemos convertirlo a un entero (int) o a un numero de punto flotante (float) antes de realizar la operacion matematica.

print('Obteenr multiples entradas del usuario')
country,city = input('En que pais y ciudad vives?\n').split() # La funcion split() divide la cadena en una lista de palabras, utilizando el espacio como separador por defecto. En este caso, se espera que el usuario ingrese el pais y la ciudad separados por un espacio.
print(f'Vives en {city}, {country}.')