import random
import os

os.system("cls" if os.name == "nt" else "clear")


def obtener_palabra_secreta() -> str:
    palabras = ["python", "programacion", "ahorcado", "desarrollo", "juego"]
    return random.choice(palabras)


def mostrar_avance(palabra_secreta: str, letras_adivinadas: list) -> str:
    adivinado = ""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            adivinado += letra
        else:
            adivinado += "_"
    return adivinado


def juego_ahorcado():
    palabra_secreta = obtener_palabra_secreta()
    letras_adivinadas = []
    intentos = 7
    juego_terminado = False

    print("¡Bienvenido al juego del Ahorcado!")
    print(f"Tienes {intentos} intentos para adivinar la palabra secreta.")
    print(mostrar_avance(palabra_secreta, letras_adivinadas))

    while not juego_terminado and intentos > 0:
        adivinanza = input("Ingresa una letra: ").lower()

        if len(adivinanza) != 1 or not adivinanza.isalpha():
            print("Por favor, ingresa una letra válida.")
        elif adivinanza in letras_adivinadas:
            print("Ya has adivinado esa letra. Intenta con otra.")
        else:
            letras_adivinadas.append(adivinanza)

            if adivinanza in palabra_secreta:
                print(f'Acertaste! La letra "{adivinanza}" está en la palabra.')
            else:
                intentos -= 1
                print(
                    f'La letra "{adivinanza}" no está en la palabra. Te quedan {intentos} intentos.'
                )
                print(f"Intentos restantes: {intentos}")

        progreso_actual = mostrar_avance(palabra_secreta, letras_adivinadas)
        print(progreso_actual)

        if "_" not in progreso_actual:
            juego_terminado = True
            print(
                f"¡Felicidades! Has adivinado la palabra secreta es: {palabra_secreta}"
            )

    if intentos == 0:
        print(f"¡Has perdido! La palabra secreta era: {palabra_secreta}")


juego_ahorcado()
