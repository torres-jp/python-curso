"""
En Jurassic Park, se ha observado que los dinosaurios carnívoros, como el temible T-Rex, depositan un número par de huevos. Imagina que tienes una lista de números enteros en la que cada número representa la cantidad de huevos puestos por un dinosaurio en el parque.

Importante: Solo se consideran los huevos de los dinosaurios carnívoros (T-Rex) aquellos números que son pares.

Objetivo:
Escribe una función en Python que reciba una lista de números enteros y devuelva la suma total de los huevos que pertenecen a los dinosaurios carnívoros (es decir, la suma de todos los números pares en la lista).
"""


# Para ver si un numero es par
# siempre usamos el modulo %
# nos da el resto de la division: eggs % 2 == 0
def count_dinosours_eggs(list_eggs) -> int:
    """
    Esta funcion recibe una lista de numeros enteros que representa la cantidad de huevos de dinosaurios diferentes y los numeros pares son los huevos de dinosaurios carnivoros
    """
    total_carnivore_eggs = 0

    for eggs in list_eggs:
        if eggs % 2 == 0:
            total_carnivore_eggs += eggs

    return total_carnivore_eggs


list_eggs = [2, 5, 78, 3, 6, 34, 3, 6, 8, 3, 2, 16, 7, 95, 344535, 3, 34]
print(count_dinosours_eggs(list_eggs))
