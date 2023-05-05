import random

filas1 = int(input("Ingrese la cantidad de filas para la primera matriz: "))
columnas1 = int(input("Ingrese la cantidad de columnas para la primera matriz: "))

def matriz(filas1,columnas1):
    matriz=[]
    for i in range(filas1):
        fila=[]
        for j in range(columnas1):
            fila.append(random.randint(1,5))
        matriz.append(fila)
    return matriz
        
matriz1=matriz(filas1,columnas1)
print(matriz1)

filas2 = int(input("Ingrese la cantidad de filas para la segunda matriz: "))
columnas2 = int(input("Ingrese la cantidad de columnas para la segunda matriz: "))

def matriz(filas2,columnas2):
    matriz=[]
    for i in range(filas2):
        fila=[]
        for j in range(columnas2):
            fila.append(random.randint(1,5))
        matriz.append(fila)
    return matriz

matriz2=matriz(filas2,columnas2)
print(matriz2)


def multiplicacion(matriz1,matriz2):

    if len(columnas1)!=len(filas2):
        print("las matrices no se pueden multiplicar")
    elif len(columnas1)==len(filas2):
        matriz3=[]
        filas=len(matriz1)
        columnas=len(matriz1[0])
        