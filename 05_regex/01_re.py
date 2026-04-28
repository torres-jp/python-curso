###
# 01 reg3x - expresiones  regulares
###

# 1. Importar el modulo de expresiones regulares (re)
import os
import re

os.system("cls")

"""Las expresioens regulares son una  secuencia de  caracteres que forman un patron de  busqueda.
Se utilizan para la busqueda de cadenas de texto , validacion de datos, etc...
"""

"""Porque aprender regex?
    - Busqueda avanzada: Encontrar patrones especificos en textos grades de forma rapida y precisa.(un editror de markdown solo  usando Regex)
    - Validacionn de datos: Asegurarte que los datos ingresados  por  el usario sean correctos. Ej: correos, usuarios, passwords
    - Extraccio de informacion: Permitir obtener  y aprovechar datos especificos de un texto, como nombres, fechas, o direcciones
    - Manipulacion del texto: Extraer ,  reemplazar y modificar partes de la cadena de texto facilmennte.
"""


# 2. Crear un patron de cadenna de texto que describe que lo queremos econtrar
pattern = "Hola"

# 3. El texto donde lo queremos  buscar.
texto = "Hola mundo"

# 4. Usar la funcion de busqueda re
result = re.search(pattern, texto)

if result:
    print("He encontrado el patron en el texto")
else:
    print("No he encontrado el patron en el texto")

# .group() devuelve la cadena que coincide con el pattern
print(result.group())

# .start() devuelve la posicion inicial de la coincidencia
print(result.start())

# .end() devuelve la posicion final de la coincidiencia
print(result.end())


###########
###########

# EJERCICIO 01
# Encuentra la primera ocurrencia de la palabra IA en el siguiente texto
# e indica en que posicion empieza y termina la coincidencia
text = "Todo el mundo dice que la IA nos va quitar el trabajo. Pero solo hace falta ver como puede cargar con las Regex para ir con cuidado"
pattern = "IA"
found_ia = re.search(pattern, text)

if found_ia:
    print(
        f"He encontrado el patron en el texto en la posicion {found_ia.start()} y termina en la posicion {found_ia.end()}"
    )
else:
    print("No he encontrado el patron en el texto")


# -------------------------

### Encontrar todas las coincidencias de un patron
# .findall() devuelve una lista con todas las coincidencias

text = "Me gusta Python. Python es lo maximo, aunque Python no es tan dificil."
pattern = "Python"

matches = re.findall(pattern, text)
print(len(matches))


# -----------------------

# .iter() devuelve un iterador que contiene todos los resultados de la busqueda.

text = "Me gusta Python. Python es lo maximo, aunque Python no es tan dificil."
pattern = "Python"

matches = re.finditer(pattern, text)

for match in matches:
    print(match.group(), match.start(), match.end())


### Modificadores
# Los modificadores son opciones que se pueden agregar a un patron para cambiar su comportamiento

# re.IGNORECASE: Ignora las mayusculas y minusculas

text = "Todo el mundo dice que la IA nos va quitar el trabajo. Pero solo hace falta ver como puede cargar con las Regex para ir con cuidado, pero la ia no es tan mala. Aprende a usar Ia"
pattern = "IA"
found_ia = re.findall(pattern, text, re.IGNORECASE)

if found_ia:
    print(found_ia)


### Reemplazar el texto
# .sub() reemplaza todas las coincidencias del patron en un texto
text = "hola mundo, hola de nuevo!!"
pattern = "hola"
replacement = "Adios"
