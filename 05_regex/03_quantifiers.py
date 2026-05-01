###
# 03 - Quantifiers
# Los cuantificadores se utulizan para espicificar cuantas ocurrencias de un caracter o grupo de caracteres se deben encontrar en una cadena
###

import re
import os

os.system("cls")
# *: Puede aparecer 0 o mas veces
text = "aaaba"
pattern = "a*"
matches = re.findall(pattern, text)
# print(matches)

# Ejercicio 1:
# ¿Cuantas palabras tiene de a 0 o mas 'a' y despues una b?

# +: Una a mas veces
text = "dddd aaa ccc bb casa asado"
pattern = "a+"
matches = re.findall(pattern, text)
# print(matches)

# ?: Puede aparecer 0 o 1 vez)
text = "aaaba"
pattern = "a?b"
matches = re.findall(pattern, text)
print(matches)

# {n} Exactamente n veces
text = "aaaaaa"
pattern = "a{3}"
matches = re.findall(pattern, text)
# print(matches)
