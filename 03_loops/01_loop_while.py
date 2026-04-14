###
# 01 - while loop
# A while loop is a control flow statement that allows code to be executed repeatedly based on a given boolean condition. The code inside the loop will continue to execute as long as the condition is true.
###
import os

os.system("cls")  # Limpiar la consola (en Windows, usa "cls" en lugar de "clear")

print("\n Bucle while: ")

# bucle con una simple condicion
contador = 1
while contador < 6:
    print("Contador:", contador)
    contador += 1  # Incrementamos el contador para evitar un bucle infinito
