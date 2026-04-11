###
# 04 - lista - métodos
# Los metodos son importantes para manipular las listas, ya que nos permiten agregar, eliminar, ordenar y realizar otras operaciones en las listas de manera eficiente.
###

import os
os.system('cls' if os.name == 'nt' else 'clear')

## Metodos de listas

#          0    1    2    3    4
lista1 = ['a', 'b', 'c', 'd', 'e']

# Agregar elementos a la lista
lista1.append('f') # Agrega un elemento al final de la lista
print(lista1)

lista1.insert(1,'@') # Agrega un elemento en una posición específica
print(lista1)

lista1.extend(['g', 'h', 'i']) # Agrega varios elementos al final de la lista
print(lista1)