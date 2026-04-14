###
# 01 - while loop
# A while loop is a control flow statement that allows code to be executed repeatedly based on a given boolean condition. The code inside the loop will continue to execute as long as the condition is true.
###
import os

os.system("cls")  # Limpiar la consola (en Windows, usa "cls" en lugar de "clear")

print("\n Bucle while: ")
# bucle con una simple condicion
# contador = 0
# while contador <= 5:
#     print("Contador:", contador)
#     contador += 1  # Incrementamos el contador para evitar un bucle infinito

# utilzando break para salir del bucle
print("\n Bucle while con break: ")

# contador = 0
# while contador <= 100:
#     contador += 1
#     print(contador)
#     if contador % 5 == 0:
#         print("Contador es múltiplo de 5, saliendo del bucle.")
#         break  # Salir del bucle cuando el contador sea múltiplo de 5


# utilizando continue para saltar una iteracion
print("\n Bucle while con continue: ")
# contador = 0
# while contador < 10:
#     contador += 1
#     if contador % 2 == 0:
#         continue
#     print(contador)


# else
print("\n Bucle while con else: ")
# contador = 0
# while contador < 5:
#     print(contador)
#     contador += 1
# else:
#     print("Bucle while finalizado")


# contador = 0
# while contador < 5:
#     print(contador)
#     contador += 1
#     break
# else:
#     print("Bucle while finalizado")


# pedirle al usuario un numero que sea positivo
numero = -1
while numero < 0:
    numero = int(input("Escriba un numero positivo: "))
    if numero < 0:
        print("El numero debe ser positivo.")

print(f"El numero que escribiste es: {numero}")
