###
# 01 reg3x - expresiones  regulares
###

# 1. Importar el modulo de expresiones regulares (re)
import re

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