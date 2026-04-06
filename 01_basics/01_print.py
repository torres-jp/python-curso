###
# 01 - print()
# El modulo print() es el modulo que imprime en pantalla lo que le indiquemos entre parentesis. Es la forma mas basica de # # # mostrar informacion al usuario.
###


print('hello world')
print("Comillas dobles")

print('python', 'es', 'un', 'lenguaje', 'de', 'programacion') # Podemos imprimir varias cosas a la vez, separandolas por comas.

print('python', 'es', 'un', 'lenguaje', 'de', 'programacion', 'friendly', sep='-') # Podemos cambiar el separador entre las cosas que imprimimos, usando el parametro sep. En este caso, el separador es un guion.

print('python', 'es', 'un',end='\n')
print('lenguaje', 'de', 'programacion') # Podemos cambiar el final de la impresion, usando el parametro end. En este caso, el final es un signo de exclamacion.