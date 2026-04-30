###
# 02 - Meta caracteres
# Los caracteres mas comunes en las expresiones regulares
###

import os
import re

os.system("cls")

# 1. el punto (.)
# Coincidir con cualquier caracter excpepto una nueva linea.

text = "Hola mundo, H0la de nuevo!, HOla otra vez"
pattern = "H.la"
found = re.findall(pattern, text)
# print(found)

texto = "casa cosa cisa causa caasa cesa"
pattern = "c.sa"
found_c = re.findall(pattern, texto)

# if found_c:
#     print(found_c)
# else:
#     print("No he encontrado ninguna coincidencia")


# ----------------------------------------------

text = "Hola mundo, H0la de nuevo!, HOla otra vez"
pattern = r"H.la"
found = re.findall(pattern, text)
# print(found)


# Como usar la barra invertida para anular el significado especial de un simbolo
text = "Mi casa es blanca. Y el coche es negro."
pattern = r"\."
matches = re.findall(pattern, text)
# print(matches)

# \d: coincide con calquier digito del 0-9
text = "El numero de telefono es 321456"
found = re.findall(r"\d{6}", text)
# print(found)

# EJERCICIO: Detectar si hay un numero de telefono en el texto gracias al prefijo +54
text = "Mi numero de telefono es +54 658987523 ok?"
pattern = r"\+54 \d{9}"
found = re.search(pattern, text)
# if found:
#     print(f"Encontre el numero de telefono {found.group()}")
# else:
#     print("No he encontrado el numero de telefono")


# \w: Coincide con cualquier caracter alfa numerico(a-z, A-Z, 0-9, _)
text = "@#$%&/(la_cobra_99"
pattern = r"\w"
found = re.findall(pattern, text)
# print(found)

# \s: Coincide con cualquier espacio en blanco (espacio,tabulacion,salto de linea)
text = "hola mundo\n ¿Como estas?\t"
pattern = r"\s"
found = re.findall(pattern, text)
# print(found)


# ^: Coinicide con el principio de una cadena
username = "Usuariox"
pattern = r"^\w"

valid = re.search(pattern, username)
# if valid:
#     print("El nombre de usuario es valido")
# else:
#     print("El nombre de usuario no es valido")


# $: Coincide con el final de una cadena
text = "Hola mundo"
pattern = r"mundo$"
valid = re.search(pattern, text)

# if valid:
#     print("El texto es valido")
# else:
#     print("El texto no es valido")


# EJERCICIO
# Valida que un correo sea de gmail
text = "correo@gmail.com"
pattern = r"@gmail.com$"
valid = re.search(pattern, text)

# if valid:
#     print("El correo es valido")
# else:
#     print("El correo no es valido")


# EJERCICIOS: tenemos una lista de archivos y necesitamos saber los nombres de los ficheros
# con la extension .txt
files = "fiile1.txt file2.pdf web-off.webpp  secret.txt"
pattern = r"\w+\.txt"
found = re.findall(pattern, files)
# print(found)


# \b: coincide con el principio o final de una palabra
text = "casa coche perro acasa acasado casada casado, casa"
pattern = r"\bcasa\b"
found = re.findall(pattern, text)
# print(found)

# |: Coincide con cualquiera de las dos opciones
texto = "pera, banana, manzana, frutilla"
pattern = r"banana|manzana"
found = re.findall(pattern, texto)
print(found)
