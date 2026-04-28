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
text = "El numero de telefono es 65815615781"
found = re.findall(r"\d", text)
print(found)
