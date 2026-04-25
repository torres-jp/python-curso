###
# 04 - Dictionaries
# Los diccionarios son colecciones de pares clave-valor.
# Sirven para almacenar datos relacionados.
###

# Ejemplo tipico de diccionario
persona = {
    "nombre": "jhon",
    "edad": 33,
    "es_estudiante": True,
    "calificaciones": [7, 8, 9],
    "socials": {
        "twitter": "@jhonn",
        "instagram": "@jhon",
        "facebook": "@jhon",
    },
}

# Para acceder a los valores
print(persona["nombre"])
print(persona["calificaciones"][1])

# Cambiaar valores al acceder
persona["nombre"] = "James"
print(persona["nombre"])

persona["calificaciones"][2] = 10
print(persona["calificaciones"])


# Eliminar una propiedad
del persona["edad"]
# print(persona)

es_estudiante = persona.pop("es_estudiante")
print(f"es estudiante: {es_estudiante}")
print(persona)


# Sobreescribir un diccionario con otro diccionario
a = {"nombre": "Gato", "edad": "33"}
b = {"nombre": "Perro", "es_estudiante": True}

a.update(b)
print(a)


# Comprobar si existe una propiedad
print("name" in persona)  # False
print("nombre" in persona)  # True

# Obtener todas las claves
print("\n Obtener todas las claves: ")
print(persona.keys())

# Obtener todos los valores
print("\n Obtener todos los valores: ")
print(persona.values())

# Obtener todos los pares clave-valor
print("\n Obtener todos los pares clave-valor: ")
print(persona.items())


for key, value in persona.items():
    print(f"{key}: {value}")
