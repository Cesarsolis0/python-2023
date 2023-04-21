import array
import random
n=int("ingrese el tamaño del arreglo: ")
lista = list(range(1,n))
random.shuffle(lista)
array1 = array.array('I', lista)
print(array1)

n = int(input('¿Que elemento quieres buscar? '))
print(f'El elemento {n} esta en la posición {array1.index(n)+1}.')
