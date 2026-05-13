import re
import os

os.system("cls")


# [: Coincide con cualquier caracter dentro de los corchetes]
text = "useR.ame_33+"
pattern = r"[\w._%+-]+"

matches = re.search(pattern, text)
# if matches:
# print("el nombre es valido")
# else:
# print("el nombre no es valido")


# Buscar todas las vocales
text = "hola mundo"
pattern = r"[aeiou]"

matches = re.findall(pattern, text)
# print(matches)

# Una Regex para encontrar las palabras man,fan,ban
# pero ignora el resto
text = "man ñam ran ban superman"
pattern = r"[mfb]an"

matches = re.findall(pattern, text)
# print(matches)

# [^]: Coincide con cualquier caracter que no este dentro de los corchetes
text = "hola mundo"
pattern = r"[^aeiou]"

matches = re.findall(pattern, text)
# print(matches)
