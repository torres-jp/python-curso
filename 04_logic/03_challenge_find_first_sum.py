"""
Dado un array de números y un número goal, encuentra los dos primeros números del array que sumen el número goal y devuelve sus índices. Si no existe tal combinación, devuelve None.

nums = [4, 5, 6, 2]
goal = 8

find_first_sum(nums, goal)  # [2, 3]
"""

import os

os.system("cls")

# def find_first_sum(nums, goal):
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if nums[i] + nums[j] == goal:
#                 return [i, j]

#     return None  # No se encontro ninguna combinacion


### Solucion usando diccionarios.
def find_first_sum(nums, goal):
    seen = {}  # diccionario para guardar numero y su indice.

    for i, value in enumerate(nums):
        print(f"index: {i}, value: {value}")


nums = [4, 5, 6, 2]
goal = 8
print(find_first_sum(nums, goal))
