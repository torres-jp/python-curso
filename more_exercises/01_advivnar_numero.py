import random
import os

os.system(
    "cls" if os.name == "nt" else "clear"
)  # Limpiar la consola al iniciar el juego


def juego_adivinar_numero():
    # Generar un número aleatorio entre 1 y 100
    numero_secreto = random.randint(1, 100)
    intentos = 0
    Adivinado = False

    print("¡Bienvenido al juego de adivinar el número!")
    print("Estoy pensando en un número entre 1 y 100. ¿Puedes adivinarlo?")
    print("Intenta adivinar el número. Escribe 'salir' para terminar el juego.")

    while not Adivinado:
        # Solicitar al usuario que ingrese su numero
        adivinanza = input("Ingresa el numero del 1 al 100: ")

        # Verificar que el número ingresado sea válido
        if adivinanza.isdigit():
            adivinanza = int(adivinanza)
            intentos += 1
            if adivinanza < numero_secreto:
                print(f"El numero secreto es mayor a {adivinanza}. Intenta de nuevo.")
            elif adivinanza > numero_secreto:
                print(f"El numero secreto es menor a {adivinanza}. Intenta de nuevo.")
            else:
                print(
                    f"¡Felicidades! Has adivinado el número {numero_secreto} en {intentos} intentos."
                )
        else:
            print(
                "Entrada no válida. Por favor, ingresa un número entre 1 y 100 o 'salir' para terminar el juego."
            )


juego_adivinar_numero()
