###
# 03 - Quantifiers
# Los quantification se utilization para specificities canvas occurrences de un character o group de characters se deben encontrar en una cadena
###

import re
import os

os.system("cls")
# *: Puede aparecer 0 o mas vices
text = "aaaba"
pattern = "a*"
matches = re.findall(pattern, text)
# print(matches)

# Coercion 1:
# ¿Cuantas palabras tiene de a 0 o mas 'a' y despises una b?

# +: Una a mas vices
text = "dddd aaa ccc bb casa asado"
pattern = "a+"
matches = re.findall(pattern, text)
# print(matches)

# ?: Puede aparecer 0 o 1 vez)
text = "aaaba"
pattern = "a?b"
matches = re.findall(pattern, text)
# print(matches)

# {n} Exactamente n veces
text = "aaaaaa"
pattern = "a{3}"
matches = re.findall(pattern, text)
# print(matches)

# {n, m} De n a m veces
text = "uu uuuu uuu uu u"
pattern = r"\w{2,3}"
matches = re.findall(pattern, text)
# print(matches)

# Ejercicio: encuentra las palabras con 4 a 6 letras
words = "ala pala muercielago leon casa arbol"
pattern = r"\b\w{4,6}\b"
matches = re.findall(pattern, words)
# print(matches)

# Encuentra las palabras con mas de 6 letras
words = "ala pala muercielago leon casa arbol fantastico"
pattern = r"\b\w{6,}\b"
matches = re.findall(pattern, words)
print(matches)
