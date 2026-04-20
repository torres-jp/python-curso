###
# 03 - range()
# permite crear una secuencia de numeros
###
import os
os.system('cls')


print('\n range: ')
# range no crea una lista
nums = range(10)

# genera una secuencia de numeros del 0 al 9
# for num in range(10):
#     print(num)

# range( inicio a fin)
# for num in range(5,10):
#     print(num)

# range(inicio a fin, paso)
# for num in range(0,10,2):
#     print(num)

# range (negativos)
# for num in range(-5,0):
#     print(num)


# for num in range(10,0,-1):
#     print(num)

# creando una lista con range().
nums = range(10)
list_of_nums = list(nums)
print(list_of_nums)


contador = 0
while contador < 5:
    print('Hacer 5 veces algo.')
    contador += 1
    
print('\n con for')
for _ in range(5):
    print('Hacer 5 veces algo.')