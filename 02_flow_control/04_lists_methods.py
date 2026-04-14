###
# 04 - lista - métodos
# Los metodos son importantes para manipular las listas, ya que nos permiten agregar, eliminar, ordenar y realizar otras operaciones en las listas de manera eficiente.
###

import os
os.system('cls' if os.name == 'nt' else 'clear')

## Metodos de listas

#          0    1    2    3    4
lista1 = ['a', 'b', 'c', 'd', 'e']

## Agregar elementos a la lista
lista1.append('f') # Agrega un elemento al final de la lista
print(lista1)

lista1.insert(1,'@') # Agrega un elemento en una posición específica
print(lista1)

lista1.extend(['g', 'h', 'i','@']) # Agrega varios elementos al final de la lista
print(lista1)


## Eliminar elementos de la lista
lista1.remove('@') # Elimina la primera ocurrencia de un elemento específico
print(lista1)

lista1.pop() # Elimina el último elemento de la lista y lo devuelve
print(lista1)

lista1.pop(1) # Elimina el elemento en la posición especificada y lo devuelve
print(lista1)

# eliminar un elemento por su indice sin devolverlo
del lista1[4] # Elimina el elemento en la posición especificada sin devolverlo
print(lista1)

lista1.clear() # Elimina todos los elementos de la lista
print(lista1)

# eliminar un rango de elementos por su indice sin devolverlos
lista = [1,2,3,4,5,]
del lista[1:3] # Elimina los elementos en el rango especificado sin devolverlos
print(lista)


## Ordenar y contar elementos en la lista
print('\n Ordenar elementos en la lista: ')
# Modificando la lista original
numbers = [5, 2, 9, 1, 5, 6,201,100,50,75,25,10]
numbers.sort() # Ordena la lista en su lugar
print(numbers)

# Creando una nueva lista ordenada
numbers = [5, 2, 9, 1, 5, 6,201,100,50,75,25,10]
sorted_numbers = sorted(numbers) # Devuelve una nueva lista ordenada
print(sorted_numbers)


print('\n Ordenar elementos en la lista de cadenas de texto: ')
frutas = ["Manzana", "banana", "Pera", "uva", "durazno"]
sorted_frutas = sorted(frutas) # Ordena la lista de cadenas de texto
print(sorted_frutas) # ['Manzana', 'Pera', 'banana', 'durazno', 'uva'] Ordena por orden alfabético, pero las mayúsculas van antes que las minúsculas

frutas.sort(key=str.lower) # Ordena la lista de cadenas de texto ignorando mayúsculas y minúsculas
print(frutas) # ['banana', 'durazno', 'Manzana', 'Pera', 'uva'] Ordena por orden alfabético, ignorando mayúsculas y minúsculas

print('\n Contar elementos en la lista: ')
numeros = [5, 2, 9,25, 1, 5, 6,201,25,100,50,75,25,10]
print(len(numeros)) # Devuelve el número de elementos en la lista
print(numeros.count(25)) # Devuelve el número de veces que un elemento específico aparece en la lista
print(5 in numeros) # Devuelve True si el elemento está en la lista, de lo contrario devuelve False