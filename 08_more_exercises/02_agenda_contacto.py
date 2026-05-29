import os

os.system("cls" if os.name == "nt" else "clear")


def mostrar_menu():
    print("\nAgenda de Contactos")
    print("1. Agregar contactos")
    print("2. Eliminar contactos")
    print("3. Buscar contactos")
    print("4. Lista de contactos")
    print("5. Salir")


def agregar_contacto(agenda):
    nombre = input("Ingrese el nombre del contacto: ")
    telefono = input("Ingrese el numero de telefono del contacto: ")
    email = input("Ingrese el email del contacto: ")

    agenda[nombre] = {"telefono": telefono, "email": email}
    print(f"Se ha agregado el contacto {nombre} a la agenda.")


def eliminar_contacto(agenda):
    nombre = input("Ingrese el nombre del contacto a eliminar: ")

    if nombre in agenda:
        del agenda[nombre]
        print(f"Se ha eliminado el contacto {nombre} de la agenda.")
    else:
        print(f"No se encontro el contacto {nombre} en la agenda.")


def buscar_contacto(agenda):
    nombre = input("Ingrese el nombre del contacto a buscar: ")

    if nombre in agenda:
        print(f"Contacto encontrado: {nombre}")
        print(f"Telefono: {agenda[nombre]['telefono']}")
        print(f"Email: {agenda[nombre]['email']}")
    else:
        print(f"No se encontro el contacto {nombre} en la agenda.")


def listar_contactos(agenda):
    if agenda:
        print("\nLista de Contactos:")
        for nombre, info in agenda.items():
            print(
                f"Nombre: {nombre}, Telefono: {info['telefono']}, Email: {info['email']}"
            )
            print("_" * 20)
    else:
        print("No hay contactos en la agenda.")


def agenda_contactos():
    agenda = {}

    while True:
        mostrar_menu()

        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            agregar_contacto(agenda)
        elif opcion == "2":
            eliminar_contacto(agenda)
        elif opcion == "3":
            buscar_contacto(agenda)
        elif opcion == "4":
            listar_contactos(agenda)
        elif opcion == "5":
            print("Saliendo de la agenda...")
            break
        else:
            print("Opcion no valida. Intente de nuevo.")


agenda_contactos()
